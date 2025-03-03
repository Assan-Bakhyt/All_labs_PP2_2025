a = input("Enter: ")

upper_c = len(list(filter(str.isupper, a)))
lower_c = len(list(filter(str.islower, a)))

print(f"Uppercase letters: {upper_c}")
print(f"Lowercase letters: {lower_c}")