
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

    def checkIfBetter(self):
        for schedule in self.currentGeneration:
            schedule.calculate_fitness()
            if schedule.get_finess() > self.bestSchedule.get_finess():
                self.bestSchedule = schedule

    def get_scheduleFitness(self, schedule): return schedule.get_finess()

    def crossOver(self):
        generation = self.currentGeneration
        for x in range(self.generationSize):
            print(generation[x].get_finess())
        sortedGeneration = sorted(generation, key=self.get_scheduleFitness, reverse=True)
        print('-----------------------------------------------')
        del sortedGeneration[self.numberOfWiners:]
        for x in range(self.numberOfWiners):
            print(sortedGeneration[x].get_finess())
