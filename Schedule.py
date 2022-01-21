from Event import Event
from random import seed
from random import randint


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
        availability = self.data.get_availability()
        memComArray = []
        guideArray = []
        for worker in workers:
            w = next((x for x in worker['role'] if x == 'Przewodniczacy'), False)
            if w:
                guideArray.append(worker)

        for worker in workers:
            w = next((x for x in worker['role'] if x == 'Czlonek komisji'), False)
            if w:
                memComArray.append(worker)

        for idx, student in enumerate(students):
            newEvent = Event(idx, student['numer_osoby'], student['numer_opiekuna'], student['numer_recenzenta'])
            currentStudentFreeTime = next((x for x in availability if x['numer_osoby'] == student['numer_osoby']), None)
            currentPromoterFreeTime = next((x for x in availability if x['numer_osoby'] == student['numer_opiekuna']),
                                           None)
            currentReviewerFreeTime = next((x for x in availability if x['numer_osoby'] == student['numer_recenzenta']),
                                           None)
            commonFreeHours = []
            currentTimeSlot = '0.0'
            for x in range(100):
                if currentStudentFreeTime['dostepnosci'][currentTimeSlot] == currentPromoterFreeTime['dostepnosci'][
                    currentTimeSlot] == currentReviewerFreeTime['dostepnosci'][currentTimeSlot]:
                    commonFreeHours.append(currentTimeSlot)
                currentTimeSlot = str(round(float(currentTimeSlot) + 0.1, 1))
            print('For student: ' + student['numer_osoby'] + ' dostępne timesloty to: ' + commonFreeHours)
            seed(1)
            choosenTimeSlot = commonFreeHours[randint(0, len(commonFreeHours))]
            newEvent.set_meetingTime(choosenTimeSlot)

            for guide in guideArray:
                currentGuideTimeslots = next((x for x in workers if x['numer_osoby'] == guide['numerOsoby']), None)
                if currentGuideTimeslots['dostepnosci'][choosenTimeSlot] == 1:
                    newEvent.set_przewodnicacy(guide['numerOsoby'])
                    break

            memComAcceptedArray = []
            tempMemComArray = []
            for memCom in memComArray:
                currentMemComTimeslots = next((x for x in workers if x['numer_osoby'] == memCom['numerOsoby']), None)
                if currentMemComTimeslots['dostepnosci'][choosenTimeSlot] == 1:
                    tempMemComArray.append(memCom['numerOsoby'])

            for x in range(3):
                rand = randint(0, len(tempMemComArray))
                memComAcceptedArray.append(tempMemComArray[rand])

            newEvent.set_czlKom(memComAcceptedArray)
            self.events.append(newEvent)
            self.numbOfEvents += 1

        return self
