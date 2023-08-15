import random
import time


class clsGoblin:
    def __init__(self, name, health, damage):
        loot_table = {'Gold': 0.5, 'Sword': 0.2, 'Shield': 0.1, 'Potion': 0.2}
        self.name = name
        self.roaming_cooldown = 0
        self.incombat = 0
        self.health = health
        self.damage = 14
        self.loot_table = loot_table
        self.goblin_swing_timer = 0
        self.attack_speed = 4

    def spawn_goblin():
        goblin_names = ["Gobbi", "Gobby", "Goblo", "Gobba", "Gobber",
                        "Gobbie", "Gobbo", "Gobbu", "Gobble", "Gobblin",
                        "Goblet", "Goblin", "Goblu", "Goblyn", "Gobboz",
                        "Gobbler", "Gobz", "Gobster", "Goblee", "Gobskull"]
        name = random.choice(goblin_names)
        health = random.randint(80, 120)
        damage = random.randint(8, 12)
        objGoblin = clsGoblin(name, health, damage)
        return objGoblin

    # adds behaviors to the goblin like roaming from place to place and attacking the player when they get close enough
    def behaviors(self, player):
        if self.roaming_cooldown == 0 and self.incombat == 0:
            print("Goblin behaviors called")
            attack_result = self.attack(player)
            roam_result = self.roam()
            return attack_result, roam_result
        # If the conditions are not met, return None
        return None

    def roam(self):
        self.roaming_cooldown = time.time() + 5
        return (f"{self.name} is roaming")

    # Removes the goblin object
    def despawn_goblin(self):
        del self

    def loot(self):
        ...

    def attack(self, player):
        if self.goblin_swing_timer <= 0:
            self.goblin_swing_timer = time.time() + self.attack_speed
            attack_damage = random.randint(1, self.damage)  # Generate random attack damage
            player.health -= attack_damage  # Subtract attack damage from player health
            if player.health <= 0:
                player.death()
            other_result = (f"{self.name} attacked you for {attack_damage} damage!")
            return other_result
        else:
            debug_message = f"{self.name} is not ready to attack. Swing timer: {self.goblin_swing_timer}"
            print(debug_message)  # Print the debug message
