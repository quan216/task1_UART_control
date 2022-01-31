


inputString = " "
outputString = inputString.encode('utf-8').hex()
print(outputString)

sum = 0

for i in range(0, 101):
    sum += i
    i += 1

print(sum)

sum = 0

for i in range(0, 11):
    sum -= i
    i += 1

print(sum)