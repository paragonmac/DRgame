import random
import time
import goblin
from goblin import Goblin




class Player:
    def __init__(self, name="Default_Player_Name", health=100, w_equipped="knife", damage=100,  inventory=None):
        self.name = name
        self.health = health
        self.damage = damage
        self.w_equipped = w_equipped
        self.inventory = inventory or []
        self.attackspeed = 3
        self.last_attack_time = 0
        self.attack_target = 0


    def target(self):
        #assert self.attack_target is not None
        self.attack_target = arg_lookup.get(arg1)
        if self.attack_target is not None and 0 <= self.attack_target < len(Goblin.goblins):
            print(f"Your target is now {Goblin.goblins[self.attack_target].name}")
            return self.attack_target
        elif len(Goblin.goblins) == 0:
            print("There are no goblins to target")
            return self.attack_target
        else:
            print("Invalid target")
        return self.attack_target
    
  
    def attack(self):
        #assert self.attack_target is not None
        if len(Goblin.goblins) == 0:
            print("There are no goblins to attack")
            return
        else:
            current_time = time.time()
            if current_time - self.last_attack_time >= self.attackspeed:  # 5 seconds have passed since the last attack
                attack_damage = random.randint(1, self.damage)  # Generate random attack damage
                Goblin.goblins[self.attack_target].health -= attack_damage
                self.last_attack_time = current_time
                print(f"{self.name} attacked {Goblin.goblins[self.attack_target].name} for {attack_damage} damage")
                #kill the goblin when it's health reaches 0
                if Goblin.goblins[self.attack_target].health <= 0:
                    print(f"{Goblin.goblins[self.attack_target].name} has been slain")
                    Goblin.goblins[self.attack_target].kill_loot_goblin()
            else:
                remaining_time = self.attackspeed - (current_time - self.last_attack_time)
                print(f"You are on cooldown. You can attack in {remaining_time:.2f} seconds.")
                
    def assess(self):
        if len(Goblin.goblins) == 0:
            print("There are no goblins in this area")
            return 
        else:
            for goblin in Goblin.goblins:
                print(f"{goblin.name} has {goblin.health} health remaining")