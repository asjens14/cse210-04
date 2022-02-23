from game.casting.gem import Gem
from game.shared.color import Color
from game.shared.point import Point

class Red_Gem(Gem):
    def __init__(self) -> None:
        """Creates a new intance of a small rock
        Inherits from the Gem class
        """
        super().__init__()
        self._score=5
        self.set_text("*")
        self.set_color(Color(255,0,0))
        self.set_velocity(Point(0,15))
