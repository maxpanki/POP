class Schedule:
    def __init__(self, data):
        self.data = data
        self.events = []
        self.numbOfConflicts = 0
        self.fitness = -1
        self.numbOfEvents = 0
        self.isFitnessChanged = True

