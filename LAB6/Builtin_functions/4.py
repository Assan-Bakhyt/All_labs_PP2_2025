import math
import time

first_i = int(input("Enter: ").strip())
second_i = int(input("Enter: ").strip())

time.sleep(second_i/1000)


print(f"Square root of {first_i} after {second_i} miliseconds is {math.sqrt(first_i)}")
