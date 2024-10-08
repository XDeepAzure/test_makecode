def on_button_pressed_a():
    led.plot(1, 1)
input.on_button_pressed(Button.A, on_button_pressed_a)

led.plot(0, 0)