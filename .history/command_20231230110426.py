from goblin import clsGoblin
from player import clsPlayer

def spawnPlayer():
    objPlayer = clsPlayer(name="Default_Player_Name", health=100, w_equipped="knife", damage=100,  inventory=None)
    return objPlayer

def spawnGoblin():
    clsGoblin.tribe.append(clsGoblin.spawn_goblin())

def Roundtimer(who, objGameWindow):
    try:
        roundtime = who.roundtime
        if roundtime > 0:
            objGameWindow.game_output_queue.put(f"You are on cooldown. You can attack in {roundtime:.2f} seconds.")
        else:
            return True
    except:
        objGameWindow.game_output_queue.put("Invalid rountime value")

def playerattack(objPlayer):
    playerDMG = objPlayer.damage  # add other weapon damage stuff here
    clsGoblin.tribe[objPlayer.attack_target].health -= playerDMG
    
def target(objPlayer, target_monster):
    objPlayer.attack_target = target_monster.arg1

def killGoblin(objPlayer):
    assert objPlayer.attack_target is not None
    del clsGoblin.tribe[objPlayer.attack_target]

def printtest():
    print("test")

