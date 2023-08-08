import random
import time




class clsPlayer:
    def __init__(self, name="Default_Player_Name", health=100, w_equipped="knife", damage=100,  inventory=None):
        self.name = name
        self.health = health
        self.damage = damage
        self.w_equipped = w_equipped
        self.inventory = inventory or []
        self.attackspeed = 3
        self.roundtime = 0
        self.attack_target = 0


    def target(self, target_monster, monster_list):
        #assert self.attack_target is not None
        self.attack_target = target_monster.arg1
        self.monster_list = monster_list
        if self.attack_target is not None and 0 <= self.attack_target < len(monster_list):
            print(f"Your target is now {target_monster[self.attack_target].name}")
            return self.attack_target
        elif len(monster_list) == 0:
            print("There are no goblins to target")
            return self.attack_target
        else:
            print("Invalid target")
        return self.attack_target

    def attack(self, target_monster, monster_list):
        #assert self.attack_target is not None
        if len(monster_list) == 0:
            print("There are no monsters to attack")
            return
        else:
            current_time = time.time()
            if current_time - self.last_attack_time >= self.attackspeed:  # 5 seconds have passed since the last attack
                attack_damage = random.randint(1, self.damage)  # Generate random attack damage
                target_monster[self.attack_target].health -= attack_damage
                self.last_attack_time = current_time
                print(f"{self.name} attacked {target_monster[self.attack_target].name} for {attack_damage} damage")
                #kill the monster when its health reaches 0
                if target_monster[self.attack_target].health <= 0:
                    print(f"{target_monster[self.attack_target].name} has been slain")
                    target_monster[self.attack_target].loot()
            else:
                remaining_time = self.attackspeed - (current_time - self.last_attack_time)
                print(f"You are on cooldown. You can attack in {remaining_time:.2f} seconds.")
                
    def assess(self, monster_list):
        if len(monster_list) == 0:
            print("There are no monsters in this area")
            return 
        else:
            for monster in monster_list:
                print(f"{monster.name} has {monster.health} health remaining")
