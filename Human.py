class Human:
    def __init__(self, name, freeTime, role):
        self.name = name
        self.freeTime = freeTime
        self.role = role

    def get_name(self): return self.name
    def get_freeTime(self): return self.freeTime
    def get_role(self): return self.role

    def __str__(self): return str('Output data')
