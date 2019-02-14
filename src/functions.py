

def p_move(p, direction):
    direction = direction + "_to"
    if hasattr(p.current_room, direction):
        p.current_room = getattr(p.current_room, direction)
    else:
        print("You can not move to that direction")


def one_word_input(p, pinput):
    if pinput == 'n' or pinput == 's' or pinput == 'e' or pinput == 'w':
        p_move(p, pinput)

    elif pinput == 'i':
        p.display_inventory()


def two_word_input(p, input_list):
    if input_list[0] == 'get' or input_list[0] == 'take':
        item_gotten = False

        if p.current_room.lighted or p.has_light:
            for item_object in p.current_room.items:
                if input_list[1] == item_object.name:
                    p.get_item(item_object)
                    item_gotten = True

            if item_gotten == False:
                print("there is no such item \n")
        else:
            print("Room is too dark to get any item")

    if input_list[0] == 'drop':
        for item_object in p.items:
            if input_list[1] == item_object.name:
                p.drop_item(item_object)

    if input_list[0] == 'hold':
        print("input is HOLD")
        for item_object in p.items:
            if input_list[1] == item_object.name:
                p.hold_item(item_object)


def display_room(p):
    print(f"\nYou are in the {p.current_room.name}")

    if p.current_room.lighted or p.has_light:
        print(p.current_room.description)
        p.current_room.display_items()
    else:
        print("Room is too dark to see anything")
