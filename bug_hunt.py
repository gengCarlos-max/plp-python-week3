count = 1
total = 0

# BUG: The while statement was missing a colon, so I added : at the end.
while count <= 5:
    total = total + count
    count = count + 1

# BUG: The loop used < instead of <=, so it stopped before adding 5.
# BUG: total is an integer, so I converted it to a string using str().
print("Sum of 1 to 5 is: " + str(total))