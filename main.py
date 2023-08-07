from game import clsGame
from goblin import clsGoblin
from player import clsPlayer


objPlayer = clsGame.objPlayer
tribe = []

command_lookup = {
    "swing": objPlayer.attack,
    "quit": clsGame.quit,
    # "spawn": Goblin(name="Goblin", health=20, damage=5).spawn_goblin,
    "target": objPlayer.target,
    "assess": objPlayer.assess,
    "help": clsGame.help,
}

arg_lookup = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
}

def spawnPlayer():
    objPlayer = clsPlayer(name="Default_Player_Name", health=100, w_equipped="knife", damage=100,  inventory=None)
    return objPlayer



def spawnGoblin():
    tribe.append(clsGoblin.spawn_goblin())

def Roundtimer(who, objGamewindow):
    try:
        roundtime = who.roundtime
        if roundtime > 0:
            objGamewindow.game_output_queue.put(f"You are on cooldown. You can attack in {roundtime:.2f} seconds.")
        else:
            return True
    except:
        objGamewindow.game_output_queue.put("Invalid rountime value")

def playerattack(objPlayer):
    playerDMG = objPlayer.damage  # add other weapon damage stuff here
    tribe[objPlayer.attack_target].health -= playerDMG

def killGoblin(objPlayer):
    assert objPlayer.attack_target is not None
    del tribe[objPlayer.attack_target]

if __name__ == "__main__":
    objGamewindow = clsGame()
    objGamewindow.run()
