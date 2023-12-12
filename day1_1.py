import generalMethods
data = generalMethods.getInputArray(1)
final_sum = a = b = 0

for substring in data:
    for char in substring:
        if char.isdigit():
            a = char
            break
    for char in substring:
        if char.isdigit():
            b = char
    final_sum += int(f"{a}{b}")
print(final_sum)
