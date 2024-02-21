from game import Game
from map import create_map
from ui import AsciiArtUI

map = [
    "|--------|",
    "|G..|..G.|",
    "|...PP...|",
    "|G....@|.|",
    "|...P..|.|",
    "|--------|"
]

map = create_map(map)
ui = AsciiArtUI(True) # or SimpleUI
game = Game(map, ui)
game.play()