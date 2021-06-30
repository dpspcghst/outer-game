"""
Outer (v0.0.014)

Demonstrating the capabilties of arcade in a platformer game
Supporting the Arcade Platformer article
at https://realpython.com/platformer-python-arcade/

All game artwork from www.kenney.nl
Game sounds and tile maps by author
"""

import arcade


class Platformer(arcade.window):
    """
    This class runs the entire game. The following methods are called to
    update game state, process user input, and draw items on the screen.
    """

    def __init__(self):
        """
        This function initializes the game object.
        """

        pass

    def setup(self):
        """
        This function sets up the game for the current level.
        """

        pass

    def on_key_press(self, key: int, modifiers: int):
        """
        This function processes key presses. Arguments: key {int} -- which
        key was pressed, modifiers {int} -- which modifiers were down at
        the time.
        """

        pass

    def on_key_release(self, key: int, modifiers: int):
        """
        This function processes key releases. Arguments: key {int} -- which
        key was released, modifiers {int} -- which modifiers were down at
        the time.
        """

        pass

    def on_update(self, delta_time: float):
        """
        This function updates the position of all game objects. Arguments:
        delta_time {float} -- how much time since the last call.
        """

        pass

    def on_draw(self):
        """
        This function draws everything displayed in Outer.
        """

        pass


if __name__ == "__main__":
    """
    This is the main entry point for Outer. This is where the game object
    window is created, the game is set up, and the game loop is kicked off.
    """

    window = Platformer()
    window.setup()
    arcade.run()
