import random

class Character:
    def __init__(self, name="", hitPoints=0, hitChance=0, maxDamage=0, armor=0):
        self.name = name
        self.hitPoints = hitPoints
        self.hitChance = hitChance
        self.maxDamage = maxDamage
        self.armor = armor

    def printStats(self):
        print(f"{self.name}: {self.hitPoints} HP")

    def isAlive(self):
        return self.hitPoints > 0

    def attack(self, defender):
        if random.randint(1, 100) <= self.hitChance:
            damage = random.randint(1, self.maxDamage)
            print(f"{self.name} hits {defender.name}...")
            print(f"  for {damage} points of damage")
            absorbed = min(damage, defender.armor)
            print(f"  {defender.name}'s armor can absorb {absorbed} points")
            actual_damage = damage - absorbed
            defender.hitPoints -= actual_damage
        else:
            print(f"{self.name} misses!")

def showStartingStats(self):
    print(f"{self.name}")
    print("==================")
    print(f" Hit points: {self.hitPoints}")
    print(f" Hit chance: {self.hitChance}")
    print(f" Max damage: {self.maxDamage}")
    print(f" Armor:      {self.armor}\n")

def fight(c1, c2):
    turn = 0
    while c1.isAlive() and c2.isAlive():
        input("\npress enter for another round: ")

        if turn % 2 == 0:
            c1.attack(c2)
        else:
            c2.attack(c1)

        c1.printStats()
        c2.printStats()

        turn += 1

    print()
    if c1.isAlive():
        print(f"{c1.name} wins!")
    else:
        print(f"{c2.name} wins!")