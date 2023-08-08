import tkinter as tk
import threading
import queue
import time
import sys
from goblin import clsGoblin
from player import clsPlayer



class clsGame:
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

        self.command_lookup["help"] = self.help
        self.command_lookup["quit"] = self.quit
        self.command_lookup["spawn"] = clsGoblin.spawn_goblin
        self.command_lookup["target"] = clsPlayer.target
        self.command_lookup["assess"] = clsPlayer.assess
        self.command_lookup["attack"] = clsPlayer.attack

    def check_game_output_queue(self, event=None):
        try:
            msg = self.game_output_queue.get(0)  # try to get message from queue
            self.gamewindow_text.config(state='normal')
            self.gamewindow_text.insert('end', msg + '\n')
            self.gamewindow_text.config(state='disabled')
        except queue.Empty:
            pass
        finally:
            self.root.after(100, self.check_game_output_queue)
    
    def on_enter(self, event=None):
        print("ENTER PRESSED")
        # get user input and format it and send to game window
        User_input = self.playerinput_var.get()
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
        arg1, arg2, arg3 = None, None, None
        print(command, args)
        if args:
            #goes through the list of args and assigns them to arg1, arg2, arg3
            arg1, *rest = args
            if len(rest) >= 2:
                arg2, arg3 = rest[:2]
            elif len(rest) == 1:
                arg2 = rest[0]
                arg3 = None
            else:
                arg2, arg3 = None, None
        command_function = self.command_lookup.get(command)
        if command_function:
            print(arg1, arg2, arg3)
            command_function(command)
        else:
            self.game_output_queue.put("Unknown command: {}".format(command))

    def help(self, *args):
        self.game_output_queue.put("Commands: swing, quit, spawn, target, assess, help")  

    def quit(self, *args):
        print("QUITTING GAME")
        self.root.destroy()
        sys.exit()

    def mainGameLoop():
        while True:
            time.sleep(1)  # simulate long running task


    def run(self):
        
        objPlayer = clsPlayer("Default_Player_Name", 100, "knife", 100, None)
        
        thread_game_output = threading.Thread(target=self.check_game_output_queue)
        thread_game_output.setDaemon=True

        thread_gameLogicWorker = threading.Thread(target=self.mainGameLoop)
        thread_gameLogicWorker.setDaemon=True
        

        objGame.playerinput_entry.bind('<Return>', objGame.on_enter)
        
        thread_gameLogicWorker.start()
        thread_game_output.start()
        
        self.root.mainloop()

if __name__ == "__main__":
    objGame = clsGame()
    objGame.run()