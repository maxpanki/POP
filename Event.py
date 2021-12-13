class Course:
    def __init__(self, id, student, opiekun):

        self.id = id
        self.student = student
        self.opiekun = opiekun
        self.przewodnicacy = None
        self.recenzenci = None
        self.czlKom = None
        self.meetingTime = None

    def get_student(self): return self.student
    def get_opiekun(self): return self.opiekun
    def get_id(self): return self.id
    def get_przewodnicacy(self): return self.przewodnicacy
    def get_recenzenci(self): return self.recenzenci
    def get_czlKom(self): return self.czlKom
    def get_meetingTime(self): return self.meetingTime

    def set_przewodnicacy(self, przewodnicacy): self.przewodnicacy = przewodnicacy
    def set_recenzenci(self, recenzenci): self.recenzenci = recenzenci
    def set_czlKom(self, czlKom): self.czlKom = czlKom
    def set_meetingTime(self, meetingTime): self.meetingTime = meetingTime

    def __str__(self): return str('Output data')
