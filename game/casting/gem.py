from game.casting.actor import Actor

class Gem(Actor):
    '''A moving Actor that moves and gives points
       contacted by the player

        Attributes:
        _score(int): points for the player
    '''
    def __init__(self) -> None:
        """Constructs a new gem"""
        super().__init__()
        self._score = 10
    
    def set_message(self, message) -> None:
        """Called to set the artifact's message
            
            Args:
            message(str): a message for the player
        """
        self._message=message
    
    def get_message(self) -> str:
        """Called to get the artifacts message

        returns:
        _message(str): a message for the player
        """
        return self._message