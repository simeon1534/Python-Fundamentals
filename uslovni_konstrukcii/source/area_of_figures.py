from math import pi

figure = str(input())

if figure == 'square':
    razmer = float(input())
    print(f'{razmer * razmer:.3f}')
elif figure == 'rectangle':
    razmer = float(input())
    razmer2 = float(input())
    print(f'{razmer * razmer2:.3f}')
elif figure == 'circle':
    razmer = float(input())
    print(f'{pi*(razmer**2):.3f}')
elif figure == 'triangle':
    razmer = float(input())
    razmer2 = float(input())
    print(f'{(razmer * razmer2)/2:.3f}')

