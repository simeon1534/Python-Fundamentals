
class Party:
    def __init__(self):
        self.people = []




party = Party()
command = input()
while True:
    if command == 'End':
        print(f"Going: {', '.join(party.people)}")
        print(f"Total: {len(party.people)}")
        break
    person = command
    party.people.append(person)
    command = input()
