is_testing = False

if is_testing:
    raw = '''32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483'''.split('\n')
else:
    with open('day_07.dat') as f:
        raw = f.read().split('\n')

hands = [[list(x.split()[0]), int(x.split()[1])] for x in raw]

card_conversion = {
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    'T': 10,
    'J': 11,
    'Q': 12,
    'K': 13,
    'A': 14
}


def hand_type(hand):
    '''Accept a hand in the form [d, d, d, d, d] and determine which type of hand it is.
        :param hand: A list of five card values [d, d, d, d, d]
        :type amount: list

        :returns: A score from 6 (4 of a kind) to 1 (one high)
        :rtype: int
'''

    hand_dict = dict.fromkeys(set(hand), 0)

    for card in hand:
        hand_dict[card] += 1

    if hand == [1,1,1,1,1]:
        5/0
        return 7

    jokers = 0
    if 1 in hand_dict:
        5/0
        jokers = hand_dict.pop(1)


    card_freq = sorted(hand_dict.values(), reverse=True)
    hand_types = [[1], [2], [2, 2], [3], [3, 2], [4], [5]]

    # what am I doing here... seems very inefficient
    for score, type in enumerate(hand_types):
        if type == card_freq[:len(type)]:
            if jokers > 0:
                5/0
                card_freq[0] += jokers
                jokers = 0
            else:
                return score + 1 + jokers

    print("WARNING: ", card_freq, hand)
# 247891767 248229745 low
#                print(
# f"{str(jokers):>2} {str(_raw_hand):>16} {str(_cards_dict):>32} {str(hand):>22}")
#               1        [3, 1, 1]          {1: 1, 13: 1, 5: 3}  [5, 13, 1, 5, 5]

for idx, whole_hand in enumerate(hands):
    temp = ''.join(whole_hand[0])
    for c, card in enumerate(whole_hand[0]):
        whole_hand[0][c] = card_conversion[card]
    new_whole_hand = [hand_type(whole_hand[0])] + whole_hand + [temp]
    hands[idx] = new_whole_hand

hands.sort()

total_winnings = 0
for rank, hand in enumerate(hands):
    total_winnings += (rank + 1) * hand[2]

print(total_winnings)
