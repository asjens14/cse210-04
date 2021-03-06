from random import randint, random
from game.casting.actor import Actor
from game.shared.point import Point

class Gem(Actor):
    '''A moving Actor that moves and gives points
       contacted by the player

        Attributes:
        _score(int): points for the player
    '''
    def __init__(self) -> None:
        """Constructs a new gem"""
        super().__init__()
        self._score=0
        self.set_velocity(Point(0,15))
    
    def get_score(self):
      """Returns the score"""
      return self._score