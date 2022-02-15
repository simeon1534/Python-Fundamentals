maze_rows = int(input())
the_maze = [list(input()) for row in range(1, maze_rows + 1)]
count = 0
rows=0
print(the_maze)
for row in range(maze_rows):
    if "k" in the_maze[row]:
        left_k = the_maze[row][the_maze[row].index('k') - 1]
        if left_k == ' ':
            the_maze[row][the_maze[row].index('k') - 1] = f'k{count}'

        right_k = the_maze[row][the_maze[row].index('k') + 1]
        if right_k == ' ':
            the_maze[row][the_maze[row].index('k') + 1] = f'k{count}'

        up_k = the_maze[row - 1][the_maze[row].index('k')]
        if up_k == ' ':
            the_maze[row - 1][the_maze[row].index('k')] = f'k{count}'

        down_k = the_maze[row + 1][the_maze[row].index('k')]
        if down_k == ' ':
            the_maze[row + 1][the_maze[row].index('k')] = f'k{count}'
        cols=the_maze[row][the_maze[row].index('k')]
        #k=maze_rows[row][cols]

        while not '' in the_maze[0]==f"k{count}" or the_maze[-1]==f"k{count}":
            count += 1
            left_k = the_maze[row][the_maze[row].index(f'k{count-1}') - 1]
            if left_k == ' ':
                the_maze[row][the_maze[row].index(f'k{count-1}') - 1] = f'k{count}'
                if the_maze[row][the_maze[row].index(f'k{count-1}') - 1] ==the_maze[row][0]:
                    break
            right_k = the_maze[row][the_maze[row].index(f'k{count-1}') + 1]
            if right_k == ' ':
                the_maze[row][the_maze[row].index(f'k{count-1}') + 1] = f'k{count}'
                if the_maze[row][the_maze[row].index(f'k{count-1}') + 1]==the_maze[row][0]:
                    break
            if row>0:
                up_k = the_maze[row - 1][the_maze[row].index(f'k{count - 1}')]
                if up_k == ' ':
                    the_maze[row - 1][the_maze[row].index(f'k{count - 1}')] = f'k{count}'
                    row-=1
            if row<maze_rows-1:
                down_k = the_maze[row + 1][the_maze[row].index(f'k{count - 1}')]
                if down_k == ' ':
                    the_maze[row + 1][the_maze[row].index(f'k{count - 1}')] = f'k{count}'
                    row+=1

            print(the_maze)

print(the_maze)
