from time import sleep
def progressbar(sleep_time):
    """used to reveal the percent that has been done,
    please input sleep time to countrol how long every two step experience"""
    for i in range(101):
        print(f"{'1'*i+'0'*(100-i)}",end="\r")
        sleep(sleep_time)

progressbar(0.1)