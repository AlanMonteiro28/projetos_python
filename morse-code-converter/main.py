from morse3 import Morse as m 


while True:
    user_input = str(input('What would you like to translate to Morse code? '))

    str_to_morse = m(user_input).stringToMorse()
    print(str_to_morse)

    while True:
        q_converter = int(input('Would you like to translate any more text?\n1. Yes\n2. No\n'))
        if q_converter == 1:
            break
        elif q_converter == 2:
            quit()
        else:
            print('Please enter valid characters.')

    

