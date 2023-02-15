supported_values = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list_items = ['x', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

x1 = [],
x2 = [],
x3 = [],
x4 = [],
x5 = [],
x6 = [],
x7 = [],
x8 = [],
x9 = [],
list_sudoku = []

print("""
__________________
x,x,x|a,a,a|b,b,b|
x,x,x|a,a,a|b,b,b|
x,x,x|a,a,a|b,b,b|
------------------
c,c,c|d,d,d|e,e,e|
c,c,c|d,d,d|e,e,e|
c,c,c|d,d,d|e,e,e|
------------------
f,f,f|g,g,g|h,h,h|
f,f,f|g,g,g|h,h,h|
f,f,f|g,g,g|h,h,h|
------------------  
""")

while True:
    user_action = input("""
            RULES!!!
1) Type 'add' to input your sudoku. 
Use integers with comma separator. 
Example: 1,2,3,4,5,6,7,8,9 OR 1,x,3,x,5,x,7,x,9
2) Type 'show' or 'display' to show your sudoku
3) Type 'exit' to leave
4) execute!!!
""")

    match user_action:
        case 'add':
            i = 0
            while i < 9:
                user_action = input(f"Input list for section {list_items[i]}:")
                trim_comma = user_action.replace(',', '')
                trim_comma_list = list(user_action)
                list_sudoku.append(user_action)
                i = i + 1
                continue
            print(list_sudoku)

        case 'show' | 'display':
            print(list_sudoku)
        case 'exit':
            break
        case 'execute':
            for x in list_sudoku:
                for x_1 in x:
                    if x_1 in x:
                        pass

                    print(x_1)

print('Poka')
