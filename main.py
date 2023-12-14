import subprocess


def console(app, command):
    print('console connected, executing now\n\n')
    subprocess.call(f'.\\{app} {command}')
    # ".\" Allows to run the app as trusted

choice = input('''SIMPLE FLASHER
    1. custom commands
               
Your choice: ''')


if choice == '1':
    cmd_inp = input('''CUSTOM COMMANDS
Your command:
adb ''')
    console('/platform-tools/adb.exe', cmd_inp)

else:
    print(f'{choice} was not an option, try again')
