import requests
import re
import os
import time
from urllib.parse import urlparse, urljoin
from bs4 import BeautifulSoup


def wechat_order_downloader():
    headers = {
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_7_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.15(0x18000f2e) NetType/WIFI Language/zh_CN',
        'Referer': 'https://mp.weixin.qq.com/'
    }

    article_url = input("请输入公众号文章地址：").strip()

    if not article_url.startswith('http'):
        print("错误：请输入有效网址（以http/https开头）")
        return

    try:
        # 获取页面内容
        response = requests.get(article_url, headers=headers, timeout=15)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'lxml')

        # 创建按日期时间命名的专属目录
        timestamp = time.strftime("%Y%m%d_%H%M%S")
        save_dir = f"wechat_images_{timestamp}"
        os.makedirs(save_dir, exist_ok=True)

        # 核心解析逻辑
        img_counter = 1  # 图片序号计数器
        duplicate_check = set()  # 重复图片校验

        for idx, img_tag in enumerate(soup.find_all('img'), 1):
            # 优先获取data-src属性（微信懒加载专用）
            img_url = img_tag.get('data-src') or img_tag.get('src')

            # 处理相对路径和无效URL
            if not img_url or 'http' not in img_url:
                continue
            full_url = urljoin(article_url, img_url)

            # 过滤非微信图床链接
            if 'mmbiz.qpic.cn' not in full_url:
                continue

            # 转换高清链接
            if '/640?' in full_url:
                hd_url = full_url.replace('/640?', '/0?')
            else:
                hd_url = full_url  # 已为高清地址则直接使用

            # 去重校验（精确到图片ID）
            unique_key = hd_url.split('/')[-2]
            if unique_key in duplicate_check:
                continue
            duplicate_check.add(unique_key)

            # 下载并保存
            try:
                response = requests.get(hd_url, headers=headers, timeout=10)
                if response.status_code == 200:
                    # 提取图片格式（优先URL参数，兜底用header）
                    content_type = response.headers.get('Content-Type', '')
                    fmt = 'jpg'  # 兜底默认格式
                    if 'wx_fmt=' in hd_url:
                        fmt = hd_url.split('wx_fmt=')[-1].split('&')[0]
                    elif 'image/' in content_type:
                        fmt = content_type.split('/')[-1]

                    # 生成顺序编号文件名
                    filename = f"{img_counter:03d}.{fmt}"
                    save_path = os.path.join(save_dir, filename)

                    # 保存文件
                    with open(save_path, 'wb') as f:
                        f.write(response.content)

                    print(f"✅ 保存第 {img_counter} 张图片 → {filename}")
                    img_counter += 1
                else:
                    print(f"❌ 下载失败（状态码 {response.status_code}）: {hd_url[:60]}...")

            except Exception as e:
                print(f"⚠️ 异常下载项：{str(e)[:50]}...")

            time.sleep(0.3)  # 礼貌访问间隔

        print(f"\n🎉 下载完成！共保存 {img_counter - 1} 张图片到【{save_dir}】目录")

    except requests.RequestException as e:
        print(f"网络请求失败：{str(e)}")
    except Exception as e:
        print(f"程序异常：{str(e)}")

if __name__ == '__main__':
    wechat_order_downloader()
