temperature = int(input("Insert Temperature "))
if temperature > 30:
    print("Its warm")
elif temperature > 20:
    print("Its Normal")
else:
    print("Its Cold")

# ternary operator

message = "Hot" if temperature > 30 else "Normal" if temperature > 20 else "Cold"
print(message)
