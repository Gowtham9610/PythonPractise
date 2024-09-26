from datetime import date
from datetime import datetime
print(date.today())
class person():
    def __init__(self,name,country,dob):
        self.name = name
        self.country = country
        self.dob = datetime.strptime(dob,'%Y-%m-%d')
    def get_age(self):
        return date.today().year-self.dob.year


p1 = person("gowtham","Indian","1992-10-16")
print(p1.get_age())
print(p1.name)
person2 = person("govi","indian","1996-05-22")
print(person2.get_age())
