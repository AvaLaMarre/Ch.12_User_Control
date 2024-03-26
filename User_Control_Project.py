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
import arcade

SW = 500
SH = 500
SPEED_RED = 3
SPEED_BLUE = 4


class Ball:
    def __init__(self, pos_x, pos_y, dx, dy, rad, col):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.dx = dx
        self.dy = dy
        self.rad = rad
        self.col = col
        self.laser_sound = arcade.load_sound('laser.wav')

    def draw_ball(self):
        arcade.draw_rectangle_filled(self.pos_x, self.pos_y, self.rad, self.rad, self.col)

    def update_ball(self):
        self.pos_y += self.dy
        self.pos_x += self.dx

        if self.pos_x < 15:
            self.pos_x = 15

        elif self.pos_x > SW - 15:
            self.pos_x = SW - 15

        elif self.pos_y < 15:
            self.pos_y = 15

        elif self.pos_y > SH - 15:
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
        if self.pos_x >= 460 and self.pos_y >= 460:
            for i in range(5):
                arcade.set_background_color(arcade.color.PINK)
                arcade.set_background_color(arcade.color.BABY_BLUE)





class Background:
    def __init__(self, col):
        self.col = col

    def draw_background(self):
        # Vert
        arcade.draw_rectangle_filled(430, 200, 50, 300, self.col)

        arcade.draw_rectangle_filled(180, 400, 50, 200, self.col)

        arcade.draw_rectangle_filled(80, 150, 50, 600, self.col)
        arcade.draw_rectangle_filled(280, 310, 250, 80, self.col)
        arcade.draw_rectangle_filled(280, 90, 250, 80, self.col)
        # Hor
        arcade.draw_rectangle_filled(220, 200, 260, 50, self.col)
        arcade.draw_rectangle_filled(385, 425, 260, 50, self.col)


class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.PASTEL_BLUE)
        self.set_mouse_visible(True)
        self.ball = Ball(320, 240, 0, 0, 30, arcade.color.BLUE)
        self.player2 = Player2(470, 470, 0, 0, 40, arcade.color.RED)
        self.background = Background(arcade.color.BABY_PINK)

    def on_draw(self):
        arcade.start_render()
        self.ball.draw_ball()
        self.player2.draw_ball()
        self.background.draw_background()

    def on_key_press(self, key, modifiers):
        if key == arcade.key.LEFT:
            self.ball.dx = -SPEED_BLUE
        elif key == arcade.key.RIGHT:
            self.ball.dx = SPEED_BLUE
        elif key == arcade.key.UP:
            self.ball.dy = SPEED_BLUE
        elif key == arcade.key.DOWN:
            self.ball.dy = -SPEED_BLUE

    def on_key_release(self, key, modifiers):
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.ball.dx = 0
        elif key == arcade.key.UP or key == arcade.key.DOWN:
            self.ball.dy = 0

    def on_update(self, dt):
        self.ball.update_ball()
        self.player2.update_ball()


def main():
    window = MyGame(SW, SH, "User Control Practice")
    arcade.run()


if __name__ == "__main__":
    main()
