success = True
for number in range(3):
# for number in range(1, 10, 2):
#    print("Attempt", number, (number) * ".")
    print("Attempt")
    if success:
        print("Successful")
        break
else:
    print("Attempted 3 times and failed")

