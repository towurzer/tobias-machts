import generalMethods


def string_to_int(string: str) -> int:
    """takes a string and returns an int
    consisting of the integer value of every digit in the input string after each another"""
    num_string = ""
    for c in string:
        if c.isdigit():
            num_string += c

    return int(num_string)


def find_limit(low_limit: int, high_limit: int, t: int, max_score: int) -> int:
    """returns the first number where the distance is greater than max. (method of choice: binary search)"""
    guess = int((high_limit - low_limit) / 2) + low_limit
    g1 = (t - guess) * guess > max_score
    g2 = (t - (guess - 1)) * (guess - 1) > max_score
    if g1 == g2:
        if g1:
            final_guess = find_limit(low_limit, guess, t, max_score)  # too low
        else:
            final_guess = find_limit(guess, high_limit, t, max_score)  # too high
    else:
        return guess
    return final_guess


def main(day):
    """main code that manages all the data.
    gets it from the generalMethods library and formats it with the @string_to_int function
    calls the find_limit function afterwards and gets the first winning number. \n\n
        Because we know that s(wait) = (t-wait)*wait is a quadratic function, which is symmetrical to wait = t/2 and
        streng monoton steigend for wait = [0:t/2) we can do some quick maths to figure out that: \n
        total_wins = (t+1)-2*first_win (t+1 because 0 also a possible element)\n
    prints the margin after calculations done"""
    data = generalMethods.getInputArray(day)
    data = (string_to_int(data[0]), string_to_int(data[1]))
    margin = (data[0] + 1) - (2 * find_limit(0, int(data[0] / 2), data[0], data[1]))
    print(margin)
    # if day == 6: print(margin == 40087680)


if __name__ == '__main__':
    main(6)
