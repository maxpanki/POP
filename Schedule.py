from Event import Event


class Schedule:
    def __init__(self, data):
        self.data = data
        self.events = []
        self.numbOfConflicts = 0
        self.fitness = -1
        self.numbOfEvents = 0
        self.isFitnessChanged = True

    def initialize(self):
        students = self.data.get_students()
        workers = self.data.get_workers()
        availability = self.data.get_workers()
        for idx, student in enumerate(students):
            newEvent = Event(idx, student['numer_osoby'], student['numer_opiekuna'], student['numer_recenzenta'])
            currentPromoter = next((x for x in workers if x['numerOsoby'] == student['numer_opiekuna']), None)
            currentReviewer = next((x for x in workers if x['numerOsoby'] == student['numer_recenzenta']), None)
            print(currentPromoter)


            self.numbOfEvents += 1

        return self
