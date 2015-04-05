# -*- coding: utf-8 -*-
from organizer import Organizer
from talk import Talk
import datetime

INPUT_FILENAME = 'talks.txt'

def feed_talks():
    talks = []
    with open(INPUT_FILENAME) as f:
        for line in f:
            talks.append(Talk(line.rstrip()))

    return talks        

def main():

    talks = []

    talks = feed_talks()
    
    organizer = Organizer()

    results = organizer.organize(talks, [180, 240, 180, 240])

    track = 1

    for (index, session) in enumerate(results, start = 1):
        if index % 2:
            print 'Track {0}'.format(track)
            curr_datetime = datetime.datetime(
                2015,
                4,
                5,
                9,
                0,
                0,
                )
        if not index % 2:
            curr_datetime = datetime.datetime(
                2015,
                4,
                5,
                13,
                0,
                0,
                )
            track = track + 1
        for talk in session.talks:
            print '{0:02d}:{1:02d} {2}'.format(curr_datetime.hour,
                                       curr_datetime.minute,
                                       talk.description)
            resultant_time = curr_datetime + datetime.timedelta(minutes=talk.length)
            curr_datetime = resultant_time


if __name__ == '__main__':
    main()