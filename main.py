import json
from Data import Data
from Schedule import Schedule
from GeneticAlgoritm import GA

if __name__ == '__main__':
    availabilityFile = open('data/dostepnosci.json', "r")
    availability = json.loads(availabilityFile.read())

    workersFile = open('data/pracownicy.json', "r")
    workers = json.loads(workersFile.read())

    studentsFile = open('data/studenci.json', "r")
    students = json.loads(studentsFile.read())

    data = Data(availability, workers, students)

    firstGeneration = []
    for x in range(10):
        schedule = Schedule(data)
        firstGeneration.append(schedule.initialize())
    ga = GA(firstGeneration, 5, 10, 5)
    ga.checkIfBetter()
    print('-----------------------------------------------')
    ga.crossOver()

