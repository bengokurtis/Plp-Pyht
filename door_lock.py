from datetime import datetime


def main():
    set_password = '1234'
    prev = ''

    print(" |  __ \                        | |                | |        / ____|               | |                     ")
    print(" | |  | |   ___     ___    _ __ | |   ___     ___  | | __    | (___    _   _   ___  | |_    ___   _ __ ___  ")
    print(" | |  | |  / _ \   / _ \  | '__|| |  / _ \   / __| | |/ /     \___ \  | | | | / __| | __|  / _ \ | '_ ` _ \ ")
    print(" | |__| | | (_) | | (_) | | |   | | | (_) | | (__  |   <      ____) | | |_| | \__ \ | |_  |  __/ | | | | | |")
    print(" |_____/   \___/   \___/  |_|   |_|  \___/   \___| |_|\_\    |_____/   \__, | |___/  \__|  \___| |_| |_| |_|")
    print("                                                                        __/ |                               ")
    print("                                                                       |___/                                ")

    password = input("Please enter your password to proceed: ")
    if password == set_password:
        print(">> You are successfully logged in!")
        print("You can use the following commands: \n > Open \n > Close \n > Quit")                          
        while True:
            print("Enter a command to execute")
            option = input().lower()
            if option == 'open':
                if prev == 'open':
                    print(">> The door is already open")
                    print(f">> Door last opened at: {last_opened}")
                else:
                    print(">> The door is now open")
                    last_opened = datetime.now()
                    prev = option
            elif option == 'close':
                if prev == 'close':
                    print(">> The door is already locked")
                    print(f">> Door last closed at: {last_closed}")
                else:
                    print(">> The door is now locked")
                    last_closed = datetime.now()
                    prev = option
            elif option == 'quit':
                print(">> Goodbye")
                break
            else:
                print(">> You have entered an invalid option. Try again")
    else:
        print("Sorry. The password you have entered does not match our records\nTry again")
        main()

main()