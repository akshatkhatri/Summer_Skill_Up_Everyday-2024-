import random
import statistics

# for _ in range(5):
#     number=random.randint(1,10)
#     print(number)   

cards=["Jack","Queen","King"]

random.shuffle(cards)

for card in cards:
    print(card)

print(statistics.mean([70,60,30,56,23,65,143,12,40,]))