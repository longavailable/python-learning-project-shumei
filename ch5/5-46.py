# -*- coding: utf-8 -*-
"""
Created on Sun Aug 24 12:18:37 2025

@author: Xiaolong Liu
"""

from wordcloud import WordCloud

str1 = '''
China holds third rehearsal for event marking 80th anniversary of victory over Japanese aggression, fascism
The third comprehensive rehearsal for the upcoming grand gathering to mark the 80th anniversary of the victory in the Chinese People's War of Resistance against Japanese Aggression and the World Anti-Fascist War concluded in Beijing early Sunday, according to the event's media center.
The rehearsal was held from 5 pm Saturday to 5 am Sunday in Tian'anmen Square.
Organizers said it was a full-process, full-element rehearsal and also the final comprehensive one for the commemoration. It focused on testing the coordination between all processes and segments, laying a solid foundation for the success of the event.
All processes were organized in an orderly manner, with tight transitions and smooth operation, achieving the intended objectives, they added.
The grand gathering, which will include a military parade, is scheduled for Sept. 3 in Tian'anmen Square.
'''

wc = WordCloud(background_color='white', width=1000, height=800)

wc.generate(str1)

wc.to_file('victory80-wordcloud.png')
