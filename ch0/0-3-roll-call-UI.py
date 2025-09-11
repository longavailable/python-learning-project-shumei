# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 2024

@author: 刘小龙

Content: 利用随机数来互动
"""

import sys, random, datetime
from pathlib import Path
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import pandas as pd


class RollCallIncremental(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("增量点名器")
        self.resize(550, 380)
        self.df = None
        self.stu_rows = []
        self.cur_idx = 0
        self.records_new = []      # 本次已点 [(行号, 状态, 得分), ...]
        self.today = datetime.date.today().strftime("%Y-%m-%d")
        self.init_ui()

    # -------------------- UI --------------------
    def init_ui(self):
        v = QVBoxLayout(self)

        grp1 = QGroupBox("1. 导入名单（可含历史）")
        h1 = QHBoxLayout()
        self.lbl_path = QLabel("未选择文件")
        btn_import = QPushButton("选择 CSV/Excel")
        btn_import.clicked.connect(self.import_file)
        h1.addWidget(self.lbl_path, 1)
        h1.addWidget(btn_import)
        grp1.setLayout(h1)
        v.addWidget(grp1)

        grp2 = QGroupBox("2. 点名方式")
        h2 = QHBoxLayout()
        self.mode_group = QButtonGroup()
        for txt, val in [("按学号顺序", True), ("随机", False)]:
            rb = QRadioButton(txt)
            rb.setChecked(val)
            self.mode_group.addButton(rb)
            h2.addWidget(rb)
        h2.addStretch()
        self.btn_start = QPushButton("开始点名")
        self.btn_start.clicked.connect(self.start_call)
        h2.addWidget(self.btn_start)
        grp2.setLayout(h2)
        v.addWidget(grp2)

        self.lbl_current = QLabel("请先导入名单并点击【开始点名】")
        self.lbl_current.setAlignment(Qt.AlignCenter)
        self.lbl_current.setStyleSheet("font-size:22px;color:#0066cc;padding:10px;")
        v.addWidget(self.lbl_current)

        grp3 = QGroupBox("3. 标记出勤（快捷键 1 2 3 4）")
        g = QGridLayout()
        self.score_btn = {}
        shortcuts = ["1", "2", "3", "4"]
        for idx, (txt, st, sc) in enumerate([
            ("出勤", "出勤", 1.0), ("公假", "公假", 0.9),
            ("事假", "事假", 0.8), ("缺勤", "缺勤", 0.0)
        ]):
            btn = QPushButton(f"{txt}  ({shortcuts[idx]})")
            btn.setEnabled(False)
            btn.clicked.connect(lambda _, stat=st, score=sc: self.mark_and_next(stat, score))
            QShortcut(QKeySequence(shortcuts[idx]), self).activated.connect(btn.click)
            g.addWidget(btn, 0, idx)
            self.score_btn[txt] = btn
        grp3.setLayout(g)
        v.addWidget(grp3)

        grp4 = QGroupBox("4. 保存结果（含历史）")
        h4 = QHBoxLayout()
        btn_xlsx = QPushButton("另存 Excel")
        btn_xlsx.clicked.connect(lambda: self.ask_save(is_excel=True))
        btn_csv = QPushButton("另存 CSV")
        btn_csv.clicked.connect(lambda: self.ask_save(is_excel=False))
        h4.addWidget(btn_xlsx)
        h4.addWidget(btn_csv)
        h4.addStretch()
        self.lbl_count = QLabel("本次已点：0")
        h4.addWidget(self.lbl_count)
        grp4.setLayout(h4)
        v.addWidget(grp4)

    # -------------------- 导入 --------------------
    def import_file(self):
        path, _ = QFileDialog.getOpenFileName(
            self, "选择名单", "", "CSV/Excel (*.csv *.xlsx *.xls)")
        if not path:
            return
        try:
            if path.lower().endswith(".csv"):
                self.df = pd.read_csv(path, dtype=str)
            else:
                self.df = pd.read_excel(path, dtype=str)
            if {"学号", "姓名"} - set(self.df.columns):
                QMessageBox.warning(self, "格式错误", "必须包含【学号】【姓名】两列")
                return
            self.df = self.df.fillna("")
            self.lbl_path.setText(Path(path).name)
            QMessageBox.information(self, "成功", f"已加载 {len(self.df)} 人")
        except Exception as e:
            QMessageBox.critical(self, "导入失败", str(e))

    # -------------------- 开始点名 --------------------
    def start_call(self):
        if self.df is None:
            QMessageBox.warning(self, "提示", "请先导入名单")
            return
        self.stu_rows = list(self.df.index)
        order = self.mode_group.checkedButton().text().startswith("按学号")
        if order:
            self.stu_rows.sort(key=lambda i: str(self.df.loc[i, "学号"]))
        else:
            random.shuffle(self.stu_rows)
        self.cur_idx = 0
        self.records_new.clear()
        self.btn_start.setEnabled(False)
        self.pop_next()

    def pop_next(self):
        if self.cur_idx >= len(self.stu_rows):
            self.finish()
            return
        row = self.stu_rows[self.cur_idx]
        stu_id = str(self.df.loc[row, "学号"])
        stu_name = str(self.df.loc[row, "姓名"])
        self.current_row = row
        self.lbl_current.setText(f"{stu_id}  {stu_name}")
        for b in self.score_btn.values():
            b.setEnabled(True)

    def mark_and_next(self, status, score):
        self.records_new.append((self.current_row, status, score))
        self.lbl_count.setText(f"本次已点：{len(self.records_new)}")
        for b in self.score_btn.values():
            b.setEnabled(False)
        self.cur_idx += 1
        self.pop_next()

    def finish(self):
        QMessageBox.information(self, "完成", "本轮点名结束，请及时保存！")
        self.btn_start.setEnabled(True)
        self.lbl_current.setText("—— 点名结束 ——")

    # -------------------- 保存前询问 --------------------
    def ask_save(self, is_excel=True):
        if self.df is None:
            QMessageBox.warning(self, "提示", "暂无数据可保存")
            return
        done = len(self.records_new)
        total = len(self.df)
        left = total - done
        ret = self.custom_msgbox(f"已点名 <b>{done}</b> 位学生，未点名 <b>{left}</b> 位学生",
                                 "请选择操作",
                                 ["继续点名", "确定保存"])
        if ret == 0:   # 继续点名
            return
        # 确定保存
        self.write_back_to_df()
        self.export_file(is_excel)

    # 将 records_new 写回 df（未点部分留空）
    def write_back_to_df(self):
        new_cols = [f"{self.today}_状态", f"{self.today}_得分"]
        for c in new_cols:
            if c not in self.df.columns:
                self.df[c] = ""
        for row, stat, sc in self.records_new:
            self.df.loc[row, new_cols[0]] = stat
            self.df.loc[row, new_cols[1]] = str(sc)

    # -------------------- 实际导出 --------------------
    def export_file(self, is_excel):
        default = f"点名结果_{self.today}.xlsx" if is_excel else f"点名结果_{self.today}.csv"
        path, _ = QFileDialog.getSaveFileName(
            self, "保存文件", default,
            "Excel 文件 (*.xlsx)" if is_excel else "CSV 文件 (*.csv)")
        if not path:
            return
        try:
            out = self.df.sort_values("学号")
            if is_excel:
                out.to_excel(path, index=False)
            else:
                out.to_csv(path, index=False, encoding='utf-8-sig')
            QMessageBox.information(self, "成功", f"已保存：{path}")
        except Exception as e:
            QMessageBox.critical(self, "保存失败", str(e))

    # -------------------- 自定义双按钮消息框 --------------------
    def custom_msgbox(self, text, title, buttons):
        """返回 0/1 表示第几个按钮被点击"""
        msg = QMessageBox(self)
        msg.setWindowTitle(title)
        msg.setText(text)
        msg.setIcon(QMessageBox.Information)
        b0 = msg.addButton(buttons[0], QMessageBox.AcceptRole)
        b1 = msg.addButton(buttons[1], QMessageBox.DestructiveRole)
        msg.setDefaultButton(b0)
        msg.exec_()
        return 0 if msg.clickedButton() == b0 else 1


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = RollCallIncremental()
    w.show()
    sys.exit(app.exec_())