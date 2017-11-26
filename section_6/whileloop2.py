#/usr/bin/env python

available_exits = ["east", "north east", "south"]
chosen_exit = None

while chosen_exit not in available_exits:
    chosen_exit = input("Please specify exit name: ")
    
print("You have chosen {} exit".format(chosen_exit))
