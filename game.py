import tkinter as tk
import threading
import queue
import player
import goblin 
import time
import sys
import random


class Game:
    """
    A window for a simple game that takes user input and displays game output.
    """
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("1600x900")  # set screen size to 1600x900 pixels
        self.root.title("Game Window")

        self.game_output_queue = queue.Queue()

        self.scrollbar = tk.Scrollbar(self.root, troughcolor='black')
        self.scrollbar.pack(side='right', fill='y')
        self.gamewindow_text = tk.Text(self.root, height=1, font=('Arial', 20), yscrollcommand=self.scrollbar.set)
        self.gamewindow_text.config(bg='black', fg='white', highlightbackground='black')  # set background color to black and foreground color to white
        self.gamewindow_text.pack(fill='both', expand=True)  # make the text area take up the whole screen

        self.playerinput_var = tk.StringVar()
        self.playerinput_entry = tk.Entry(self.root, textvariable=self.playerinput_var, font=('Arial', 20))
        self.playerinput_entry.config(bg='black', fg='white')  # set background color to black and foreground color to white
        self.playerinput_entry.place(relx=0, rely=0.95, relwidth=1, relheight=0.05)  # make the text area take up 5% of the screen

        self.playerinput_entry.bind('<Return>', self.on_enter)

    def check_game_output_queue(self):
        try:
            msg = self.game_output_queue.get(0)  # try to get message from queue
            self.gamewindow_text.config(state='normal')
            self.gamewindow_text.insert('end', msg + '\n')
            self.gamewindow_text.config(state='disabled')
        except queue.Empty:
            pass
        finally:
            self.root.after(100, self.check_game_output_queue)
    
    
    ###### GAME COMMANDS ######        
    def worker(self):
        while True:
            time.sleep(1)  # simulate long running task
            goblin.goblin_behavior()
    
    @staticmethod   
    def quit():
        print("QUITTING GAME")
        game.root.destroy()
        sys.exit()
        
    @staticmethod    
    def help():
        game.game_output_queue.put("Commands: swing, quit, spawn, target, assess, help")

    def on_enter(self, event):
        # get user input and format it and send to game window
        user_input = self.playerinput_var.get()
        append_user_input = f">>> {user_input}"
        self.playerinput_var.set('')
        self.game_output_queue.put(append_user_input)
        # send user input to be processed for action
        self.input_start(user_input)

    def process_command(self, command, args):
        global arg1, arg2, arg3
        if args:
            arg1, *rest = args
            if len(rest) >= 2:
                arg2, arg3 = rest[:2]
            elif len(rest) == 1:
                arg2 = rest[0]
                arg3 = "None"
            else:
                arg2, arg3 = "None", "None"
        global command_function
        command_function = self.command_lookup.get(command)
        if command_function:
            command_function()
            arg1, arg2, arg3 = "None", "None", "None"
        else:
            self.game_output_queue.put("Unknown command: {}".format(command))

    
    command_lookup = {
            #"swing": player.attack,
            "quit": quit,
            #"spawn": Goblin(name="Goblin", health=20, damage=5).spawn_goblin,
            #"target": player.target,
            #"assess": player.assess,
            "help": help,
        }
    
    arg_lookup = {
            "one": 1,
            "two": 2,
            "three": 3,
            "four": 4,
            "five": 5,
            "six": 6,
        }

    def input_start(self, input):
        user_input = input
        command, *args = user_input.split()
        self.process_command(command, args)

    def run(self):
        t_worker = threading.Thread(target=self.worker)
        t_worker.setDaemon(True)
        
        t_player_input = threading.Thread(target=self.on_enter)
        t_player_input.setDaemon(True)
        
        t_game_output = threading.Thread(target=self.check_game_output_queue)
        t_game_output.setDaemon(True)
        
        t_worker.start()
        t_player_input.start()
        t_game_output.start()
        
        self.root.mainloop()


if __name__ == "__main__":
    game = Game()
    game.run()