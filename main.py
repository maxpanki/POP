import json
from Data import Data
from Schedule import Schedule
from GeneticAlgoritm import GA
from experiment import experiments
from experiment import experiment

if __name__ == '__main__':
    availabilityFile = open('data/dostepnosci.json', "r", encoding="utf-8")
    availability = json.loads(availabilityFile.read())

    workersFile = open('data/pracownicy.json', "r", encoding="utf-8")
    workers = json.loads(workersFile.read())

    studentsFile = open('data/studenci.json', "r", encoding="utf-8")
    students = json.loads(studentsFile.read())

    data = Data(availability, workers, students)

    #experiments are executed very long, uncomment next line to run experiments
    #experiments(data)

    shedule = experiment(data, 50, 8/10, 20, 100)
    shedule.print()


