import json
from Data import Data
from Schedule import Schedule

if __name__ == '__main__':
    availabilityFile = open('data/dostepnosci.json', "r")
    availability = json.loads(availabilityFile.read())

    workersFile = open('data/pracownicy.json', "r")
    workers = json.loads(workersFile.read())

    studentsFile = open('data/studenci.json', "r")
    students = json.loads(studentsFile.read())

    data = Data(availability, workers, students)

    schedule = Schedule(data)
    schedule.initialize()
