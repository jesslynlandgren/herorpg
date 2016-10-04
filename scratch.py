class Character(object):
    def __init__(self):
        self.name = ""
        self.health = 0
        self.power = 0

    def print_status(self):
        print "The {0} has {1} health and {2} power.".format(self.name, self.health, self.power)

    def alive(self):
        return self.health >0

    def attack(self, other):
        if other.name != "zombie":
            other.health -= self.power
            print "The {0} does {1} damage to the {2}".format(self.name, self.power, other.name)
        else:
            print "Zombies are invincible!!"
        if other.health <= 0:
            print "The {0} is dead.".format(other.name)

class Hero(Character):
    def __init__(self):
        self.name = "hero"
        self.health = 10
        self.power = 5

class Goblin(Character):
    def __init__(self):
        self.name = "goblin"
        self.health = 6
        self.power = 2


class Zombie(Character):
    def __init__(self):
        self.name = "zombie"
        self.health = "INVINCIBLE!!"
        self.power = 3


h = Hero()
g = Goblin()


def printCharacterList():
    characters =   {'hero': {'health': 10, 'damage': 5}, "20'%' chance of dealing double damage per turn"}
                    'goblin': {'health': 10, 'damage': 5}, ""}
                    'zombie': {'health': 'INVINCIBLE!!', 'damage': 5, "can't die"}
                    'medic'
                    }
    for c in characters:


def playGame():
    print "Available characters:\n"





    print "1. Hero - Dam20% pobablility of double damage"
    print "2. Goblin"
    print "3. Zombie (cannot die)"
    print "4 "
    char1 = raw_input('Chooose the first character')

while h.alive() > 0 and g.alive() > 0:
    h.print_status()
    g.print_status()
    print
    print "What do you want to do?"
    print "1. fight goblin"
    print "2. do nothing"
    print "3. flee"
    print "> ",
    input = raw_input()
    if input == "1":
        h.attack(g)
    elif input == "2":
        pass
    elif input == "3":
        print "Goodbye."
        break
    else:
        print "Invalid input %r" % input

    if g.alive() > 0:
        g.attack(h)
