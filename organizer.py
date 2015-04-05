# -*- coding: utf-8 -*-
from session import Session


class Organizer:

    def organize(self, talks, session_lengths):
        self.sessions = self.construct_sessions(session_lengths)
        self.loop_sessions(talks)
        return self.sessions

    def construct_sessions(self, session_lengths):
        sessions = []

        for session_length in session_lengths:
            sessions.append(Session(session_length))
        return sessions

    def loop_sessions(self, talks):
        talks_done = [False for i in range(1, len(talks) + 1)]
        for session in self.sessions:
            self.loop_talks(session, talks, talks_done)

    def loop_talks(
        self,
        session,
        talks,
        talks_done,
        ):
        for (index, talk) in enumerate(talks):
            if talks_done[index]:
                continue
            if session.canadd(talk):
                session.add(talk)
                talks_done[index] = True



            