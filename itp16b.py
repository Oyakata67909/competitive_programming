n = int(input())
card_list = [input() for i in range(n)]
for suit in ['S', 'H', 'C', 'D']:
    for number in range(1, 14):
        card_check = suit + " " + str(number)
        if not (card_check in card_list): print(card_check)
            


