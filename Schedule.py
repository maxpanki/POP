from Event import Event
from random import seed
from random import randint
import time


class Schedule:
    def __init__(self, data):
        self.data = data
        self.events = []
        self.numbOfConflicts = 0
        self.fitness = -1
        self.numbOfEvents = 0
        self.isFitnessChanged = True

    def get_events(self): return self.events
    def get_numbOfConflicts(self): return self.numbOfConflicts
    def get_finess(self): return self.fitness
    def get_numbOfEvents(self): return self.numbOfEvents
    def get_isFitnessChanged(self): return self.isFitnessChanged

    def set_numbOfConflicts(self, val): self.numbOfConflicts = val
    def set_events(self, val): self.events = val

    def print(self):
        eventsSorted = sorted(self.get_events(), key=lambda x: ord(x.get_meetingTime()[0])*10+ord(x.get_meetingTime()[2]), reverse=False)
        for event in eventsSorted:
            event.print()


    def calculate_fitness(self):
        events = self.get_events()
        availability = self.data.get_availability()
        #First part - verifies that schedule can exist
        for event_i in events:

            promoter = event_i.get_promoter()
            if not event_i.checkIfHasTime(promoter, availability):
                self.numbOfConflicts += 1
                print('A')
            reviewer = event_i.get_reviewer()
            if not event_i.checkIfHasTime(reviewer, availability):
                self.numbOfConflicts += 1
                print('A')
            memCom = event_i.get_memCom()
            for mem in memCom:
                if not event_i.checkIfHasTime(mem, availability):
                    self.numbOfConflicts += 1
                    print('A')

            a = [promoter, reviewer, *memCom]
            seen = set()
            dupes = []
            for x in a:
                if x in seen:
                    dupes.append(x)
                else:
                    seen.add(x)
            self.numbOfConflicts += len(dupes)
            print('some B')
            for event_j in events:
                if event_i.get_id() != event_j.get_id():
                    if event_j.get_meetingTime() == event_i.get_meetingTime():
                        self.numbOfConflicts += 2
                        print('C')
        if self.numbOfConflicts > 0:
            fitness = 1 / (1.0 * self.numbOfConflicts)
            self.fitness = fitness
            return fitness
        #Second part - optimization
        current_fitness = 1
        for day in range(0, 10):
            todaysEvents = []
            todaysAssignedWorkers = []
            for x in events:
                if x.get_meetingTime()[0] == str(day):
                    todaysEvents.append(x)
            for event in todaysEvents:
                todaysAssignedWorkers.append(event.get_promoter())
                todaysAssignedWorkers.append(event.get_guide())
                todaysAssignedWorkers.append(event.get_reviewer())
                todaysAssignedWorkers.extend(event.get_memCom())
            seen = set()
            uniq = []
            for x in todaysEvents:
                if x not in seen:
                    uniq.append(x)
                    seen.add(x)
            numberOfWorkers = len(uniq)
            current_fitness += 1/(1.0 * numberOfWorkers + 1)
        self.fitness = current_fitness
        return current_fitness


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
                if currentStudentFreeTime['dostepnosci'][currentTimeSlot] == currentPromoterFreeTime['dostepnosci'][currentTimeSlot] == currentReviewerFreeTime['dostepnosci'][currentTimeSlot]:
                    commonFreeHours.append(currentTimeSlot)
                currentTimeSlot = str(round(float(currentTimeSlot) + 0.1, 1))
            seed(time.time())
            choosenTimeSlot = commonFreeHours[randint(0, len(commonFreeHours) - 1)]
            newEvent.set_meetingTime(choosenTimeSlot)

            for guide in guideArray:
                currentGuideTimeslots = next((x for x in availability if x['numer_osoby'] == guide['numerOsoby']), None)
                if currentGuideTimeslots['dostepnosci'][choosenTimeSlot] == 1:
                    newEvent.set_przewodnicacy(guide['numerOsoby'])
                    break

            memComAcceptedArray = []
            tempMemComArray = []
            for memCom in memComArray:
                currentMemComTimeslots = next((x for x in availability if x['numer_osoby'] == memCom['numerOsoby']), None)
                if currentMemComTimeslots['dostepnosci'][choosenTimeSlot] == 1:
                    tempMemComArray.append(memCom['numerOsoby'])

            for x in range(1):
                rand = randint(0, len(tempMemComArray) - 1)
                memComAcceptedArray.append(tempMemComArray[rand])

            newEvent.set_czlKom(memComAcceptedArray)
            self.events.append(newEvent)
            self.numbOfEvents += 1

        return self
