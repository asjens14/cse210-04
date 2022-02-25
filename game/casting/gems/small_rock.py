from game.casting.gem import Gem
from game.shared.color import Color
from game.shared.point import Point

class Small_Rock(Gem):
    """A visible, moveable thing that changes points
    
    The responsibility of Actor is to keep track of its appearance, position and velocity in 2d 
    space.

    Attributes:
        _text (string): The text to display
        _font_size (int): The font size to use.
        _color (Color): The color of the text.
        _position (Point): The screen coordinates.
        _velocity (Point): The speed and direction.
    """
    def __init__(self) -> None:
        """Creates a new intance of a small rock
        Inherits from the Gem class
        """
        super().__init__()
        self._score=-10
        self.set_text("[]")
        self.set_color(Color(0,255,0))
