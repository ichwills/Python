from wxpy import *
import time
import 搞笑动图
import threading


#bot = Bot(cache_path=True,console_qr=0.5)
bot = Bot(cache_path=True)
myself = bot.self



#图片推送
def tuisong():
    huzhexing = bot.friends().search('胡哲兴')[0]
    xinxing = bot.friends().search('唯一')[0]
    xiaoyu = bot.friends().search('aliyas')[0]
    while True :
        搞笑动图.get()
        xinxing.send_msg("新的动图")
        xinxing.send_image("gif.gif")
        huzhexing.send_msg("新的美图到啦")
        huzhexing.send_image("gif.gif")
        xiaoyu.send_msg("新的图片到啦！")
        xiaoyu.send_image("gif.gif")
        time.sleep(3600)

threads = []
tuisong()

#embed()






