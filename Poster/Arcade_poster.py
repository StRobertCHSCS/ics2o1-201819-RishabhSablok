import arcade
import ctypes

WIDTH = 600
HEIGHT = 600
RECT_WIDTH = 50
RECT_HEIGHT = 50


center_x = 100      # Initial x position
center_y = 150       # Initial y position
delta_x = 3.5       # change in x
delta_y = 2.5      # change in y

my_button = [500, 300, 100, 100]  # x, y, width, height


def Mbox(title, text, style):
    return ctypes.windll.user32.MessageBoxW(0, text, title, style)


def on_update(delta_time):
    global center_x, center_y
    global delta_x, delta_y

    center_x += delta_x
    center_y += delta_y

    # Figure out if we hit the edge and need to reverse.
    if center_x < RECT_WIDTH // 2 or center_x > WIDTH - RECT_WIDTH // 2:
        delta_x *= -1

    if center_y < RECT_HEIGHT // 2 + 70 or center_y > HEIGHT - RECT_HEIGHT // 2 - 20:
        delta_y *= -1


def on_draw():

    arcade.start_render()
#    texture = arcade.load_texture("Back.jpg")
#    arcade.draw_texture_rectangle(300, 300, texture.width*1.5, texture.height*1.5, texture, 0)
    # Draw in here...
    arcade.draw_text("No Cyber-Bullying", 120, 450, arcade.color.BLACK, font_size=35)
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
    arcade.draw_texture_rectangle(530, 500, 0.6 * texture.width, 0.6 * texture.height, texture)
    arcade.draw_xywh_rectangle_filled(my_button[0], my_button[1], my_button[2], my_button[3], arcade.color.BISQUE)
    arcade.draw_text("Click to learn ", 505, 380, arcade.color.BISTRE, font_size=13)
    arcade.draw_text("more about", 505, 360, arcade.color.BISTRE, font_size=13)
    arcade.draw_text("how bullying", 505, 340, arcade.color.BISTRE, font_size=13)
    arcade.draw_text("affects others", 505, 320, arcade.color.BISTRE, font_size=13)
    texture = arcade.load_texture("NO.jpg")
    arcade.draw_texture_rectangle(60, 420, 0.6 * texture.width, 0.6 * texture.height, texture)
    texture = arcade.load_texture("Words.jpg")
    arcade.draw_texture_rectangle(60, 275, 0.6 * texture.width, 0.6 * texture.height, texture)

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
    my_button_x, my_button_y, my_button_w, my_button_h = my_button

    # Need to check all four limits of the button.
    if (x > my_button_x and x < my_button_x + my_button_w and y > my_button_y and y < my_button_y + my_button_h):
        print("One-third of all kids have been a victim of cyber bullying.\n\nTen to 20 percent of these youth experience this abuse on a continuous basis.\n\nThe most typical forms of bullying online include disrespecting or ignoring the presence of another.\n\nFifty percent of all teens have been exposed to teen cyber abuse, such being a victim, witness, or offender of cyber abuse.\n\n____________________________________________________________________________________________________________________________________________________________________________________")
        Mbox('More Info', 'One-third of all kids have been a victim of cyber bullying.\n\nTen to 20 percent of these youth experience this abuse on a continuous basis.\n\nThe most typical forms of bullying online include disrespecting or ignoring the presence of another.\n\nFifty percent of all teens have been exposed to teen cyber abuse, such being a victim, witness, or offender of cyber abuse.', 0)

    else:
        print("not clicked")


def setup():
    arcade.open_window(WIDTH, HEIGHT, "My Poster")
    arcade.schedule(on_update, 1/60)
    arcade.set_background_color(arcade.color.INDIAN_YELLOW)
    # Override arcade window methods
    window = arcade.get_window()
    window.on_draw = on_draw
    window.on_update = on_update
    window.on_key_press = on_key_press
    window.on_key_release = on_key_release
    window.on_mouse_press = on_mouse_press

    arcade.run()


if __name__ == '__main__':
    setup()
