# -*- coding: utf-8 -*-
import re

LIGHTNING_TALK = 5


class Talk:

    def __init__(self, talk):
        words = talk.split()
        self.length = 0
        mins_pattern = re.compile('\d+min')

        if words[-1] == 'lightning':
            self.length = LIGHTNING_TALK
        elif mins_pattern.match(words[-1]):
            matched_pattern = mins_pattern.match(words[-1]).group()
            matched_pattern = matched_pattern.replace('min', '')
            self.length = int(matched_pattern)
        else:
            print 'incorrect format'

        self.description = talk



            