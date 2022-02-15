maze_rows = int(input())
the_maze = [list(input()) for row in range(1, maze_rows + 1)]
uspeshno=False
number_of_moves=0
cant_get_out=False

for row in range(maze_rows):
    if "k" in the_maze[row]:
        length_columns = len(the_maze[row])
        current_row=row
        if ('k'or f"k{number_of_moves}") in the_maze[0] or ('k' or f"k{number_of_moves}") in the_maze[-1] or ('k'or f"k{number_of_moves}") in the_maze[row][0] or ('k'or f"k{number_of_moves}") in the_maze[row][-1]:
            uspeshno = True
            break

        left_k = the_maze[row][the_maze[row].index('k') - 1]
        if left_k == ' ':
            the_maze[row][the_maze[row].index('k') - 1] = f'k{number_of_moves}'

        right_k = the_maze[row][the_maze[row].index('k') + 1]
        if right_k == ' ':
            the_maze[row][the_maze[row].index('k') + 1] = f'k{number_of_moves}'

        up_k = the_maze[row - 1][the_maze[row].index('k')]
        if up_k == ' ':
            the_maze[row - 1][the_maze[row].index('k')] = f'k{number_of_moves}'
            row -= 1
        down_k = the_maze[row + 1][the_maze[row].index('k')]
        if down_k == ' ':
            the_maze[row + 1][the_maze[row].index('k')] = f'k{number_of_moves}'
            row += 1
        while True:
            number_of_moves += 1
            if  f"k{number_of_moves-1}" in the_maze[0]  or f"k{number_of_moves-1}" in the_maze[-1] or f"k{number_of_moves-1}" in the_maze[row][0] or  f"k{number_of_moves-1}" in the_maze[row][-1]:
                uspeshno = True
                break
            cant_get_out=True
            left_k = the_maze[row][the_maze[row].index(f'k{number_of_moves-1}') - 1]
            if left_k == ' ':
                the_maze[row][the_maze[row].index(f'k{number_of_moves-1}') - 1] = f'k{number_of_moves}'
                cant_get_out=False
            right_k = the_maze[row][the_maze[row].index(f'k{number_of_moves-1}') + 1]
            if right_k == ' ':
                the_maze[row][the_maze[row].index(f'k{number_of_moves-1}') + 1] = f'k{number_of_moves}'
                cant_get_out = False

            up_k = the_maze[row - 1][the_maze[row].index(f'k{number_of_moves-1}')]
            if up_k == ' ':
                the_maze[row - 1][the_maze[row].index(f'k{number_of_moves-1}')] = f'k{number_of_moves}'
                row-=1
                cant_get_out = False

            down_k = the_maze[row + 1][the_maze[row].index(f'k{number_of_moves-1}')]
            if down_k == ' ':
                the_maze[row + 1][the_maze[row].index(f'k{number_of_moves-1}')] = f'k{number_of_moves}'
                row+=1
                cant_get_out=False


            if cant_get_out==True:
                print(f"Kate cannot get out")
                break

if uspeshno:
    print(f"Kate got out in {number_of_moves+1} moves")



