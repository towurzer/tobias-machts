import math

import day8_1
import generalMethods


def return_prim_factors(num: int) -> list[int]:
    """returns the list of prime fachtors of num"""
    factors = []
    while num > 1:
        for i in range(2, int(num) + 1):
            if int(num) % i == 0 and generalMethods.is_prime(i):
                factors.append(i)
                num /= i
                break
    return factors


def main(day):
    """gets the input data, extracts instructions (first line) and extracts a dictionary which nodes lead to
    which other nodes depending on whether you are going left or going right (from 3rd line onwards).
    finds the steps needed for each starting position tho end up on a position with "__Z".
    Calculates the steps needed to simultaneously end up on __Z positions for each starting pos."""
    # TODO: get instructions list and steps dictionary
    data = generalMethods.getInputArray(day, separator="\n\n")
    formatted_input = day8_1.format_input_day_8(data)
    instructions = formatted_input[0]
    steps = formatted_input[1]

    # TODO: find circle lengths
    counter = 0
    kgv_input = {}
    start_pos = [key for key in steps.keys() if key[-1] == "A"]
    positions = start_pos.copy()
    finish = [False]
    while not finish[0]:  # while the number of steps for at least one of the starting positions hasn't been found
        for i in range(len(positions.copy())):
            positions[i] = steps[positions[i]][instructions[counter % len(instructions)]]
            if positions[i][-1] == "Z" and start_pos[i] not in kgv_input.keys():
                kgv_input[start_pos[i]] = counter + 1
        counter += 1
        finish = [sp in kgv_input.keys() for sp in start_pos]  # evaluate if done
        finish.sort()

    # TODO: calculate steps
    different_primes = list(set([prime for primes_of_pos in [return_prim_factors(kgv_input[pos]) for pos in start_pos]
                            for prime in primes_of_pos]))  # get all the prime factors of the kgv_input values

    print(math.prod(different_primes))  # calculate the kgv / lcm
    # print(math.prod(different_primes) == 13663968099527)


if __name__ == '__main__':
    main(8)
