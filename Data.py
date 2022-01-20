class Data:
    def __init__(self, availability, workers, students):

        self.availability = availability
        self.workers = workers
        self.students = students

    def get_students(self): return self.students
    def get_workers(self): return self.workers
    def get_availability(self): return self.availability

    def __str__(self): return str('Output data')
