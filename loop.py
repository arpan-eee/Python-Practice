for number in range(3):
    print("Attempt ", number)

for odd in range(1, 100, 2):
    print("Odd Number ", odd)

# breaking a loop - brake
# for else - else will execute if loop doesn't break
# nested loop

# iterable
for x in "Python":
    print(x)

for a in [1, 2, 3, 4, 5]:
    print(a)

num = 10
while num:
    print(num)
    num = num-1

command = ""
while command.lower() != "quit":
    command = input(">")
    print("ECHO ", command)

# infinity loop
# while true:
