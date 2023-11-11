import time

print("What would you like to count to?: ")
countto = int(input()) + 1
count = 0

start = time.time()

while count != countto:
    count = count + 1

end = time.time()
rounded = round(end - start, 2)

print()
print()
print()
print()

print("It took your computer: ", rounded, "To count to:", countto - 1)