import tkinter as tk
import threading
import queue
import time
import sys
import random

class clsGame:
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
            #goblin.goblin_behavior()
    
    @staticmethod   
    def quit():
        print("QUITTING GAME")
        clsGame.root.destroy()
        sys.exit()
        
    @staticmethod    
    def help():
        clsGame.game_output_queue.put("Commands: swing, quit, spawn, target, assess, help")

    def on_enter(self):
        # get user input and format it and send to game window
        objUser_input = self.playerinput_var.get()
        append_user_input = f">>> {objUser_input}"
        self.playerinput_var.set('')
        self.game_output_queue.put(append_user_input)
        # send user input to be processed for action
        self.input_start(objUser_input)

    def process_command(self, command, args):
        #global G_arg1, G_arg2, G_arg3
        if args:
            arg1, *rest = args
            if len(rest) >= 2:
                arg2, arg3 = rest[:2]
            elif len(rest) == 1:
                arg2 = rest[0]
                arg3 = "None"
            else:
                arg2, arg3 = "None", "None"
        command_function = self.command_lookup.get(command)
        if command_function:
            G_arg1 = self.arg_lookup.get(arg1)
            G_arg2 = self.arg_lookup.get(arg2)
            G_arg3 = self.arg_lookup.get(arg3)
            command_function()
            arg1, arg2, arg3 = "None", "None", "None"
        else:
            self.game_output_queue.put("Unknown command: {}".format(command))


    def input_start(self, input):
        objUser_input = input
        command, *args = objUser_input.split()
        self.process_command(command, args)

    def run(self):
        thread_worker = threading.Thread(target=self.worker)
        thread_worker.setDaemon(True)
        
        thread_player_input = threading.Thread(target=self.on_enter)
        thread_player_input.setDaemon(True)
        
        thread_game_output = threading.Thread(target=self.check_game_output_queue)
        thread_game_output.setDaemon(True)
        
        thread_worker.start()
        thread_player_input.start()
        thread_game_output.start()
        

        self.root.mainloop()



