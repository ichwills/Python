import exifread
import re

def  imageread():
        GPS = {}
        date = ''
        picture = open("D:\\1.jpg",'rb')
        imagetext = exifread.process_file(picture)
        for key in imagetext:                           
                print(key,":",imagetext[key])
        print('********************************************************\n********************************************************')
        for q in imagetext:                             
                if q == "GPS GPSLongitude":
                        print("GPS经度 =", imagetext[q],imagetext['GPS GPSLatitudeRef'])
                elif q =="GPS GPSLatitude":
                        print("GPS纬度 =",imagetext[q],imagetext['GPS GPSLongitudeRef'])
                elif q =='Image DateTime':
                        print("拍摄时间 =",imagetext[q])

imageread()