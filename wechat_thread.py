#-*- coding=UTF-8 -*-
import sys
import threading

class TimeWindow:

    def __init__(self):
        self.t = None


    def time_next(self):

        if BaseCheckin.checkin_list != []:

            self.start_timing(60)



    def start_timing(self, dev=900):
        self.t = threading.Timer(dev, self.time_next)

        self.t.start()




