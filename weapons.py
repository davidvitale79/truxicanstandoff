from typing import Dict
import random

class Weapon:
    def __init__(self, name: str, weapon_type: str, damage: int,
                 crit: int, value: int) -> None:
        self.name = name
        self.weapon_type = weapon_type
        self.damage = damage
        self.crit = crit
        self.value = value

    def display_attributes(self):
        print(f"Weapon Name: {self.name}")
        print(f"Damage: {self.damage}")
        print(f"Weapon_type: {self.weapon_type}")
        print(f"Crit: {self.crit}")
        print(f"Value: {self.value}")

    def separate_weapons_by_type(weapons):
        weapons_by_type = {}

        for weapon in weapons_types:
            weapon_type = weapon["weapon_type"]
            if weapon_type not in weapons_by_type:
                weapons_by_type[weapon_type] = []
            weapons_by_type[weapon_type].append(weapon["name"])
        return weapons_by_type

class WeaponFactory:
    def __init__(self, weapon_factory=None) -> None:
        self.weapon_factory = weapon_factory

    def __str__(self):
        return f"Weapon(name={self.name}, damage={self.damage})"

    def create_weapon(self, weapons: Dict[str,any]) -> Weapon:
        required_keys = {'name', 'weapon_type', 'damage', 'crit', 'value'}
        if not required_keys.issubset(weapons.keys()):
            raise ValueError(f"Missing keys in random_value. Required keys: {required_keys}")
        return Weapon(
            name=weapons['name'],
            weapon_type=weapons['weapon_type'],
            damage=weapons['damage'],
            crit=weapons['crit'],
            value=weapons['value']
        )

weapons = [
    {"name": "Long Bow", "weapon_type": "Ranged", "damage": 10, "crit": 6, "value": 8},
    {"name": "Diamond Lance", "weapon_type": "Ranged", "damage": 8, "crit": 3, "value": 15},
    {"name": "Diamond Sword", "weapon_type": "Sharp", "damage": 7, "crit": 12, "value": 15},
    {"name": "Golden Hammer", "weapon_type": "Blunt", "damage": 10, "crit": 2, "value": 5},
    {"name": "Two Handed Sword", "weapon_type": "Sharp", "damage": 3, "crit": 12, "value": 5},
    {"name": "Golden Axe", "weapon_type": "Sharp", "damage": 5, "crit": 7, "value": 15},
    {"name": "Master Sword", "weapon_type": "Sharp", "damage": 7, "crit": 5, "value": 8},
    {"name": "Mace", "weapon_type": "Blunt", "damage": 5, "crit": 7, "value": 7},
    {"name": "Two Handed Sword", "weapon_type": "Sharp", "damage": 3, "crit": 12, "value": 8},
    {"name": "Halberd", "weapon_type": "Ranged", "damage": 3, "crit": 4, "value": 6},
    {"name": "Hammer", "weapon_type": "Blunt", "damage": 5, "crit": 5, "value": 5},
    {"name": "Cross Bow", "weapon_type": "Ranged", "damage": 7, "crit": 4, "value": 12},
    {"name": "Axe", "weapon_type": "Sharp", "damage": 9, "crit": 2, "value": 10},
    {"name": "Bone Sword", "weapon_type": "Sharp", "damage": 4, "crit": 6, "value": 6},
    {"name": "Dagger", "weapon_type": "Sharp", "damage": 3, "crit": 4, "value": 4},
    {"name": "Iron Sword", "weapon_type": "Sharp", "damage": 5, "crit": 7, "value": 10},
    {"name": "Short Bow", "weapon_type": "Ranged", "damage": 4, "crit": 6, "value": 7},
    {"name": "Brass Knuckles", "weapon_type": "Blunt", "damage": 2, "crit": 5, "value": 0},
    {"name": "Silver Sword", "weapon_type": "Sharp", "damage": 6, "crit": 8, "value": 12},
    {"name": "War Hammer", "weapon_type": "Blunt", "damage": 10, "crit": 6, "value": 8}
]


