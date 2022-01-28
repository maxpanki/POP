import time
import json
from random import seed
from Schedule import Schedule
from Data import Data
from random import random
from random import randint
import copy

class GA:
    def __init__(self, generation, numberOfWiners, generationSize, mutateRate):
        self.currentGeneration = generation
        self.bestSchedule = generation[0]
        self.epoch = 1
        self.numberOfWiners = numberOfWiners
        self.generationSize = generationSize
        self.mutateRate = mutateRate


    def get_bestSchedule(self): return self.bestSchedule
    def next_epoch(self): self.epoch += 1
    def get_epoch(self): return self.epoch

    def checkIfBetter(self):
        for schedule in self.currentGeneration:
            schedule.calculate_fitness()
            if schedule.get_finess() > self.bestSchedule.get_finess():
                print('***************')
                print(schedule.get_finess())
                print('is bigger than')
                print(self.bestSchedule.get_finess())
                self.bestSchedule = schedule
                print(self.get_bestSchedule().get_finess())

    def get_scheduleFitness(self, schedule): return schedule.get_finess()

    def mutate(self):
        availabilityFile = open('data/dostepnosci.json', "r", encoding="utf-8")
        availability = json.loads(availabilityFile.read())

        workersFile = open('data/pracownicy.json', "r", encoding="utf-8")
        workers = json.loads(workersFile.read())

        studentsFile = open('data/studenci.json', "r", encoding="utf-8")
        students = json.loads(studentsFile.read())

        data = Data(availability, workers, students)
        return Schedule(data).initialize()

    def crossOver(self):
        seed(time.time())
        generation = copy.deepcopy(self.currentGeneration)
        sortedGeneration = sorted(generation, key=self.get_scheduleFitness, reverse=True)
        del sortedGeneration[self.numberOfWiners:]
        newGeneration = copy.deepcopy(sortedGeneration)
        while len(newGeneration) != self.generationSize:
            rand1 = randint(0, self.numberOfWiners - 1)
            rand2 = randint(0, self.numberOfWiners - 1)
            while rand1 == rand2:
                rand2 = randint(0, self.numberOfWiners - 1)
            p_1 = copy.deepcopy(sortedGeneration[rand1])
            p_2 = copy.deepcopy(sortedGeneration[rand2])
            child = copy.deepcopy(p_1)
            events = []

            for i in range(0, len(p_1.get_events())):
                if random() > 0.5:
                    events.append(p_2.get_events()[i])
                else:
                    events.append(p_1.get_events()[i])
            child.set_events(events)
            child.set_numbOfConflicts(0)
            if randint(0, 100) <= self.mutateRate:
                child = self.mutate()
            newGeneration.append(child)
        self.currentGeneration = newGeneration



