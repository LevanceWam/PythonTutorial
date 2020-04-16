import threading


def timeExpire():
    print("Times up!")


timer = threading.Timer(2.0, timeExpire)
timer.start()
