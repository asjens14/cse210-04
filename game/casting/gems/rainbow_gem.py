from game.casting.gem import Gem
from game.shared.color import Color
from game.shared.point import Point
import random as rand

class Rainbow_Gem(Gem):
    def __init__(self) -> None:
        """Creates a new intance of a rainbow gem
        Inherits from the Gem class
        """
        super().__init__()
        self._score=10
        self.set_text("*")
        self.set_color(Color(rand.randint(0,255),rand.randint(0,255),rand.randint(0,255)))
