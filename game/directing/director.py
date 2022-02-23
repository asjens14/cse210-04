from game.shared.point import Point
from game.casting.gems.small_rock import Small_Rock
from game.casting.gems.large_rock import Large_Rock
from game.casting.gems.blue_gem import Blue_Gem
from game.casting.gems.rainbow_gem import Rainbow_Gem
from game.casting.gems.red_gem import Red_Gem
import random
class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        _keyboard_service (KeyboardService): For getting directional input.
        _video_service (VideoService): For providing video output.
    """

    def __init__(self, keyboard_service, video_service):
        """Constructs a new Director using the specified keyboard and video services.
        
        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
            video_service (VideoService): An instance of VideoService.
        """
        self._keyboard_service = keyboard_service
        self._video_service = video_service
        self._score=0
        
    def start_game(self, cast):
        """Starts the game using the given cast. Runs the main game loop.

        Args:
            cast (Cast): The cast of actors.
        """
        self._video_service.open_window()
        while self._video_service.is_window_open():
            self._get_inputs(cast)
            self._do_updates(cast)
            self._do_outputs(cast)
        self._video_service.close_window()

    def _get_inputs(self, cast):
        """Gets directional input from the keyboard and applies it to the robot.
        
        Args:
            cast (Cast): The cast of actors.
        """
        robot = cast.get_first_actor("robots")
        velocity = self._keyboard_service.get_direction()
        robot.set_velocity(velocity)        

    def _do_updates(self, cast):
        """Updates the robot's position and resolves any collisions with artifacts.
        
        Args:
            cast (Cast): The cast of actors.
        """
        banner = cast.get_first_actor("banners")
        robot = cast.get_first_actor("robots")
        gems = cast.get_actors("gems")

        banner.set_text(f"Score: {self._score}")
        max_x = self._video_service.get_width()
        max_y = self._video_service.get_height()
        robot.move_next(max_x, max_y)

        #goes through each individual gem and updates it
        for gem in gems:
            gem.move_next(max_x,max_y)
            position = gem.get_position()
            if robot.get_position().equals(position):
                cast.remove_actor("gems",gem)
                self._score += gem.get_score()
                banner.set_text(f"Score: {self._score}")    
            if position.equals(Point(position.get_x(), max_y - 15)):
                cast.remove_actor("gems",gem)
        
        COLS = 60
        CELL_SIZE = 15
        FONT_SIZE = 15

        x = random.randint(1, COLS - 1)
        position = Point(x, 0)
        position = position.scale(CELL_SIZE)
        
        gem = random.choice([Small_Rock(), Large_Rock(), Blue_Gem(), Rainbow_Gem(), Red_Gem()])
        gem.set_font_size(FONT_SIZE)
        gem.set_position(position)
        cast.add_actor("gems", gem)

    def _do_outputs(self, cast):
        """Draws the actors on the screen.
        
        Args:
            cast (Cast): The cast of actors.
        """
        self._video_service.clear_buffer()
        actors = cast.get_all_actors()
        self._video_service.draw_actors(actors)
        self._video_service.flush_buffer()
