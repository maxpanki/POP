class MeetingTime:
    def __init__(self, id, time):
        self.id = id
        self.time = time

    def get_id(self): return self.id
    def get_time(self): return self.time

    def __str__(self): return str('Output data')
