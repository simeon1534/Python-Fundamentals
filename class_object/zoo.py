class Zoo:
    __animals = 0

    def __init__(self, zoo_name):
        self.mammals = []
        self.fishes = []
        self.birds = []
        self.zoo_name = zoo_name

    def add_animal(self, species, name):
        if species == "mammal":
            self.mammals.append(name)
        elif species == "fish":
            self.fishes.append(name)
        elif species == "bird":
            self.birds.append(name)
        self.__animals += 1

    def get_info(self, species):
        result=''
        if species=='mammal':
            result+=f"Mammals in {self.zoo_name}: {', '.join(self.mammals)}"
        elif species == 'fish':
            result += f"Fishes in {self.zoo_name}: {', '.join(self.fishes)}"
        elif species == 'bird':
            result += f"Birds in {self.zoo_name}: {', '.join(self.birds)}"

        result+= f"\nTotal animals: {self.__animals}"

        return result
zoo_name = input()
zoo1 = Zoo(zoo_name)
n = int(input())
for i in range(1, n + 1):
    species_name = input().split(' ')
    zoo1.add_animal(species_name[0], species_name[1])
what_kind_animal = input()
print(zoo1.get_info(what_kind_animal))
