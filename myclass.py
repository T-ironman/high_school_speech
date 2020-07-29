from playsound import playsound
import datetime
import pyttsx3
import time

class_begin_file = 'classbegin.mp3'
class_over_file = 'classover.mp3'

def get_time():
    time_now = str(datetime.datetime.now())
    #print("现在的时间:",time_now)
    hour = (str(datetime.datetime.now()))[11:13]
    #print("小时:", hour)
    minute = (str(datetime.datetime.now()))[14:16]
    #print("分钟:",minute)
    return time_now[:19],hour,minute

def class_begin(time_now):
    # hxt = pyttsx3.init()
    # hxt.say("现在时间：%s" % time)
    # hxt.runAndWait()
    print("现在时间：%s" % time_now)
    for i in range(2):
        playsound(class_begin_file)
    time.sleep(30)
    time.sleep(30)

def class_over(time_now):
    # hxt = pyttsx3.init()
    # hxt.say("现在时间：%s" % time)
    # hxt.runAndWait()
    print("现在时间：%s" % time_now)
    for i in range(2):
        playsound(class_over_file)
    time.sleep(30)
    time.sleep(30)


def music_for_class(time,hour,minute):
    hour = int(hour)
    minute = int(minute)
    if hour == 7:
        if minute == 55:
            class_begin(time)
        else:
            pass
    elif hour == 8:
        if minute == 35:
            class_over(time)
        elif minute == 45:
            class_begin(time)
        else:
            pass
    elif hour == 9:
        if minute == 25:
            class_over(time)
        elif minute == 55:
            class_begin(time)
        else:
            pass
    elif hour == 10:
        if minute == 35:
            class_over(time)
        elif minute == 45:
            class_begin(time)
        else:
            pass
    elif hour == 11:
        if minute == 25:
            class_over(time)
        elif minute == 35:
            class_begin(time)
        else:
            pass
    elif hour == 12:
        if minute == 15:
            class_over(time)
        else:
            pass
    elif hour == 15:
        if minute == 0:
            class_begin(time)
        elif minute == 40:
            class_over(time)
        elif minute == 50:
            class_begin(time)
        else:
            pass
    elif hour == 16:
        if minute == 30:
            class_over(time)
        elif minute == 40:
            class_begin(time)
        else:
            pass
    elif hour == 17:
        if minute == 20:
            class_over(time)
        elif minute == 30:
            class_begin(time)
        else:
            pass
    elif hour == 18:
        if minute == 10:
            class_over(time)
        else:
            pass
    elif hour == 19:
        if minute == 10:
            class_begin(time)
        elif minute == 50:
            class_over(time)
        else:
            pass
    elif hour == 20:
        if minute == 0:
            class_begin(time)
        elif minute == 40:
            class_over(time)
        elif minute == 50:
            class_begin(time)
        else:
            pass
    elif hour == 21:
        if minute == 30:
            class_over(time)
        elif minute == 40:
            class_begin(time)
        else:
            pass
    elif hour == 22:
        if minute == 20:
            class_over(time)
        else:
            pass
    else:
        pass

def main():
    print("程序运行中")
    while True:
        time_now,hour,minute = get_time()
        #print(time_now,hour,minute)
        music_for_class(time_now,hour,minute)

if __name__ == '__main__':
    main()