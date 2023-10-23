def main():
    ...
    grocery_list = {}
    add_item(grocery_list)
    items = list(grocery_list)
    items.sort()
    print(i, grocery_list[i] for i in items, sep = " ")


def add_item(in_dict):
    ...
    while True:
        try:
            current_item = input("").upper()
            if current_item in in_dict:
                in_dict[current_item] = in_dict[current_item] + 1
            else:
                in_dict[current_item] = 1
        except EOFError or KeyError:
            break


main()