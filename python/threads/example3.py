import threading
import time

def thread_function(name):
    print("Thread {} starting".format(name))
    time.sleep(2)
    print("Thread {} finishing".format(name))

if __name__ == "__main__":
    threads = list()
    for index in range(3):
        print("Main    : create and start thread {}".format(index))
        x = threading.Thread(target=thread_function, args=(index,))
        threads.append(x)
        x.start()

    for index, thread in enumerate(threads):
        print("Main    : before joining thread {}".format(index))
        thread.join()
        print("Main    : thread {} done".format(index))
