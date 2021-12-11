import threading
import time

sum = 0


class Worker(threading.Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name  # thread 이름 지정

    def run(self):
        global sum
        print("sub thread start ", threading.currentThread().getName())
        for i in range(1, int(self.name) + 1):
            sum += i
        print("sub thread end ", threading.currentThread().getName())


if __name__ == "__main__":
    name = "thread {}".format(10)
    thread = Worker(10)  # sub thread 생성
    thread.start()  # sub thread의 run 메서드를 호출
    thread.join()

    print(f"sum = {sum}")
    print("main thread end")
