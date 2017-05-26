"""
"⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⡀⠀⢀⣀⠀⠀⠀⠀⠀⢀⡀
⠀⠀⠀⠀⠀⠀⣀⣀⡀⠀⠀⠀⢀⡠⠔⠒⠉⠁⠀⠀⠀⠀⠀⠀⠀⡇⢀⣠⣴⣾⠟⢱
⠀⠀⠀⠀⠀⡌⠈⠻⣿⣿⣦⣆⠁⠀⠀⠀⠀⠀⠀⠀⠀⢀⡀⠤⢤⣽⣿⣿⣟⠡⢤⡘
⠀⠀⠀⠀⢰⠠⣒⠉⠙⢿⣿⡿⠷⣀⣠⠴⢤⣀⠀⠀⠈⠁⡀⡴⠿⢿⣿⠋⠀⣔⠁⠇
⠀⢀⡠⠔⡎⠀⢠⣃⣠⠞⠁⠀⠀⠀⠀⠀⡄⠀⠉⠑⠒⡉⠈⠀⠀⠀⠈⠑⠶⡭⠼⡄
⢠⠃⠀⠀⠇⠀⢀⠞⠁⠀⢠⠀⢠⠚⠉⡹⢳⠀⠀⠀⠀⡷⡏⠉⠙⢢⡀⠀⠀⠘⢟⠁
⢸⠀⠀⠀⢸⢠⠃⠀⠀⠀⡎⠀⠀⠀⣼⣁⠘⡀⠀⠀⠀⡇⡈⢢⣀⡀⠁⠀⠀⠀⠈⢆
⡜⠀⠀⠀⢀⠇⠀⠀⠀⢸⠀⢀⡴⠋⢉⠉⠳⣵⡀⠀⠀⣯⠞⢉⡉⠹⣆⠀⠀⠀⠀⠘⡆
⠈⠐⡎⠑⠟⠀⠀⠀⠀⡏⠀⡊⠀⠀⠀⣵⡀⠉⠑⣄⠀⠃⠀⠀⢈⣦⠹⡀⠀⢰⢦⡀⡇
⠀⢰⠀⠀⡀⠀⠀⠀⠀⡇⢠⣧⣤⣤⣾⣿⣷⠀⠀⠀⠁⣦⣤⣴⣾⣿⡆⡇⠀⢸⠀⠙⠇
⠀⢸⣦⣀⡇⠀⠀⠀⠀⡇⢸⣿⣿⣿⣿⡿⣿⠀⠀⠀⠀⣿⣿⣿⣿⣿⡇⡇⠀⢸
⠀⢸⣿⣿⣧⠀⠀⠀⠀⡇⠈⠳⠈⠛⠋⠐⠃⠀⠀⠀⠤⠛⠈⠛⠉⠜⠀⢇⡀⡼
⠀⠀⢿⣿⣿⣆⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀⢆⣀⠤⣀⡠⠀⠀⠀⠀⠀⠀⢀⣵⠃
⠀⠀⠈⠻⣿⠿⢷⣄⠀⠀⢧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡀⢀⣠⠔⣫⠃
⠀⠀⠀⠀⠀⠀⠀⠀⣱⣦⣈⡻⡛⠒⢴⠉⠉⠑⢤⠤⡖⠊⢁⡿⠟⣏⡴⠁
⠀⠀⠀⠀⠀⠀⠀⣴⣿⣿⡿⠈⠉⠀⠘⡄⠀⠀⢠⣠⠁⢀⠎
⠀⠀⠀⠀⠀⢀⣾⣿⣿⣿⠃⠀⠀⠀⠀⣷⣠⣶⣿⠗⠔⠋
⠀⠀⠀⠀⠀⠘⠛⠛⠛⠃⠀⠀⠀⠀⠀⠛⠛⠛⠃﻿
"""
#-------------------------------------------------------------------------#

#Stats----------------------------------------------------------------------

#---------------------------------------------------------------------------
import random

class Person(object):
    def __init__(self, name, idnum, melee = 100, ranged = 100, strength = 100):
        self.name = name
        self.idnum = idnum
        self.health = ['normal', 'injured', 'dead']
        self.strength = strength
        self.melee = melee
        self.ranged = ranged
        self.has_task = False
        self.task = None
    def __str__(self):
        return ("My name is {}".format(self.name))
    def allocate_task(self):
        print("{} : What should i do?".format(self.name) )
        print("0.Select another character 1.Hunt 2.No task")
        task_selection = input(">>")
        if task_selection == '0':
            return None
        elif task_selection == '1':
            self.task = 'Hunt'
            print('{} : Hunt'.format(self.name))
    def hunt(self, stats):
        pass



