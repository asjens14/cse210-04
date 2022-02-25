from game.casting.gem import Gem
from game.shared.color import Color
from game.shared.point import Point

class Blue_Gem(Gem):
    def __init__(self) -> None:
        """Creates a new intance of a blue gem
        Inherits from the Gem class
        """
        super().__init__()
        self._score=20
        self.set_text("*")
        self.set_color(Color(0,0,255))
