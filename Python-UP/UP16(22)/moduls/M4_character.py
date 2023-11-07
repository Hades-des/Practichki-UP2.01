class Character:
    def __init__(self, name, level, health):
        self.name = name
        self.level = level
        self.health = health
        self.attack_power = 10
        self.defense = 5
        self.abilities = {}

    def set_health(self, health):
        self.health = health

    def get_health(self):
        return self.health

    def set_attack_power(self, attack_power):
        self.attack_power = attack_power

    def get_attack_power(self):
        return self.attack_power

    def set_defense(self, defense):
        self.defense = defense

    def get_defense(self):
        return self.defense

    def attack(self, enemy):
        damage = self.attack_power - enemy.get_defense()
        if damage > 0:
            enemy.set_health(enemy.get_health() - damage)

    def defend(self):
        self.defense += 3

    def use_ability(self, ability_name):
        if ability_name in self.abilities:
            print(f"{self.name} использует способность: {ability_name}")
        else:
            print(f"{self.name} не имеет способности с именем {ability_name}")