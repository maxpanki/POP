import json
from Data import Data
from Schedule import Schedule
from GeneticAlgoritm import GA

def experiment(data, generationSize, winnersSizeRatio, mutateRate, numberOfIterations):
    firstGeneration = []
    for x in range(generationSize):
        schedule = Schedule(data)
        firstGeneration.append(schedule.initialize())
    ga = GA(firstGeneration, int(winnersSizeRatio*generationSize), generationSize, mutateRate)
    while ga.get_epoch() < numberOfIterations:
        ga.checkIfBetter()
        ga.crossOver()
        ga.next_epoch()

    print('*|*|*|*|*|*|*|*|*|*|*|*|')
    print("Number of iterations: " + str(numberOfIterations))
    print("Generation size: " + str(generationSize))
    print("Winners / generation size ratio: " + str(winnersSizeRatio))
    print("Mutate rate: " + str(mutateRate))
    print("fitness: " + str(ga.get_bestSchedule().get_fitness()))
    print('*|*|*|*|*|*|*|*|*|*|*|*|')

    return ga.get_bestSchedule()


def experiments(data):

    #generation size
    experiment(data, 10, 8/10, 20, 100)
    experiment(data, 50, 8/10, 20, 100)
    experiment(data, 100, 8/10, 20, 100)

    #mutation rate
    experiment(data, 50, 8/10, 3, 100)
    experiment(data, 50, 8/10, 20, 100)
    experiment(data, 50, 8/10, 90, 100)

    #winners rate
    experiment(data, 50, 8/10, 20, 100)
    experiment(data, 50, 5/10, 20, 100)
    experiment(data, 50, 2/10, 20, 100)






