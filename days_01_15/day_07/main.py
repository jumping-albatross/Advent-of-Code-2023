is_testing = False
is_part_one = False

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

if not is_part_one:
    card_conversion['J'] = 1


def hand_type(hand: list[int]):
    '''Accept a hand in the form [d, d, d, d, d] and determine which type of hand it is.
        :param hand: A list of five card values [d, d, d, d, d]
        :type amount: list

        :returns: A score from 1 to 7 (high card to 5 of a kind)
        :rtype: int
'''
    if hand == [1, 1, 1, 1, 1]:
        return 7

    hand_dict = dict.fromkeys(set(hand), 0)

    for card in hand:
        hand_dict[card] += 1

    jokers = hand_dict.pop(1) if 1 in hand_dict else 0

    card_freq = sorted(hand_dict.values(), reverse=True)

    card_freq[0] += jokers  # always results in stronger hand

    hand_types = [[5], [4], [3, 2], [3], [2, 2], [2], [1]]

    for score, hand_type in enumerate(hand_types):
        if hand_type == card_freq[:len(hand_type)]:
            return len(hand_types) - score

    raise Exception("This should not have happened.")


for i, hand in enumerate(hands):
    for c, card in enumerate(hand[0]):
        hand[0][c] = card_conversion[card]
    hands[i] = [hand_type(hand[0])] + hand

hands.sort()

total_winnings = 0
for rank, hand in enumerate(hands):
    total_winnings += (rank + 1) * hand[2]

print(total_winnings)
