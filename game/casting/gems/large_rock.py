from game.casting.gem import Gem
from game.shared.color import Color
from game.shared.point import Point

class Large_Rock(Gem):
    def __init__(self) -> None:
        super().__init__()
        self._score=-20
        self.set_text("0")
        self.set_color(Color(255,255,0))
