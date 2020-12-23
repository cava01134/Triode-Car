import microbit as m
R_MOTOR = m.pin14
L_MOTOR = m.pin15

def learning_mode(right_res, left_res):
    m.display.show(m.Image.HEART_SMALL)
    r_min = 500
    r_max = 1
    l_min = 500
    l_max = 1
    while True:
        right_res = m.pin1.read_analog()
        left_res = m.pin2.read_analog()
        if right_res >= r_max:
            r_max = right_res
        if right_res < r_min:
            r_min = right_res
        if left_res >= l_max:
            l_max = left_res
        if left_res < l_min:
            l_min = left_res

        print("R:" + str(right_res), "L:" + str(left_res))
        m.sleep(100)
        if m.button_a.was_pressed():
            print('r_max:', r_max, 'r_min:', r_min ,'l_max:', l_max, 'l_min:', l_min)
            save_data(r_max, r_min, l_max, l_min)
            break

def save_data(r_max, r_min, l_max, l_min):
    with open('wheel_data.txt', 'w') as file:
        file.write(str(r_max))
        file.write('\n')
        file.write(str(r_min))
        file.write('\n')
        file.write(str(l_max))
        file.write('\n')
        file.write(str(l_min))

def load_data():
    with open('wheel_data.txt', 'r') as file:
        r_max = int(file.readline())
        r_min = int(file.readline())
        l_max = int(file.readline())
        l_min = int(file.readline())
    right_on_line = (r_min + 40)
    left_on_line = (l_min + 40)
    return right_on_line, left_on_line

def handle_stop_state(state):
    m.display.show("S", wait=False)
    R_MOTOR.write_digital(1)
    L_MOTOR.write_digital(1)

def handle_go_state(state):
    m.display.show("G", wait=False)
    R_MOTOR.write_digital(0)
    L_MOTOR.write_digital(0)
    m.sleep(8)
    R_MOTOR.write_digital(1)
    L_MOTOR.write_digital(1)

def handle_right_state(state):
    m.display.show("R", wait=False)
    R_MOTOR.write_digital(1)
    L_MOTOR.write_digital(0) #Turn Right

def handle_left_state(state):
    m.display.show("L", wait=False)
    R_MOTOR.write_digital(0)
    L_MOTOR.write_digital(1) #Turn Left