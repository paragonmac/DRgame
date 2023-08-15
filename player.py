import random
import time


class clsPlayer:
    def __init__(self, name="Default_Player_Name", health=100,
                 w_equipped="knife", damage=50,  inventory=None):
        self.name = name
        self.health = health
        self.damage = 50
        self.w_equipped = w_equipped
        self.inventory = inventory or []
        self.attackspeed = 3
        self.roundtime = 0
        self.attack_target = 0

    def target(self, monster_list, arg1):
        if type(arg1) is not int:
            self.attack_target = int(arg1)
        else:
            self.attack_target = arg1

        # Check if the attack_target is within the valid range of 1 through 6
        if self.attack_target < 1 or self.attack_target > len(monster_list):
            return f"{self.attack_target} is an invalid target"

        # Subtracting 1 to convert from 1-based to 0-based indexing
        target_index = self.attack_target - 1

        # Check and see if the target index exists in monster_list
        if target_index in range(len(monster_list)):
            self.attack_target = target_index
            return f"Your target is now {monster_list[target_index].name}"
        elif len(monster_list) == 0:
            return "There are no monsters to target"

    def attack(self, target_monster, monster_list):
        local_target_monster = target_monster
        local_monster_list = monster_list
        local_monster_object = local_monster_list[local_target_monster]
        message = ""
        current_time = 0
        if local_target_monster is not None and 0 <= local_target_monster < len(local_monster_list):
            current_time = time.time()
            if current_time > self.roundtime:  # 5 seconds have pass
                # put attack hit or miss here
                self.roundtime = time.time() + self.attackspeed
                local_monster_object.health -= self.damage + random.randint(-10, 10)
                if local_monster_object.health <= 0:
                    # drop loot here
                    local_monster_list.pop(local_target_monster)
                    message = f"You killed {local_monster_object.name} " \
                        f"dealing {self.damage}. Roundtime: {(self.roundtime - current_time):.2f}"
                    local_target_monster = None
                else:
                    message = f"You hit {local_monster_object.name} " \
                        f"dealing {self.damage} damage. Roundtime: {self.roundtime - current_time:.2f}"
            else:
                message = "You must wait " \
                    f"{(self.roundtime - current_time):.2f} seconds before attacking again."
        else:
            message = "You have no target, please use Target command"
            local_target_monster = 0
        return message, local_target_monster, local_monster_list

    def assess(monster_list):
        monster_breakout = []
        for i, monster in enumerate(monster_list):
            monster_info = f"#{i+1}: {monster.name} has {monster.health} health remaining"
            monster_breakout.append(monster_info)
        return '\n'.join(monster_breakout)

    def death(self):

        # resets player stats and wipes inventory
        self.health = 100
        # world reset function here
        return f"{self.name} has died"
