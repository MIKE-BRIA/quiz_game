class job:

  def __init__(self, job_type, salary, hoursworked):

    self.job_type = job_type
    self.salary = salary
    self.hoursworked = hoursworked

  def print(self):
    print("== JOB ==")
    print()
    print(f"{self.job_type:<10} {self.salary:^10} {self.hoursworked:>10}")


class teacher(job):

  def __init__(self, salary, hoursworked, subject, position):

    self.job_type = "Teacher"
    self.salary = salary
    self.hoursworked = hoursworked
    self.subject = subject
    self.position = position

  def print(self):
    print("== JOB ==")
    print()
    print(f"{self.job_type:<10} {self.salary:^10} {self.hoursworked:>10}")
    print(f"{self.subject:<10} {self.position:>21}")


class doctor(job):

  def __init__(self, salary, hoursworked, speciality, experience):

    self.job_type = "Doctor"
    self.salary = salary
    self.hoursworked = hoursworked
    self.speciality = speciality
    self.experience = experience

  def print(self):
    print("== JOB ==")
    print()
    print(f"{self.job_type:<10} {self.salary:^10} {self.hoursworked:>10}")
    print(f"{self.experience:<10} {self.speciality:>21}")


lawyer = job("Lawyer", "$100,000", "40")
lawyer.print()

doc = doctor("$120,000", "48", "7", "Pediatric Consultant")
doc.print()

teach = teacher("$50,000", "48+", "CompSci", "Asst. Principal")
teach.print()
