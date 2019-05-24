import arcade


WIDTH = 600
HEIGHT = 600


def on_update(delta_time):
    pass


def on_draw():

    arcade.start_render()
    # Draw in here...
    arcade.draw_text("No Cyber-Bullying", 150, 400, arcade.color.INDIAN_YELLOW, font_size=30)
    arcade.draw_circle_filled(600, 0, 400, arcade.color.BURLYWOOD)
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
    arcade.draw_text("Use your phone wisely or YOU WILL REGRET", 10, 140, arcade.color.BOLE, font_size=10)

    arcade.draw_rectangle_outline(300, 300, 595, 595, arcade.color.BLACK, border_width=5)


def on_key_press(key, modifiers):
    pass


def on_key_release(key, modifiers):
    pass


def on_mouse_press(x, y, button, modifiers):
    pass


def setup():
    arcade.open_window(WIDTH, HEIGHT, "My Poster")
    arcade.set_background_color(arcade.color.GENERIC_VIRIDIAN)
    arcade.schedule(on_update, 1/60)

    # Override arcade window methods
    window = arcade.get_window()
    window.on_draw = on_draw
    window.on_key_press = on_key_press
    window.on_key_release = on_key_release
    window.on_mouse_press = on_mouse_press

    arcade.run()


if __name__ == '__main__':
    setup()
