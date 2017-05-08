import random
import math
from collections import defaultdict
import sys,os

STAT_MOBILITY = {
    "outstanding": 140,
    "athletic": 120,
    "normal": 100,
    "disabled": 10,
    "ill": 80,
    "injured": 70,
    "severely ill/injured": 0
}

SEX_DIC = {"Male" : 10,
       "Female" : -6,
}

# The numbers mean entropy
ETHNICITY = {'Sang' : 1,
             'Gah-Uun Deh' : 3,
             'A-reh' : 4}

current_path = "."
data_path = os.path.join(current_path, 'data')

"""Sort out Names"""
names_list = defaultdict(list)


with open(os.path.join(data_path, 'names.txt'), 'r') as names:
    current_allocation = None
    lines = names.readlines()
    for line in lines:
        if line.strip() == 'Sang_Male':
            current_allocation = 'Sang_Male'
        elif line.strip() == 'Sang_Female':
            current_allocation = 'Sang_Female'
        elif line.strip() == 'Gah-Uun Deh_Male':
            current_allocation = 'Gah-Uun Deh_Male'
        elif line.strip() == 'Gah-Uun Deh_Female':
            current_allocation = 'Gah-Uun Deh_Female'
        elif line.strip() == 'Ah-reh_Male':
            current_allocation = 'Ah-reh_Male'
        elif line.strip() == 'Ah-reh_Female':
            current_allocation = 'Ah-reh_Female'
        elif line.strip() == None:
            continue
        else:
            print(current_allocation, ' = ' ,line)
            names_list[current_allocation].append(line.strip('\n'))


"""Create human templet"""
class Person(object):
    def __init__(self, ethnicity, sex, age, name = None, Unusual = None):
        """Basic info"""
        self.__name = None
        self.__sex = sex
        self.__ethnicity = ethnicity
        self.__age = age

        """Stats"""
        if Unusual == "Yes":
            life = random.randrange(0, 6)
            if life == 0:
                self.__mobility = STAT_MOBILITY["outstanding"]
            elif life == 1:
                self.__mobility = STAT_MOBILITY["athletic"]
            elif life == 2:
                self.__mobility = STAT_MOBILITY["disabled"]
            elif life == 3:
                self.__mobility = STAT_MOBILITY["ill"]
            elif life == 4:
                self.__mobility = STAT_MOBILITY["injured"]
            elif life == 5:
                self.__mobility = STAT_MOBILITY["severely ill/injured"]
        else :
            self.__mobility = STAT_MOBILITY["normal"]
        self.__melee = 100
        self.__aim = 100

        self.__inteligence = 0
        self.__focus = 100
        self.__reaction = 100

        """Post-processing booleans"""
        self.__processed = False
        self.__isleader = False
        if age < 12:
            self.__ischild = True
        elif age > 55:
            self.__iselder = True
        else:
            self.__ischild = False
            self.__iselder = False
    def statcalc(self):
        """Calculates and randomizes personal stats based on sex, age, ethnicity with a bit of abnormality factor"""

        """Mobility calculation"""
        self.__mobility = self.__mobility + (35 - self.__age) + random.randrange(-20, 20) + (SEX_DIC[self.__sex] * (5 - ETHNICITY[self.__ethnicity]))
        if self.__age < 8:
            self.__mobility = int(self.__mobility / (10 -self.__age))
        if self.__mobility < 0:
            self.__mobility = 0

        """Melee/aim calculation"""

        self.__inteligence += (self.__age * 2)  + random.randrange(-20, 20)
        self.__focus = -(((int(self.__age/5) - 10)**2) -100) +  random.randrange(-30, 30)
        if self.__focus < 0:
            self.__focus = 0
        self.__reaction = -(((int(self.__age/3) - 10)**2) - 100) +  random.randrange(-30, 30)
        if self.__reaction < 0:
            self.__reaction = 0
        self.__melee += self.__mobility + self.__focus + random.randrange(-20, 20)
        self.__aim += self.__reaction + random.randrange(-20, 20)
    #For Debug
    def printstat(self):
        print ("Sex : ", self.__sex)
        print("Age : ", self.__age)
        print("Ethnicity", self.__ethnicity)
        print("Mobility", self.__mobility)
        print("Inteligence : ", self.__inteligence)
        print("Focus" , self.__focus)
        print("Reaction", self.__reaction)
        print("Melee", self.__melee)
        print("Aim", self.__aim)
        print("----------------------------")
"""
class Tribe(object):
    def __init__(self, ethnicity):
        self.__tribe_name = ethnicity
        self.__tribesmen=[]
        self.__elders=[]
        self.__children=[]
        self.__iscomplete = False
    def generate(self):
        abnormals_max = ethnicity[self.__tribe_name]
        max_tribesmen = ethnicity[self.__tribe_name] * 10
        current_abnormals = 0
        if current_abnormals < abnormals_max and random.randrange(0, 100) < ethnicity[self.__tribe_name]:
            name_selector = random.randrange[]
"""
#--------------------------Debug Section------------------------------------------------
if __name__ == "__main__":
    for i in range(0, 100):
        random_sex = random.randrange(0, 2)
        if random_sex == 0:
            person = Person('A-reh', 'Male', random.randrange(0, 80))
        else:
            person = Person('A-reh', 'Female', random.randrange(0, 80))

        person.statcalc()
        person.printstat()
        print (names_list)