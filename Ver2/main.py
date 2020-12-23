import microbit as m
import triodecar as t
import music
r_min = 500
r_max = 1
l_min = 500
l_max = 1
right_res = 1
left_res = 1
right_on_line = 1
left_on_line = 1
STOP, GO, RIGHT, LEFT = range(4)
state = STOP

music.play(music.BA_DING)
m.display.show(m.Image.HAPPY)
print('Press A to start learning, Press B to Go')
while True:
    if m.button_a.was_pressed():
        t.learning_mode(right_res, left_res)
        m.display.show(m.Image.HEART)
    if m.button_b.was_pressed():
        right_on_line, left_on_line = t.load_data()
        while True:
            right_res = m.pin1.read_analog()
            left_res = m.pin2.read_analog()
            #if (right_res >= right_on_line) and (left_res >= left_on_line):
                #state = GO
            if (right_res >= right_on_line) and (left_res < left_on_line):
                state = RIGHT
            if (right_res < right_on_line) and (left_res >= left_on_line):
                state = LEFT
            #if (right_res < right_on_line) and (left_res < left_on_line):
                #state = GO

            if state == STOP:
                t.handle_stop_state(state)
            elif state == RIGHT:
                t.handle_right_state(state)
            elif state == LEFT:
                t.handle_left_state(state)
            else:
                t.handle_go_state(state)
            print("R:" + str(right_res), "L:" + str(left_res))