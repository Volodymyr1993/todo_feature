def get_avarage():
    with open("../journal/17-12-2022.txt", "r") as file:
        data = file.readlines()

    sorted_data = sorted(data)

    list_with_floats = []

    for i in sorted_data:
        stripped_i = i.strip('\n')
        if stripped_i.isdigit():
            list_with_floats.append(stripped_i)
        else:
            pass


    list_with_floats = [float(i) for i in list_with_floats]
    avarage = sum(list_with_floats) / len(list_with_floats)

    return avarage

avarage = get_avarage()
print(avarage)