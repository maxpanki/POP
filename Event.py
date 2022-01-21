class Event:
    def __init__(self, id, student_id, promoter_id, reviewer_id):

        self.id = id
        self.student = student_id
        self.promoter = promoter_id
        self.guide = None
        self.reviewer = reviewer_id
        self.memCom = None
        self.meetingTime = None

    def checkIfHasTime(self, worker, availability):
        workerTime = next((x for x in availability if x['numer_osoby'] == worker), None)
        if workerTime['dostepnosci'][self.meetingTime] == 1:
            return True
        else:
            return False

    def get_student(self): return self.student
    def get_promoter(self): return self.promoter
    def get_id(self): return self.id
    def get_guide(self): return self.guide
    def get_reviewer(self): return self.reviewer
    def get_memCom(self): return self.memCom
    def get_meetingTime(self): return self.meetingTime

    def set_przewodnicacy(self, guide): self.guide = guide
    def set_recenzenci(self, reviewer): self.reviewer = reviewer
    def set_czlKom(self, memCom): self.memCom = memCom
    def set_meetingTime(self, meetingTime): self.meetingTime = meetingTime

    def __str__(self): return str('Output data')
