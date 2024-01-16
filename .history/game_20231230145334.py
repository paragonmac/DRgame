import threading
import queue
import time
import sys
from room import clsRoom
from goblin import clsGoblin
from player import clsPlayer


class clsGame:
    RoomID = 0
    thread_game_output = None
    thread_player_input = None
    monster_list = []
    last_command = []
    last_command_index = None
    main_game_loop_bool = True

    command_lookup = {
        "help": help,
        "quit": quit,
        "spawn": clsGoblin.spawn_goblin,
        "target": clsPlayer.target,
        "assess": clsPlayer.assess,
        "attack": clsPlayer.attack,

    }
    arg_lookup = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
    }

    """
    A window for a simple game that takes user input and displays game output.
    """
    def __init__(self):
        self.game_output_queue = queue.Queue()

        self.command_lookup["help"] = self.help
        self.command_lookup["quit"] = self.quit
        self.command_lookup["spawn"] = self.go_spawn_goblin
        self.command_lookup["target"] = self.go_target
        self.command_lookup["assess"] = self.go_assess
        self.command_lookup["attack"] = self.go_attack


        # if the index is out of range then return the last index and start over from the beginning
        if len(clsGame.last_command) == 0:
            return
        if clsGame.last_command_index is None:
            clsGame.last_command_index = len(clsGame.last_command)
        clsGame.last_command_index += 1
        if clsGame.last_command_index > len(clsGame.last_command) - 1:
            clsGame.last_command_index = 0
        self.playerinput_var.set(clsGame.last_command[clsGame.last_command_index])


    def go_attack(self, *args):
        player_target = objPlayer.attack_target
        if player_target is None:
            return self.game_output_queue.put("You have no target")
        if len(clsGame.monster_list) == 0:
            return self.game_output_queue.put("There are no creatures to attack")
        result = objPlayer.attack(player_target, clsGame.monster_list)
        message, objPlayer.attack_target, clsGame.monster_list = result
        self.game_output_queue.put(message)

    def go_target(self, *args):
        if len(clsGame.monster_list) == 0:
            return self.game_output_queue.put("There are no creatures to target")
        result = objPlayer.target(clsGame.monster_list, g_arg1)
        return self.game_output_queue.put(result)

    def go_spawn_goblin(self, *args):
        if len(clsGame.monster_list) >= 6:
            return print("Maximum number of goblins reached")
        result = clsGoblin.spawn_goblin()
        print(result)  # debug
        clsGame.monster_list.append(result)
        self.game_output_queue.put((f"{result.name} has spawned"))

    def go_assess(self, *args):
        if len(clsGame.monster_list) == 0:
            return self.game_output_queue.put("There are no creatures to assess")

        result = clsPlayer.assess(clsGame.monster_list)
        print(f"go_assess{result}")  # debug
        self.game_output_queue.put(result)
        return print(result)

    def check_game_output_queue(self, event=None):
        try:
            msg = self.game_output_queue.get(0)  # try to get message from queue
            if msg is None:  # if there is no message in the queue
                return  # return without doing anything
            self.roomwindow.config(state='normal')
            self.roomwindow.insert('end', msg + '\n')
            self.roomwindow.see('end')
            self.roomwindow.config(state='disabled')
        except queue.Empty:
            pass
        finally:
            self.root.after(150, self.check_game_output_queue)

    def on_enter(self, event=None):
        print("ENTER PRESSED")
        # get user input and format it and send to game window
        User_input = self.playerinput_var.get()
        clsGame.last_command_index = 0
        clsGame.last_command.append(User_input)
        append_user_input = f">>> {User_input}"
        self.playerinput_var.set('')
        self.game_output_queue.put(append_user_input)
        # send user input to be processed for action
        self.input_start(User_input)

    def input_start(self, input):
        print(input)
        User_input = input
        if User_input:
            command, *args = User_input.split()
            self.process_command(command, args)

    def process_command(self, command, args):
        global g_arg1, g_arg2, g_arg3
        g_arg1, g_arg2, g_arg3 = None, None, None
        print(command, args)
        if args:
            # goes through the list of args and assigns them to g_arg1, g_arg2,g_arg3
            g_arg1, *rest = args
            if len(rest) >= 2:
                g_arg2, g_arg3 = rest[:2]
            elif len(rest) == 1:
                g_arg2 = rest[0]
                g_arg3 = None
            else:
                g_arg2, g_arg3 = None, None
        command_function = self.command_lookup.get(command)
        if command_function:
            print(g_arg1, g_arg2, g_arg3)
            command_function(command)
        else:
            self.game_output_queue.put("Unknown command: {}".format(command))

    def help(self, *args):
        self.game_output_queue.put("Commands: swing, quit, spawn, target,"
                                   " assess, help")

    def quit(self, *args):
        print("QUITTING GAME")
        self.root.destroy()
        self.main_game_loop_bool = False
        thread_game_output.join()
        thread_gameLogicWorker.join()
        
        sys.exit()

    def main_game_loop(self, event=None):
        print("Main game loop started")
        while self.main_game_loop_bool is True:
            if len(clsGame.monster_list) != 0 and objPlayer.health > 0:
                for monster in clsGame.monster_list: # this is where the goblin take its turn
                    attack_result, roam_results = clsGoblin.behaviors(monster, objPlayer)
                    if attack_result:
                        self.game_output_queue.put(attack_result)
                    if roam_results:
                        self.game_output_queue.put(roam_results)
            clsGame.room_update()
            time.sleep(1)  # simulate long running task

    def start_game(self, *args):
        print("GAME STARTED")
        self.game_output_queue.put("GAME STARTED")
        self.game_output_queue.put("You are in a room with a goblin")
        self.game_output_queue.put("What do you do?")

    def run(self):
        global thread_game_output, thread_gameLogicWorker
        thread_game_output = threading.Thread(target=self.check_game_output_queue)
        thread_game_output.setDaemon = True

        thread_gameLogicWorker = threading.Thread(target=self.main_game_loop)
        thread_gameLogicWorker.setDaemon = True
        
        thread_gameLogicWorker.start()
        thread_game_output.start()



if __name__ == "__main__":
    objPlayer = clsPlayer("Default_Player_Name", 100, "knife", 100, None)
    objGame = clsGame()
    objGame.run()
