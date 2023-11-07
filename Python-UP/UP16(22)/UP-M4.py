from moduls.M4_character import Character

hero = Character("Герой", 2, 200)
enemy = Character("Враг", 3, 160)
print(f"{hero.name}: Уровень {hero.level}, Здоровье {hero.health}")
print(f"{enemy.name}: Уровень {enemy.level}, Здоровье {enemy.health}")
hero.attack(enemy)
print(f"{hero.name} атакует {enemy.name}. Здоровье {enemy.name}: {enemy.health}")
enemy.defend()
print(f"{enemy.name} защищается. Защита {enemy.name}: {enemy.get_defense()}")
hero.use_ability("Притвориться мертвым")
print(f"{hero.name}: Уровень {hero.level}, Здоровье {hero.get_health()}")
print(f"{enemy.name}: Уровень {enemy.level}, Здоровье {enemy.get_health()}")
