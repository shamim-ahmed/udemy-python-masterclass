#!/usr/bin/env python3

available_parts = ["computer", "monitor", "keyboard", "mouse", "mouse mat"]
current_choice = "-"
chosen_parts = []

while current_choice != "0":
    if current_choice in "12345":
        idx = int(current_choice) - 1
        chosen_parts.append(available_parts[idx])
    else:
        print("Please add options from the list below:")
        
        for i, part in enumerate(available_parts):
            print("{}: {}".format(i + 1, part))
        
        print("0: to finish")

    current_choice = input()

print(chosen_parts)
