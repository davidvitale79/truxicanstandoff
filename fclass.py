class Character:
    def __init__(self, target: str, name: str,
                 health: int, weapon: str, inventory = None)-> None:
        self.target = target
        self.name = name
        self.health = health
        self.health_max = health
        self.weapon = weapon
        self.inventory = inventory if inventory is not None else []

    def attack(self, target, weapon) -> None:
        self.target = target
        self.weapon = weapon
        target.health -= weapon.damage
        target.health = max(target.health, 0)
        print(f"*{self.name}*".center(20))
        print(f"-{weapon.name}-".center(20))
        print(f"DEALT {weapon.damage} DAMAGE TO {target.name} WITH {weapon.name}!\n".center(20))

    def crit(self, target, weapon) -> None:
        self.target = target
        self.weapon = weapon
        crit_damage = weapon.crit
        total_damage = crit_damage + weapon.damage
        target.health = max(target.health, 0)
        target.health -= total_damage

        text = (f"*{self.name}*".center(20))
        ctext = "CRITICAL HIT!".center(20, "*")
        ctxt = (f"*{weapon.name}*".center(20))
        ctext1 = (f"** {crit_damage} **".center(20,"*"))
        ctext2 = (f"** BASE DAMAGE {weapon.damage} **".center(20))
        ctext3 = (f"** FOR A TOTAL OF {total_damage} **".center(20))
        print(f"{text}\n{ctext}\n{ctxt}\n{ctext1}\n{ctext2}\n{ctext3}\n")

    def equip(self, weapon) -> None:
        self.weapon = weapon
        print(f"*{self.name}* equipped a(n) -{self.weapon.name}-!")


    def drop(self, weapon)-> None:
        self.weapon = weapon
        print(f"*{self.name}* has dropped the -{weapon.name}-!")


class Hero(Character):
    def __init__(self, target: str, name: str, health: int, weapon: str) -> None:
        super().__init__(name = name, health = health,
                         target = target,  weapon = weapon, inventory = str(None))
        self.target = target
        self.name = name
        self.health = health
        self.health_max = health
        self.weapon = weapon
        self.inventory_hero = []


class Enemy(Character):
    target = Hero
    def __init__(self, target: str, name: str, health: int, weapon: str) -> None:
        super().__init__(name = name, health = health,
                target = target, weapon = weapon, inventory = str(None))
        self.enemy = Enemy
        self.target = target
        self.name = name
        self.health = health
        self.health_max = health
        self.weapon = weapon
        self.inventory_enemy = []


class Ncp(Character):
    def __init__(self, target: str, name: str, health: int, weapon: str)-> None:
            super().__init__(name = name, health = health,
                             target = target, weapon = weapon, inventory = str(None))
            self.target = target
            self.name = name
            self.health = health
            self.health_max = health
            self.weapon = weapon
            self.inventory_npc = []