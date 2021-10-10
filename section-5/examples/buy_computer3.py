#!/usr/bin/env python3

available_parts = ["computer", "monitor", "keyboard", "mouse", "mouse mat", "hdmi cable", "dvd drive"]
valid_choices = []

for i in range(1, len(available_parts) + 1):
    valid_choices.append(str(i))

current_choice = -1
chosen_parts = []

while current_choice != "0":
    if current_choice in valid_choices:
        idx = int(current_choice) - 1
        current_part = available_parts[idx]

        if current_part in chosen_parts:
            chosen_parts.remove(current_part)
        else:
            chosen_parts.append(current_part)
    else:
        print("Please add options from the list below:")
        
        for i, part in enumerate(available_parts):
            print("{}: {}".format(i + 1, part))
        
        print("0: to finish")

    current_choice = input()

print(chosen_parts)
