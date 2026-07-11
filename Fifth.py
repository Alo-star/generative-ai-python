import random
# heads=0
# trials =10000

# for i in range(trials):
#     if random.choice(["H","T"])=="H":
#         heads+=1
#         print("Probability of Head:",heads/trials)

        # Dice Example
count=0
trials=10000
for i in range(trials):
    if random.randint(1,6)==3:
        count+=1
print("Probability Of getting 3:",count/trials)