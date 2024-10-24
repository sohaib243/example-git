import random


for i in range(1, 10):
    print(f"Dice Throw: {random.randint(1, 6)}")

from datetime import datetime

current_date_time = datetime.now()
print(current_date_time)

summer = datetime(2024, 7, 1)

if current_date_time < summer:
    print("It is not summer")
elif current_date_time == summer:
    print("Mid Summer")
elif:
    print("Summer is gone")
