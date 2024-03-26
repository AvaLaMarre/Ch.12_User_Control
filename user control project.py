"""
# 12.0 Jedi Training (10 pts)  Name:________________

Update the code in this chapter to do the following:
Open a 500px by 500px window.
Change the Ball class to a Box class.
Instantiate two 30px by 30px boxes. One red and one blue.
Make the blue box have a speed of 240 pixels/second
Make the red box have a speed of 180 pixels/second
Control the blue box with the arrow keys.
Control the red box with the WASD keys.
Do not let the boxes go off of the screen.
Incorporate different sounds when either box hits the edge of the screen.
Have two people play this TAG game at the same time.
The red box is always "it" and needs to try to catch the blue box.
When you're done demonstrate to your instructor!


Starter Testing Code:
"""
import random

import arcade

SW = 300
SH = 500
SPEED_BLUE = 6


class Ball:
    def __init__(self, pos_x, pos_y, dx, dy, rad, col):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.dx = dx
        self.dy = dy
        self.rad = rad
        self.col = col

    def draw_ball(self):
        arcade.draw_rectangle_filled(self.pos_x, self.pos_y, self.rad, self.rad, self.col)

    def update_ball(self):
        self.pos_y += self.dy
        self.pos_x += self.dx

        if self.pos_x < 15:
            self.pos_x = 15

        if self.pos_x > SW - 15:
            self.pos_x = SW - 15

        if self.pos_y < 15:
            self.pos_y = 15

        if self.pos_y > SH - 15:
            self.pos_y = SH - 15


class Player2(Ball):
    def __init__(self, pos_x, pos_y, dx, dy, rad, col):
        super().__init__(pos_x, pos_y, dx, dy, rad, col)
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.dx = dx
        self.dy = dy
        self.rad = rad
        self.col = col

    def update_ball(self):
        self.pos_y += self.dy

        if self.pos_y < 0:
            self.pos_y = random.randint(600, 780)
            self.pos_x = random.randint(20, 290)


class Player3(Player2):
    def __init__(self, pos_x, pos_y, dx, dy, rad, col):
        super().__init__(pos_x, pos_y, dx, dy, rad, col)
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.dx = dx
        self.dy = dy
        self.rad = rad
        self.col = col


class Player4(Player2):
    def __init__(self, pos_x, pos_y, dx, dy, rad, col):
        super().__init__(pos_x, pos_y, dx, dy, rad, col)
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.dx = dx
        self.dy = dy
        self.rad = rad
        self.col = col


class Player5(Player2):
    def __init__(self, pos_x, pos_y, dx, dy, rad, col):
        super().__init__(pos_x, pos_y, dx, dy, rad, col)
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.dx = dx
        self.dy = dy
        self.rad = rad
        self.col = col


class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.ASH_GREY)
        self.set_mouse_visible(True)
        self.ball = Ball(320, 40, 0, 0, 30, arcade.color.BLUE)
        x = random.randint(4, 298)
        y = random.randint(530, 900)
        x2 = random.randint(4, 298)
        y2 = random.randint(530, 900)
        x3 = random.randint(4, 298)
        y3 = random.randint(530, 900)
        x4 = random.randint(4, 298)
        y4 = random.randint(530, 900)
        self.player2 = Player2(x, y, 0, -10, 20, arcade.color.RED)
        self.player3 = Player3(x2, y2, 0, -10, 20, arcade.color.RED)
        self.player4 = Player4(x3, y3, 0, -10, 20, arcade.color.RED)
        self.player5 = Player5(x4, y4, 0, -10, 20, arcade.color.RED)

    def on_draw(self):
        arcade.start_render()
        self.ball.draw_ball()
        self.player2.draw_ball()
        self.player3.draw_ball()
        self.player4.draw_ball()
        self.player5.draw_ball()

    def on_key_press(self, key, modifiers):
        if key == arcade.key.LEFT:
            self.ball.dx = -SPEED_BLUE
        elif key == arcade.key.RIGHT:
            self.ball.dx = SPEED_BLUE

    def on_key_release(self, key, modifiers):
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.ball.dx = 0

    def on_update(self, dt):
        self.ball.update_ball()
        self.player2.update_ball()
        self.player3.update_ball()
        self.player4.update_ball()
        self.player5.update_ball()

        if self.ball.pos_x - 25 <= self.player2.pos_x <= self.ball.pos_x + 25 and self.player2.pos_y <= 50:
            arcade.set_background_color(arcade.color.BLACK)
            self.player2.dy *= 0
            self.player3.dy *= 0
            self.player4.dy *= 0
            self.player5.dy *= 0

        elif self.ball.pos_x - 25 <= self.player3.pos_x <= self.ball.pos_x + 25 and self.player3.pos_y <= 50:
            arcade.set_background_color(arcade.color.BLACK)
            self.player2.dy *= 0
            self.player3.dy *= 0
            self.player4.dy *= 0
            self.player5.dy *= 0

        elif self.ball.pos_x - 25 <= self.player4.pos_x <= self.ball.pos_x + 25 and self.player4.pos_y <= 50:
            arcade.set_background_color(arcade.color.BLACK)
            self.player2.dy *= 0
            self.player3.dy *= 0
            self.player4.dy *= 0
            self.player5.dy *= 0

        elif self.ball.pos_x - 25 <= self.player5.pos_x <= self.ball.pos_x + 25 and self.player5.pos_y <= 50:
            arcade.set_background_color(arcade.color.BLACK)
            self.player2.dy *= 0
            self.player3.dy *= 0
            self.player4.dy *= 0
            self.player5.dy *= 0


def main():
    window = MyGame(SW, SH, "User Control Practice")
    arcade.run()


if __name__ == "__main__":
    main()
