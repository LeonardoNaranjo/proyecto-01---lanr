def on_button_pressed_a():
    basic.show_icon(IconNames.HEART)
    basic.pause(100)
    basic.show_leds("""
        . . . . .
                . # . # .
                . # # # .
                . . # . .
                . . . . .
    """)
    basic.clear_screen()
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_forever():
    pass
basic.forever(on_forever)
