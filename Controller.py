# ****************************************************************************
# Commented lines in the code must be uncommented when the related classes
# are pushed and are available. For now we only know these lines must be there.
# ****************************************************************************

import os

# from AI import AI
from threading import Thread
from queue import Queue
from Model import World

class Controller():

    def __init__(self):
        self.sending_flag = True
        self.conf = {}
        self.network = None
        self.queue = Queue()
        self.world = World(self.queue)
        # self.client = AI()
        self.argNames = ["AICHostIP", "AICHostPort", "AICToken", "AICRetryDelay"]
        self.argDefaults = ["127.0.0.1", 7099, "00000000000000000000000000000000", "1000"]

    def start(self):
        self.read_settings()
        # self.network = Network(ip=self.conf[self.argNames[0]],
        #                        port=self.conf[self.argNames[1]],
        #                        token=self.conf[self.argNames[2]],
        #                        message_handler=self.handle_message)
        # self.network.connect()

        def run():
            while self.sending_flag:
                event = self.queue.get()
                self.queue.task_done()
                message = {
                    'name': Event.EVENT,
                    'args': [{'type': event.type, 'args': event.args}]
                }
                # self.network.send(message)

        Thread(target=run, daemon=True).start()

    def terminate(self):
        print("finished!")
        # self.network.close()
        self.sending_flag = False

    def read_settings(self):
        if os.environ.get(self.argNames[0]) is None:
            for i in range(len(self.argNames)):
                self.conf[self.argNames[i]] = self.argDefaults[i]
        else:
            for i in range(len(self.argNames)):
                self.conf[self.argNames[i]] = os.environ.get(self.argNames[i])

    def handle_message(self, message):
        pass

    def do_turn(self):

        def run():
            # self.client.do_turn(self.world)
            pass

        Thread(target=run, daemon=True).start()

# This class should be moved to Model.py
class Event:
    EVENT = "event"

    def __init__(self, type, args):
        self.type = type
        self.args = args

    def add_arg(self, arg):
        self.args.append(arg)


c = Controller()
c.start()
