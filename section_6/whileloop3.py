#/usr/bin/env python

available_exits = ["east", "north east", "south"]
chosen_exit = None

while chosen_exit not in available_exits:
    chosen_exit = input("Please specify exit name: ")
    
    if chosen_exit == 'end':
        print("Game over. Try again later")
        break
    
else:
    print("Aren't you glad that you got out of that place ?")
