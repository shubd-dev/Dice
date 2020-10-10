import random
dice_no = random.randint(0,6)
one = '''-----
|   |
| o |
|   |
-----
'''

two = '''-----
|o  |
|   |
|  o|
-----
'''

three = '''-----
|o  |
| o |
|  o|
-----
'''

four = '''-----
|o o|
|   |
|o o|
-----
'''

five = '''-----
|o o|
| o |
|o o|
-----
'''

six = '''-----
|o o|
|o o|
|o o|
-----
'''
dic = {1:one, 2:two, 3:three, 4:four, 5:five, 6:six}
for dice_nu in dic:
    if dice_no == dice_nu:
        print(dic[dice_nu])