from email import message
from game.casting.actor import Actor

class Artifact(Actor):
    '''An unmoving actor that gives a message when you 
        run into the player

        Attributes:
        _message(str): a message for the player
    '''
    def __init__(self) -> None:
        """Constructs a new artifact"""
        super().__init__()
        self._message=''
    
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