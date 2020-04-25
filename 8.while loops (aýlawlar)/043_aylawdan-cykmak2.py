# çäksiz aýlawdan çykmak v.2
# flag ulanmak

prompt = ("\nÇykmak üçin,'x' giriň.\nGiriň: ")

flag = True

while flag:
    msg = input(prompt)

    if msg == 'x':
        flag = False
    else:
        print(msg)