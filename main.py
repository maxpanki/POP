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
    for x in range(50):
        schedule = Schedule(data)
        firstGeneration.append(schedule.initialize())
    ga = GA(firstGeneration, 40, 50, 20)
    while ga.get_bestSchedule().get_finess() < 1 or ga.get_epoch() < 5000:
        ga.checkIfBetter()
        print('k')
        print(ga.get_bestSchedule().get_numbOfConflicts())
        print('k')
        print(ga.get_bestSchedule().get_finess())
        print('-----------------------------------------------')
        ga.crossOver()
        ga.next_epoch()
    print('*|*|*|*|*|*|*|*|*|*|*|*|')
    print(ga.get_bestSchedule().get_finess())
    print('*|*|*|*|*|*|*|*|*|*|*|*|')


