tickets = input().split(", ")
winning_symbols = ["@", "#", "$", "^"]


def isJackpot(ticket):
    first_half = ticket[:10]
    second_half = ticket[10:]
    if not first_half == second_half:
        return False
    for symbol in winning_symbols:
        if symbol * 10  == first_half:
            print(f'ticket "{ticket}" - 10{ticket[0]} Jackpot!')
            return True
    return False


def isWinningTicket(ticket):
    first_half = ticket[:10]
    second_half = ticket[10:]
    for symbol in winning_symbols:
        if symbol * 6 in first_half and symbol * 6 in second_half:
            count_left = first_half.count(symbol)
            count_right = second_half.count(symbol)
            count = min(count_left, count_right)
            print(f'ticket "{ticket}" - {count}{symbol}')
            return True
    return False


for ticket in tickets:
    ticket=ticket.strip()


    if not len(ticket) == 20:
        print(f"invalid ticket")
        continue
    if isJackpot(ticket):
        continue

    if isWinningTicket(ticket):
        continue









    print(f'ticket "{ticket}" - no match')