
import threading
import time

def get_hello():
    print("Function to print hello.")
    time.sleep(10)
    print("hello function is complete.\n")
    return "hello"
def get_world():
    print("Function to print world.")
    time.sleep(5)
    print("world function is complete.\n")
    return "world"

def get_message():
    print("Function to print message.")
    time.sleep(2)
    print("message function is complete.\n")
    return "You are just awesome!"


class Executor:
    def __init__(self, hello, world, message):
        self.threadpools = []
        self.hello = hello
        self.world = world
        self.message = message
        self.hello_response = self.world_response = self.message_response = None

    def execute(self):
        if self.hello:
            self.threadpools.append(threading.Thread(target=self.helper_get_hello, args=()))
        if self.world:
            self.threadpools.append(threading.Thread(target=self.helper_get_world, args=()))
        if self.message:
            self.threadpools.append(threading.Thread(target=self.helper_get_message, args=()))

        for thread in self.threadpools:
            thread.start()
        self.run()

        return self.hello_response, self.world_response, self.message_response

    def run(self):
        for thread in self.threadpools:
            thread.join()

    def helper_get_hello(self):
        self.hello_response = get_hello()

    def helper_get_world(self):
        self.world_response = get_world()

    def helper_get_message(self):
        self.message_response = get_message()


def fun(hello, world, message):
    hello_response = world_response = message_response = False
    message = "failed"
    try:
        e = Executor(hello, world, message)
        hello_response, world_response, message_response = e.execute()
    except Exception:
        pass
    else:
        message = "success"

    return (message, hello_response, world_response, message_response)


if __name__ == "__main__":
    print(fun(True, True, True))
    print("------------")
    print(fun(False, True, True))

