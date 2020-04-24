import hlt
from hlt import NORTH, EAST, SOUTH, WEST, STILL, Move, Square
import random

class State:
    def __init__ (self):
        self.moves = []

def choose_move(state):
#    move = random.choice((NORTH, EAST, SOUTH, WEST, STILL))
    move = None
    if state.moves:
        last_move = state.moves[-1]
        move = random.choice((NORTH, EAST, SOUTH, WEST, STILL))
        while move == last_move:
            move = random.choice((NORTH, EAST, SOUTH, WEST, STILL))
    else:
        move = random.choice((NORTH, EAST, SOUTH, WEST, STILL))

    state.moves.append(move)
    return move


myID, game_map = hlt.get_init()
hlt.send_init("Micah's Bot")

current_state = State()

while True:
    game_map.get_frame()
    moves = [Move(square, random.choice((NORTH, EAST, SOUTH, WEST, STILL))) for square in game_map if square.owner == myID]
#    moves = [Move(square, choose_move(current_state)) for square in game_map if square.owner == myID]
    hlt.send_frame(moves)
