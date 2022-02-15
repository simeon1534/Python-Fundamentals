width = int(input())
length = int(input())
heigth = int(input())
free_space = width * length * heigth
total_space=0
space_diff=0
command=input()

while command!="Done" or space_diff<0:
   carton_space=int(command)
   total_space+=carton_space
   space_diff=abs(total_space-free_space)
   if total_space>=free_space:
      print(f"No more free space! You need {space_diff} Cubic meters more.")
   command=input()
   break

if command == "Done":
      print(f"{space_diff} Cubic meters left.")