from game.casting.gem import Gem
from game.shared.color import Color
from game.shared.point import Point

class Small_Rock(Gem):
    def __init__(self) -> None:
        super().__init__()
        self._score=-10
        self.set_color(Color(0,255,0))
        self.set_velocity(Point(0,15))
