import keyboard

while True:
    try:
        if keyboard.is_pressed('q'):
            break
        else:
            # print("You pressed %s" % keyboard.key)
            pass
    except:
        break
