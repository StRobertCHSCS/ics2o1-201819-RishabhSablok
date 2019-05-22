import arcade


WIDTH = 640
HEIGHT = 480

# Size of the rectangle
RECT_WIDTH = 50
RECT_HEIGHT = 50


center_x = 100      # Initial x position
center_y = 50       # Initial y position
delta_x = 3       # change in x
delta_y = 1      # change in y

def on_update(delta_time):
    global center_x, center_y
    global delta_x, delta_y

    center_x += delta_x
    center_y += delta_y

    # Figure out if we hit the edge and need to reverse.
    if center_x < RECT_WIDTH // 2 or center_x > WIDTH - RECT_WIDTH // 2:
        delta_x *= -1

    if center_y < RECT_HEIGHT // 2 or center_y > HEIGHT - RECT_HEIGHT // 2:
        delta_y *= -1


def on_draw():
    arcade.start_render()
    # Draw in here...
    arcade.draw_rectangle_filled(center_x, center_y, RECT_WIDTH, RECT_HEIGHT, arcade.color.ALIZARIN_CRIMSON)


def on_key_press(key, modifiers):
    pass


def on_key_release(key, modifiers):
    pass


def on_mouse_press(x, y, button, modifiers):
    pass


def setup():
    arcade.open_window(WIDTH, HEIGHT, "My Arcade Game")
    arcade.set_background_color(arcade.color.WHITE)
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