import time
import webbrowser


def break_time(max_breaks):
    break_count = 0
    while break_count < max_breaks:
        print("begin || " + time.ctime())
        time.sleep(1)
        print("after sleep")
        webbrowser.open("https://www.youtube.com/watch?v=xzHvOthWpJ4")
        # print('webbrowser.open("https://www.youtube.com/watch?v=xzHvOthWpJ4")')
        break_count += 1
        print(break_count)

break_time(3)