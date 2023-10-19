elements = input().split()

turns_so_far = 0
is_game_won = False
command = input()

while command != "end":
    turns_so_far += 1
    index1, index2 = map(int, command.split())

    if index1 == index2 or index1 < 0 or index2 < 0 or index1 >= len(elements) or index2 >= len(elements):
        middle_index = int(len(elements) / 2)
        elements.insert(middle_index, f"-{turns_so_far}a")
        elements.insert(middle_index, f"-{turns_so_far}a")
        print("Invalid input! Adding additional elements to the board")

    elif elements[index1] == elements[index2]:
        found_element = elements.pop(index1)
        elements.remove(found_element)
        print(f"Congrats! You have found matching elements - {found_element}!")
    else:
        print("Try again!")

    if len(elements) == 0:
        is_game_won = True
        break

    command = input()

if is_game_won:
    print(f"You have won in {turns_so_far} turns!")
else:
    print("Sorry you lose :(")
    print(" ".join(elements))
