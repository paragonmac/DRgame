import random
import time

class clsGoblin:
    def __init__(self, name, health, damage):
        loot_table = {'Gold': 0.5, 'Sword': 0.2, 'Shield': 0.1, 'Potion': 0.2}
        self.name = name
        self.roaming_cooldown = 0
        self.incombat = 0
        self.health = health
        self.damage = damage
        self.loot_table = loot_table
        self.goblin_swing_timer = 0
        self.tribe = []

    def spawn_goblin(self):
        if len(self.tribe) < 6:
            goblin_names = ["Gobbi", "Gobby", "Goblo", "Gobba", "Gobber", "Gobbie", "Gobbo", "Gobbu", "Gobble", "Gobblin", "Goblet", "Goblin", "Goblu", "Goblyn", "Gobboz", "Gobbler", "Gobz", "Gobster", "Goblee", "Gobskull"]
            name = random.choice(goblin_names)
            health = random.randint(80, 120)
            damage = random.randint(8, 12)
            objGoblin = clsGoblin(name, health, damage)
            self.tribe.goblins.append(objGoblin)
            return print(f"{objGoblin.name} has spawned")
        else:
            print("Maximum number of goblins reached")
    '''        
    #adds behaviors to the goblin like roaming from place to place and attacking the player when they get close enough
    def behaviors(self):
        if self.roaming_cooldown == 0 and self.incombat == 0:
            self.roam()

    def roam(self):
        print(f"{self.name} is roaming")
    '''
    # Removes the goblin object
    def despawn_goblin(self):
        del self
        
    def loot(self):
        ...
        
    def attack(self, player):
        if self.goblin_swing_timer <= 0:
            attack_damage = random.randint(1, self.damage)  # Generate random attack damage
            player.health -= attack_damage
            self.goblin_swing_timer = 1
            print(f"{self.name} attacked {player.name} for {attack_damage} damage")
            return player.health
        else:
            self.goblin_swing_timer -= 1
            return player.health