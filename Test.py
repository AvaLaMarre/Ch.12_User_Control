import random

import arcade

SW = 640
SH = 480
SPEED = 10


class Stars:
    def __init__(self, pos_x, pos_y, dy, rad, col):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.dy = dy
        self.rad = rad
        self.col = col

    def draw_star(self):
        arcade.draw_circle_filled(self.pos_x, self.pos_y, self.rad, self.col)

    def update_star(self):
        self.pos_y += self.dy
        if self.pos_y < self.rad:
            self.pos_y = random.randint(SH+20, SH+200)


class Ship:
    def __init__(self, pos_x, pos_y, dx, dy, side1, side2, col):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.dx = dx
        self.dy = dy
        self.side1 = side1
        self.side2 = side2
        self.col = col

    def draw_ship(self):
        arcade.draw_rectangle_filled(self.pos_x, self.pos_y , 10, 40, arcade.color.YELLOW)
        arcade.draw_rectangle_filled(self.pos_x, self.pos_y, 30, 30, arcade.color.ORANGE)
        arcade.draw_arc_filled(self.pos_x, self.pos_y, 50, 50, arcade.color.GREEN, 0, 180, 180)

    def update_ship(self):
        self.pos_y += self.dy
        self.pos_x += self.dx

        if self.pos_x < -60:
            self.pos_x = SW + 20
        elif self.pos_x > SW + 50:
            self.pos_x = -30


class Bullet:
    def __init__(self, pos_x, pos_y, dy, rad, col):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.dy = dy
        self.rad = rad
        self.col = col

    def draw_bullet(self):
        arcade.draw_circle_filled(self.pos_x, self.pos_y, self.rad, self.col)

    def update_bullet(self):
        self.pos_y += self.dy


class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.BLACK)
        self.star_list = []
        self.bullet_list = []
        self.ship = Ship(SW/2, 30, 0, 0, 50, 50, arcade.color.WHITE)
        for i in range(200):
            self.pos_x = random.randint(0, SW)
            self.pos_y = random.randint(0, 600)
            self.rad = random.randint(1, 4)
            self.dy = -1
            self.col = arcade.color.WHITE
            self.star = Stars(self.pos_x, self.pos_y, self.dy, self.rad, self.col)
            self.star_list.append(self.star)
        for i in range(20):
            self.dy = 6
            self.bullet = Bullet(self.ship.pos_x, 60, self.dy, 10, arcade.color.WHITE)
            self.bullet_list.append(self.bullet)

    def on_draw(self):
        arcade.start_render()
        for star in self.star_list:
            star.draw_star()
        self.ship.draw_ship()


    def on_key_press(self, key, modifiers):
        if key == arcade.key.LEFT:
            self.ship.dx = -SPEED
        elif key == arcade.key.RIGHT:
            self.ship.dx = SPEED

        if key == arcade.key.SPACE:
            self.bullet.draw_bullet()

    def on_key_release(self, key, modifiers):
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.ship.dx = 0

    def on_update(self, dt):
        self.ship.update_ship()
        for star in self.star_list:
            star.update_star()
        for bullet in self.bullet_list:
            bullet.update_bullet()


def main():
    window = MyGame(SW, SH, "CSP SPACE INVADERS!")
    arcade.run()


if __name__ == "__main__":
    main()