random_weapon1 = {
    "name": random.choice([weapon["name"] for weapon in weapons]),
    "weapon_type": random.choice([weapon_type["weapon_type"] for weapon_type in weapons]),
    "damage": random.choice([random_damage["damage"] for random_damage in weapons]),
    "crit": random.choice([random_crit["crit"] for random_crit in weapons]),
    "value": random.choice([random_value["value"] for random_value in weapons])
}

random_weapon2 = {
    "name": random.choice([weapon["name"] for weapon in weapons]),
    "weapon_type": random.choice([random_weapon_type["weapon_type"] for random_weapon_type in weapons]),
    "damage": random.choice([random_damage["damage"] for random_damage in weapons]),
    "crit": random.choice([random_crit["crit"] for random_crit in weapons]),
    "value": random.choice([random_value["value"] for random_value in weapons])
}

random_weapon3 = {
    "name": random.choice([weapon["name"] for weapon in weapons]),
    "weapon_type": random.choice([random_weapon_type["weapon_type"] for random_weapon_type in weapons]),
    "damage": random.choice([random_damage["damage"] for random_damage in weapons]),
    "crit": random.choice([random_crit["crit"] for random_crit in weapons]),
    "value": random.choice([random_value["value"] for random_value in weapons])
}


weapon_factory = WeaponFactory()
random_weapon1 = weapon_factory.create_weapon(random_weapon1)
random_weapon2 = weapon_factory.create_weapon(random_weapon2)
random_weapon3 = weapon_factory.create_weapon(random_weapon3)

long_bow = Weapon(name='Long Bow', weapon_type='Ranged', damage=10, crit=6, value=8)
diamond_lance = Weapon(name='Diamond Lance', weapon_type='Ranged', damage=8, crit=3, value=15)
diamond_sword = Weapon(name='Diamond Sword', weapon_type='Sharp', damage=7, crit=12, value=15)
golden_hammer = Weapon(name='Golden_hammer', weapon_type='Blunt', damage=10, crit=2, value=5)
golden_sword = Weapon(name='Golden Sword', weapon_type='Sharp', damage=3, crit=12, value=5)
golden_axe = Weapon(name='Golden Axe', weapon_type='Sharp', damage=5, crit=7, value=15)
master_sword = Weapon(name='Master Sword', weapon_type='Sharp', damage=7, crit=5, value=8)
mace = Weapon(name='Mace', weapon_type='Blunt', damage=5, crit=7, value=7)
two_handed_sword = Weapon(name='Two Handed Sword', weapon_type='Sharp', damage=3, crit=12, value=8)
halberd = Weapon(name='Halberd', weapon_type='Ranged', damage=3, crit=4, value=6)
hammer = Weapon(name='Hammer', weapon_type='Blunt', damage=5, crit=5, value=5)
cross_bow = Weapon(name='Cross Bow', weapon_type='Ranged', damage=7, crit=4, value=12)
axe = Weapon(name='axe', weapon_type='Sharp', damage=9, crit=2, value=10)
bone_sword = Weapon(name='Bone Sword', weapon_type='Sharp', damage=4, crit=6, value=6)
dagger = Weapon(name='Dagger', weapon_type='Sharp', damage=3, crit=4, value=4)
iron_sword = Weapon(name='Iron Sword', weapon_type='Sharp', damage=5, crit=7, value=10)
short_bow = Weapon(name='Short Bow', weapon_type='Ranged', damage=4, crit=6, value=7)
brass_knuckles = Weapon(name='Brass Knuckles', weapon_type='Blunt', damage=2, crit=5, value=0)
silver_sword = Weapon(name='Silver Sword', weapon_type='Sharp', damage=6, crit=8, value=12)
war_hammer = Weapon(name='War Hammer', weapon_type='Blunt', damage=10, crit=6, value=8)
