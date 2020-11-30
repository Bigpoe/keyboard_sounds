import keyboard  # using module keyboard
from ..play_sound import play_sound

def read_inputs():
    while True:  # making a loop
        # try:  # used try so that if user pressed other than the given key error will not be shown
        if keyboard.is_pressed('a'):
            print('A key pressed!')
            play_sound.a_sound()
        if keyboard.is_pressed('b'):
            print('B key pressed!')
            play_sound.b_sound()
        if keyboard.is_pressed('c'):
            print('C key pressed!')
            play_sound.c_sound()
        if keyboard.is_pressed('d'):
            print('D key pressed!')
            play_sound.d_sound()
        if keyboard.is_pressed('e'):
            print('E key pressed!')
            play_sound.e_sound()
        if keyboard.is_pressed('f'):
            print('F key pressed!')
            play_sound.f_sound()
        if keyboard.is_pressed('g'):
            print('G key pressed!')
            play_sound.g_sound()
        if keyboard.is_pressed('h'):
            print('H key pressed!')
            play_sound.h_sound()
        if keyboard.is_pressed('i'):
            print('I key pressed!')
            play_sound.i_sound()
        if keyboard.is_pressed('j'):
            print('J key pressed!')
            play_sound.j_sound()
        if keyboard.is_pressed('k'):
            print('K key pressed!')
            play_sound.k_sound()
        if keyboard.is_pressed('l'):
            print('L key pressed!')
            play_sound.l_sound()
        if keyboard.is_pressed('m'):
            print('M key pressed!')
            play_sound.m_sound()
        if keyboard.is_pressed('n'):
            print('N key pressed!')
            play_sound.n_sound()
        if keyboard.is_pressed('o'):
            print('O key pressed!')
            play_sound.o_sound()
        if keyboard.is_pressed('p'):
            print('P key pressed!')
            play_sound.p_sound()
        if keyboard.is_pressed('q'):
            print('Q key pressed!')
            play_sound.q_sound()
        if keyboard.is_pressed('r'):
            print('R key pressed!')
            play_sound.r_sound()
        if keyboard.is_pressed('s'):
            print('S key pressed!')
            play_sound.s_sound()
        if keyboard.is_pressed('t'):
            print('T key pressed!')
            play_sound.t_sound()
        if keyboard.is_pressed('u'):
            print('U key pressed!')
            play_sound.u_sound()
        if keyboard.is_pressed('v'):
            print('V key pressed!')
            play_sound.v_sound()
        if keyboard.is_pressed('w'):
            print('W key pressed!')
            play_sound.w_sound()
        if keyboard.is_pressed('x'):
            print('X key pressed!')
            play_sound.x_sound()
        if keyboard.is_pressed('y'):
            print('Y key pressed!')
            play_sound.y_sound()
        if keyboard.is_pressed('z'):
            print('Y key pressed!')
            play_sound.z_sound()
