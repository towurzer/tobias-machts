import generalMethods
data = generalMethods.getInputArray(1)
end_sum = v_a = v_b = 0
valid_numbers = "zero, one, two, three, four, five, six, seven, eight, nine, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9".split(", ")
number_lib = {"zero": "0", "one": "1", "two": "2", "three": "3", "four": "4",
              "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}

for substring in data:
    a = 999
    b = -1
    for num in valid_numbers:
        if num in substring:
            if substring.index(num) < a:
                a = substring.index(num)
                v_a = num
            if substring.rindex(num) > b:
                b = substring.rindex(num)
                v_b = num

    if not v_a.isdigit():
        v_a = number_lib[v_a]
    if not v_b.isdigit():
        v_b = number_lib[v_b]

    end_sum += int(f"{v_a}{v_b}")

print(end_sum)
