import arcade


WIDTH = 600
HEIGHT = 600
RECT_WIDTH = 50
RECT_HEIGHT = 50


center_x = 100      # Initial x position
center_y = 150       # Initial y position
delta_x = 3       # change in x
delta_y = 3      # change in y


def on_update(delta_time):
    global center_x, center_y
    global delta_x, delta_y

    center_x += delta_x
    center_y += delta_y

    # Figure out if we hit the edge and need to reverse.
    if center_x < RECT_WIDTH // 2 or center_x > WIDTH - RECT_WIDTH // 2:
        delta_x *= -1

    if center_y < RECT_HEIGHT // 2 + 70 or center_y > HEIGHT - RECT_HEIGHT // 2:
        delta_y *= -1


def on_draw():

    arcade.start_render()
#    texture = arcade.load_texture("Back.jpg")
#    arcade.draw_texture_rectangle(300, 300, texture.width*1.5, texture.height*1.5, texture, 0)
    # Draw in here...
    arcade.draw_text("No Cyber-Bullying", 100, 450, arcade.color.BLACK, font_size=40)
    arcade.draw_circle_filled(600, 0, 280, arcade.color.DARK_BLUE)
    texture = arcade.load_texture("Computer.png")
    scale = 0.3
    arcade.draw_texture_rectangle(500, 120, scale * texture.width, scale * texture.height, texture, 0)
    arcade.draw_text("If you do not want", 430, 180, arcade.color.CADET, font_size=15)
    arcade.draw_text("to say it then why", 430, 155, arcade.color.CADET, font_size=15)
    arcade.draw_text("type it ?", 430, 130, arcade.color.CADET, font_size=15)
    texture = arcade.load_texture("Sign.jpg")
    arcade.draw_texture_rectangle(64, 555, scale * texture.width, scale * texture.height, texture, 0)
    texture = arcade.load_texture("Phone.png")
    arcade.draw_texture_rectangle(50, 100, scale * texture.width, scale * texture.height, texture, 0)
    arcade.draw_text("Use your", 12, 140, arcade.color.BOLE, font_size=11)
    arcade.draw_text("phone wisely", 12, 120, arcade.color.BOLE, font_size=11)
    arcade.draw_text("or YOU WILL", 12, 100, arcade.color.BOLE, font_size=11)
    arcade.draw_text("REGRET IT", 12, 70, arcade.color.BOLE, font_size=15)
    arcade.draw_rectangle_outline(300, 300, 595, 595, arcade.color.BLACK, border_width=5)
    texture = arcade.load_texture("Mean.jpg")
    arcade.draw_texture_rectangle(540, 500, 0.6 * texture.width, 0.6 * texture.height, texture)
    texture = arcade.load_texture("Cops.png")
    arcade.draw_texture_rectangle(center_x, center_y, 0.08 * texture.width, 0.08 * texture.height, texture, 0)
    arcade.draw_text("If you bully", center_x - 30, center_y - 65, arcade.color.BLACK)
    arcade.draw_text("him I will", center_x - 30, center_y - 80, arcade.color.BLACK)
    arcade.draw_text("Bully you !!!", center_x - 30, center_y - 95, arcade.color.BLACK)

def on_key_press(key, modifiers):
    pass


def on_key_release(key, modifiers):
    pass


def on_mouse_press(x, y, button, modifiers):
    pass


def setup():
    arcade.open_window(WIDTH, HEIGHT, "My Poster")
    arcade.schedule(on_update, 1/60)
    arcade.set_background_color(arcade.color.INDIAN_YELLOW)
    # Override arcade window methods
    window = arcade.get_window()
    window.on_draw = on_draw
    window.on_key_press = on_key_press
    window.on_key_release = on_key_release
    window.on_mouse_press = on_mouse_press

    arcade.run()


if __name__ == '__main__':
    setup()
