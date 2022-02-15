population = list(map(int, input().split(', ')))
min_wealth = int(input())
no_equal = False
for i in range(len(population)):
    if population[i] < min_wealth:
        razlikata= min_wealth - population[i]
        max_num=max(population)
        if max_num-razlikata>=min_wealth:
            population[i] +=razlikata
            population[population.index(max_num)] -=   razlikata
         #while population[i]<min_wealth:
         #  population[-1]-=1
          # population[i]+=1

if sum(population) >= len(population) * min_wealth:
    print(population)
else:
    print("No equal distribution possible")