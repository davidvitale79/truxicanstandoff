from fclass import Hero,Enemy
from weapons import *

enemy = Enemy
chance = None

weapon_by_type = None

def cal_hit_chance(a_accuracy, d_evasion):
    hit_chance = a_accuracy - d_evasion
    if hit_chance < 0:
        hit_chance = 0
    elif hit_chance > 100:
        hit_chance = 100
    return hit_chance

a_accuracy = 80
d_evasion = 20
hit_chance = cal_hit_chance(a_accuracy, d_evasion)

def is_hit(hit_chance):
    roll = random.randint(1, 100)
    return roll <= hit_chance


hero = Hero(name="Hero", health=100, weapon=random_weapon1, target=enemy.target)
hero.equip(random_weapon1)
random_weapon1.display_attributes()
input("Press enter to continue...\n")

enemy = Enemy(name="Enemy", health=100, weapon=random_weapon2, target=hero.target)
enemy.equip(random_weapon2)
random_weapon2.display_attributes()
input("Press enter to continue...\n")

print([weapon_by_type])

while True:
    if is_hit(hit_chance):
        hero.attack(enemy, random_weapon1)
        input("Press enter to continue...\n")
    else:
        hero.crit(enemy, random_weapon1)
        input("Press enter to continue...\n")

    if is_hit(hit_chance):
        enemy.attack(hero, random_weapon2)
        input("Press enter to continue...\n")
    else:
        enemy.crit(hero, random_weapon2)
        input("Press enter to continue...\n")

    if enemy.health <= 0:
        print(f"{enemy.name} has been defeated by {hero.name}!")
        break

    if hero.health <= 0:
        print(f"{hero.name} has been defeated by {enemy.name}!")
        break


    print(f"Health of {hero.name}: {hero.health}")

    print(f"Health of {enemy.name}: {enemy.health}")
    input("Press enter to continue...\n")

    if input('Choose an action: ') == 'drop':
        hero.drop(hero.weapon)