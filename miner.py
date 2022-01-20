import hashlib
import time
import string
import random

t = time.time()

s = input("Type a secret!\n")
x = hashlib.sha256(bytes(s, encoding="utf-8")).hexdigest()
print(f"Secret! The current hash is:\n{x}")

i = 0
interval = 1

a = []
h = ""

sample = string.ascii_letters + string.digits
size = 1

speed = 0
total = 0

last_time = time.time()
while h != x:
    c = "".join(random.choices(sample, k = size))
    h = hashlib.sha256(bytes(c, encoding="utf-8")).hexdigest()
    speed += 1
    total += 1
    if not h in a:
        a.append(h)
    elif len(sample) ** size == len(a):
        print(f"Increase size to {size}")
        size += 1
        a.clear()
    
    if time.time() - last_time >= interval:
        print(f"{total} hashes - {speed} H/s")
        last_time = time.time()
        speed = 0

print(f"Found! Your secret is {c}\nHash {h}\nBlock size {total}\nAvg Speed {total / (time.time() - t)} H/s")
