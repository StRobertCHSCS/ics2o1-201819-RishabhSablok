import arcade
import ctypes


WIDTH = 600
HEIGHT = 600
time = 0
time2 = 0
time_a = 0
a = 1
a1 = 1
b = 1
c = 1
d = 1
score = 0
answer2 = False
q1b1 = False
q1b2 = False
q1b3 = False
q1b4 = False
q2b1 = False
q2b2 = False
q2b3 = False
q2b4 = False
q3b1 = False
q3b2 = False
q3b3 = False
q3b4 = False
q4b1 = False
q4b2 = False
q4b3 = False
q4b4 = False
answer1 = False
check_answer1 = False
check_answer2 = False
# There are better ways to represent buttons
my_button = [450, 450, 70, 70]  # x, y, width, height
my_button2 = [450, 325, 70, 70]
my_button3 = [450, 200, 70, 70]
my_button4 = [450, 75, 70, 70]
show_text = False
show_text1 = False
show_text2 = False
show_text3 = False


def box(title, text, style):
    return ctypes.windll.user32.MessageBoxW(0, text, title, style)


def on_update(delta_time):
    pass


def on_draw():
    arcade.start_render()
    # Draw in here...
    global time, time2, a, b, c, d, answer1, time_a, answer2
    if 10 - time // 70 > 0:
        arcade.draw_text("You have " + str(10 - time // 70) + " seconds left to answer the question.", 135, 30, arcade.color.RED, 12)
        time += 1
    time2 += 1
    if time2 // 700 == 0:
        arcade.draw_text("How many bits are there is one byte ?", 20, 550, arcade.color.BLACK, font_size=30)
        arcade.draw_text("2", 100, 475, arcade.color.BLACK, font_size=30)
        arcade.draw_text("8", 100, 350, arcade.color.BLACK, font_size=30)
        arcade.draw_text("64", 100, 225, arcade.color.BLACK, font_size=30)
        arcade.draw_text("1024", 100, 100, arcade.color.BLACK, font_size=30)
        if q1b2 and a == 1:
            box('RIGHT', 'Right answer, 1 byte is 8 bits. Now wait until the timer ends.', 0)
            a += 1
        elif (q1b1 or q1b3 or q1b4) and b == 1:
            box('WRONG', "Wrong answer, the correct answer is 8.", 0)
            b += 1

    if time2 // 700 == 1:
        if 10 - time_a // 70 > -1:
            arcade.draw_text("You have " + str(10 - time_a // 70) + " seconds left to answer the question.", 135, 30,
                             arcade.color.RED, 12)
        time_a += 1
        arcade.draw_text("What is Internet ?", 20, 550, arcade.color.BLACK, font_size=40)
        arcade.draw_text("Internet is a magic device", 100, 475, arcade.color.BLACK, font_size=20)
        arcade.draw_text("Internet is a bundle of computers", 100, 350, arcade.color.BLACK, font_size=20)
        arcade.draw_text("Internet is a system of computers", 100, 250, arcade.color.BLACK, font_size=20)
        arcade.draw_text("connected to each other.", 100, 210, arcade.color.BLACK, font_size=20)
        arcade.draw_text("Internet is a place to store all your data", 100, 100, arcade.color.BLACK, font_size=10)
        if q2b3 and c == 1:
            box('RIGHT', 'Right answer,Please wait until the timer ends.', 0)
            c += 1
        elif (q2b1 or q2b2 or q2b4) and d == 1:
            box('WRONG', "Wrong answer, the correct answer is, internet is a system of computers connected to each other around the world.", 0)
            d += 1

    if time2 // 700 == 2:
        arcade.draw_text("What is ", 20, 550, arcade.color.BLACK, font_size=30)
        arcade.draw_text("2", 100, 475, arcade.color.BLACK, font_size=30)
        arcade.draw_text("8", 100, 350, arcade.color.BLACK, font_size=30)
        arcade.draw_text("64", 100, 225, arcade.color.BLACK, font_size=30)
        arcade.draw_text("1024", 100, 100, arcade.color.BLACK, font_size=30)
        if 10 - time // 70 > -1:
            arcade.draw_text("You have " + str(10 - time // 70) + " seconds left to answer the question.", 135, 30,
                             arcade.color.RED, 12)
            time += 1
    if time2 // 700 == 3:
        arcade.draw_text("How many bits are there is one byte ?", 20, 550, arcade.color.BLACK, font_size=30)
        arcade.draw_text("2", 100, 475, arcade.color.BLACK, font_size=30)
        arcade.draw_text("8", 100, 350, arcade.color.BLACK, font_size=30)
        arcade.draw_text("64", 100, 225, arcade.color.BLACK, font_size=30)
        arcade.draw_text("1024", 100, 100, arcade.color.BLACK, font_size=30)
    if time2 // 700 == 4:
        exit()

    arcade.draw_xywh_rectangle_filled(my_button[0],
                                      my_button[1],
                                      my_button[2],
                                      my_button[3],
                                      arcade.color.BLACK)
    arcade.draw_xywh_rectangle_filled(my_button2[0],
                                      my_button2[1],
                                      my_button2[2],
                                      my_button2[3],
                                      arcade.color.BLACK)
    arcade.draw_xywh_rectangle_filled(my_button3[0],
                                      my_button3[1],
                                      my_button3[2],
                                      my_button3[3],
                                      arcade.color.BLACK)
    arcade.draw_xywh_rectangle_filled(my_button4[0],
                                      my_button4[1],
                                      my_button4[2],
                                      my_button4[3],
                                      arcade.color.BLACK)


"""
        elif q1b3 and c == 1:
            box('Wrong', 'Wrong answer, the correct answer is 8.', 0)
            c += 1
            score -= 1
        elif q1b4 and d == 1:
            box('Wrong', 'Wrong answer, the correct answer is 8.', 0)
            d += 1
        if (d == 2 or c == 2 or b == 2) and question_cancel1 == 1 :
            score -= 1

"""


def on_key_press(key, modifiers):
    pass


def on_key_release(key, modifiers):
    pass


def on_mouse_press(x, y, button, modifiers):
    global show_text, show_text1, show_text2, show_text3, q1b1, q1b2, q1b3, q1b4, q2b1, q2b2, q2b3, q2b4, q3b1, q3b2, q3b3, q3b4, q4b1, q4b2, q4b3, q4b4

    # unpack the button list into readable? variables.
    my_button_x, my_button_y, my_button_w, my_button_h = my_button
    my_button2_x, my_button2_y, my_button2_w, my_button2_h = my_button2
    my_button3_x, my_button3_y, my_button3_w, my_button3_h = my_button3
    my_button4_x, my_button4_y, my_button4_w, my_button4_h = my_button4

    # Need to check all four limits of the button.
    if x > my_button_x and x < my_button_x + my_button_w and y > my_button_y and y < my_button_y + my_button_h:
        if time2 // 700 == 0:
            show_text = True
            q1b1 = True
        elif time2 // 700 == 1:
            show_text1 = True
            q2b1 = True
        elif time2 // 700 == 2:
            show_text2 = True
            q3b1 = True
        elif time2 // 700 == 3:
            show_text3 = True
            q4b1 = True
    if x > my_button2_x and x < my_button2_x + my_button2_w and y > my_button2_y and y < my_button2_y + my_button2_h:
        if time2 // 700 == 0:
            show_text = True
            q1b2 = True
        elif time2 // 700 == 1:
            show_text1 = True
            q2b2 = True
        elif time2 // 700 == 2:
            show_text2 = True
            q3b2 = True
        elif time2 // 700 == 3:
            show_text3 = True
            q4b2 = True
    if x > my_button3_x and x < my_button3_x + my_button3_w and y > my_button3_y and y < my_button3_y + my_button3_h:
        if time2 // 700 == 0:
            show_text = True
            q1b3 = True
        elif time2 // 700 == 1:
            show_text1 = True
            q2b3 = True
        elif time2 // 700 == 2:
            show_text2 = True
            q3b3 = True
        elif time2 // 700 == 3:
            show_text3 = True
            q4b3 = True
    if x > my_button4_x and x < my_button4_x + my_button4_w and y > my_button4_y and y < my_button4_y + my_button4_h:
        if time2 // 700 == 0:
            show_text = True
            q1b4 = True
        elif time2 // 700 == 1:
            show_text1 = True
            q2b4 = True
        elif time2 // 700 == 2:
            show_text2 = True
            q3b4 = True
        elif time2 // 700 == 3:
            show_text3 = True
            q4b4 = True


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
