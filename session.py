# -*- coding: utf-8 -*-


class Session:

    def __init__(self, length):
        if not isinstance(length, int):
            print 'Length should be an integer'
        self.talks = []
        self.available_time = length

    def add(self, talk):
        if not self.canadd(talk):
            print 'talk too long'
        self.available_time -= talk.length
        self.talks.append(talk)

    def canadd(self, talk):
        if talk.length > self.available_time:
            return False
        else:
            return True



