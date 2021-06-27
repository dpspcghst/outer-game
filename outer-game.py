#!/usr/bin/python3

"""
Chthun; or, The Modern Persephone

Demonstrating the capabilities of arcade in a platformer game
Supporting the Arcade Platformer article
at https://realpython.com/platformer-python-arcade/

All game artwork from www.freegameart.org
Game sounds and tile maps by author

"""

import arcade
import pathlib

SCREEN_WIDTH = 1103  # 2206 ideal
SCREEN_HEIGHT = 600.67  # ideal 1201.33
SCREEN_TITLE = "CHTHUN"

ASSETS_PATH = pathlib.Path(__file__).resolve().parent.parent / "assets"


class Platformer(arcade.window):
    """
    """

    def __init__(self) -> None:
        """
        """

        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        self.coins = None
        self.background = None
        self.walls = None
        self.ladders = None
        self.goals = None
        self.enemies = None

        self.player = None

        self.physics_engine = None

        self.score = 0

        self.level = 1

        self.coin_sound = arcade.load_sound(
            str(ASSETS_PATH / "sounds" / "coin.wav")
        )

        self.jump_sound = arcade.load_sound(
            str(ASSETS_PATH / "sounds" / "jump.wav")
        )

        self.victory_sound = arcade.load_sound(
            str(ASSETS_PATH / "sounds" / "victory.wav")
        )

    def setup(self):
        """
        This function sets up the game for the current level.
        """

        pass

    def on_key_press(self, key: int, modifiers: int):
        """
        This function processes key presses. Arguments: key {int} -- Which key was pressed and
        modifiers {int} -- Which modifers were down at the time.
        """

    def on_key_release(self, key: int, modifiers: int):
        """
        This function processes key releases. Arguments: key {int} -- Which key was released and
        modifiers {int} -- Which modifers were down at the time.
        """

    def on_update(self, delta_time: float):
        """
        This function updates the position of all game objects. Arguments: delta_time {float} --
        How much time since the last call.
        """

        pass

    def on_draw(self):
        """
        """

        pass


if __name__ == "__main__":
    """
    """

    window = Platformer()
    window.setup()
    arcade.run()
