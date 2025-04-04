import time
import math

num, delay = 25100, 2123 

time.sleep(delay / 1000)  
result = math.sqrt(num)

print(f"Square root of {num} after {delay} milliseconds is {result}")