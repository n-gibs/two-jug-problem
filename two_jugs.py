#Time complexity: O(N+M)
#Aux Space = O(1)

import sys

def gcd(a:int, b:int) -> int:
    if b == 0:
        return a
    return gcd(b, a%b)

def get_sequence(from_capacity:int, to_capacity:int, target:int) -> list:

    step = 0
    # start with both jugs empty
    sequence=[f'{step}. Start J1 (capacity:{from_capacity}) and J2 (capacity:{to_capacity}) empty -> (0,0)']

    # fill up source jug
    from_jug = to_capacity
    to_jug = 0
    step += 1
    sequence.append(f'{step}. Fill J2 up completely -> ({to_jug},{from_jug})')

    while to_jug is not target and from_jug is not target:

        # the max amount availible to be poured is either the amount in the source jug or the difference between the capacity of the source jug and the amount in the destination jug, which ever is smaller
        max_amt = min(from_jug, from_capacity-to_jug)

        #Empty source jug into destination jug
        to_jug += max_amt
        from_jug -= max_amt
        step += 1
        sequence.append(f'{step}. Transfer water from J2 to J1 -> ({to_jug},{from_jug})')

        # when source jug hits target, dump destination jug
        if from_jug == target:
            to_jug = 0
            step += 1
            sequence.append(f'{step}. Empty J1 completely -> ({to_jug},{from_jug})')
            return sequence

        # when destination jug hits target, dump source jug
        if to_jug == target:
            from_jug = 0
            step += 1
            sequence.append(f'{step}. Empty J2 completely -> ({to_jug},{from_jug})')
            return sequence

        # fill when source jug is empty
        if from_jug == 0:
            from_jug = to_capacity
            step += 1
            sequence.append(f'{step}. Fill J2 up completely -> ({to_jug},{from_jug})')

        #empty when destination jug is at capacity
        if to_jug == from_capacity:
            to_jug = 0
            step += 1
            sequence.append(f'{step}. Empty J1 up completely -> ({to_jug},{from_jug})')

    return sequence

def get_min_sequence(jug_1:int, jug_2:int, target:int):

    # jug_1 needs to be larger than jug_2 to find gcd
    if jug_2 > jug_1:
        jug_2, jug_1 = jug_1, jug_2

    # if the target/gcd is not a whole number
    # the sequence is not achieveable
    if target % gcd(jug_1, jug_2) != 0:
        return -1

    # get both options
    # jug 1 is source
    option_1 = get_sequence(jug_1, jug_2, target)

    # jug 2 is source
    option_2 = get_sequence(jug_2, jug_1, target)

    # return smaller of 2 sequences
    return option_1 if len(option_1) < len(option_2) else option_2

"""
pass 3 numbers in as arguments
1 -> jug_1 capacity
2 -> jug_2 capacity
3 -> target

example:
python3 two_jugs.py 10 6 8
"""
args = sys.argv

result = get_min_sequence(int(args[1]), int(args[2]), int(args[3]))

if result == -1:
    print('not achieveable')
else:
    for i in range(len(result)):
        print(result[i])