class Group(object):
    def __init__(self, name, food = 100, men = 20, weapons = 40):
        self.food = food
        self.men = men
        self.name = name
        self.weapons = weapons
        self.relationship = 100
    def endturn(self):
        self.food -= self.men
        if self.weapons < self.men * 4:
            self.weapons += self.men * 2
        if self.food < int(self.men/2):
            return False
        elif self.men < 3:
            return False
        elif self.food < self.men * 7:
            self.hunt()
        else:
            return True
    def stat(self):
        if self.endturn() == False:
            print("{} is extinct. ".format(self.name))
        else:
            print(self.name)
            print("Food = {}".format(self.food))
            print("Men = {}".format(self.men))
            print("Weapon = {}".format(self.weapons))
    def hunt(self):
        weapon_usage_max = 10
        weapon_usage_min = 5

        if self.weapons < weapon_usage_min:
            weapon_usage_max = self.weapons
            weapon_usage_min = 0

        luck = 2

        weapon_usage = int(random.randrange(weapon_usage_min, weapon_usage_max) * (self.men * 2 / 10))
        food_gain = random.randrange(int(weapon_usage/luck), weapon_usage)

        self.weapons -= weapon_usage
        self.food += food_gain
        if self.weapons <= 0:
            self.weapons = 0

class Torch(Group):
    def __init__(self, members, food = 100, men = 20, weapons = 0, ammo = 10, name = "Torch"):
        super().__init__(name, food, men, weapons)
        self.ammo =  ammo
        self.name = name
        self.members = members


sang = Group(name = 'Sang', food = 400, men = 20, weapons = 40)
gah_un_deh = Group(name = "Gah_un-deg", food = 200, men = 40, weapons = 40)

jaguar = Person(idnum = 1, name = 'Jaguar')
hugh = Person(idnum = 2, name = 'Hugh')
nika = Person(idnum = 3, name = 'Nika')
harry = Person(idnum = 4, name = 'Harry')
torch_list = [jaguar, hugh, nika, harry]

torch = Torch(food=80, men=5, weapons = 0, ammo = 10, members =  torch_list)

group_list = [sang, torch]


class Turn():
    def __init__(self, groups_list, torch_list):
        self.groups_list = groups_list
        self.torch_list = torch_list
        self.tasks = ['Hunt']
        self.Hunt = []

    def turn(self, turn_no):
        print("Turn #{}".format(turn_no))
        for group in self.groups_list:
            group.stat()
        quit = self.task(self.groups_list, self.torch_list)
        if quit:
            return False
        else:
            for group in self.groups_list:
                group.endturn()
            return True

    def task(self, groups_list, torch_list):
        done = False
        #Basic empty task list
        hunting = []
        investigate = ''
        Gift = ''
        Attack = []

        #Ask tsk loop. Return True to end the loop, Return False to end the loop and quit the game entirely
        while not done:
            print("Allocate tasks to each members, Input 'c' to check everyone's task. Input 'd' if you are done. The members with no task will take a break.")
            for member in torch_list:
                print("{}.{}".format(member.idnum, member.name))
            print("d.Done")
            print("q.Quit")
            selection = input(">>")
            print("1.Hunting 2.Investigate 3.Gift 4.Attack")

            if selection == 'q' or selection == 'Q':
                #Quit the game entirely
                return True
            elif selection == 'd' or selection == 'D':
                done = True
            elif selection == 'c' or selection == 'C':
                print("Task Check")
                for member in hunting:
                    print('Hunting : {}'.format(member))
            else:
                index = int(selection) - 1
                    print ("{} : What should I do?".format(torch_list[index].name))
                    task_selection = input(">>")
                    #if int(task_selection) == range(1, 5):
                    torch_list[index].has_task = True
                    hunting.append(torch_list[index])

        #Quit just this loop
        return True

    # def hunt(self, task, group, members = None):
    #     weapon_usage_max = 10
    #     weapon_usage_min = 5
    #     ammo_usage_max = 5
    #     ammo_usage_min = 3
    #     if group.name == 'Torch':
    #         d
    #     else:
    #         weapon_usage_max = int(weapon_usage_max * group.weapon_usage_max_adjust)
    #         weapon_usage_min = int(weapon_usage_min * group.weapon_usage_min_adjust)
    #     food_gain_min = weapon_usage_min + random.randrange(-1 , 2)
    #     food_gain_max = weapon_usage_max + random.randrange(-2, 3)


def intro():
    print("Aboriginal Faith Prototype")
    print("Beginning 2017-05-15")

def menu():
    done = True
    while done:
        print("1.Start New Game")
        print("2.Quit")
        selection = input()
        if selection == '2':
            quit()
        elif selection == '1':
            return 'Start New Game'

def main():
    #Run every time
    intro()
    menu()

    turn_no = 1
    turn = Turn(group_list, torch_list)
    while turn.turn(turn_no):
        turn_no += 1

if __name__ == "__main__":
    main()
