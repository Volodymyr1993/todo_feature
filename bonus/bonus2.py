a = [1, "vova", 2, ['Vita', 1], 1.2, None]

empty_list = []
value = False
for i in a:
    if isinstance(i, int | float):
        empty_list.append(i)
        print(empty_list)
    elif isinstance(i, list):
        for x in i:
            if isinstance(x, int | float):
                empty_list.append(x)
            else:
                print(f"Value --> {x} in list is not int")
    else:
        print(f"value --> {i} in not int")


print(empty_list)