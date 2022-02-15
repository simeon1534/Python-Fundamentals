#n=int(input())

#for char_1 in range(97,100):
  #  letter_1= chr(char_1)
 #   for char_2 in range(97,100):
  #      letter_2= chr(char_2)
  #      for char_3 in range(97, 100):
   #         letter_3 = chr(char_3)
   #         print(f'{letter_1}{letter_2}{letter_3}')
num=int(input())

for i in range(0,num):
    for k in range(0, num):
        for j in range(0, num):
            print(f'{chr(97+i)}{chr(97+k)}{chr(97+j)}')