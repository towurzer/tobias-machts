import generalMethods


def find_differences(value_list: list[int]) -> list[list[int]]:
    """
    returns the list with lists of the differences between 2 neighbouring values in it \n
    for that it takes an integer list as input and  creates a new list with the differences
    between the neighbouring values. This list gets appended to the final return list. If the differences aren't zero
    it calls itself with the new generated difference list as input, and appends the newly generated different list to
    the final difference list. Then it checks again if all the values are zero. If they are,
    then the final difference list (list[list[int]]) gets returned.
     """
    global differences
    difference_list = []
    for i in range(1, len(value_list)):
        difference_list.append(value_list[i] - value_list[i - 1])

    differences.append(difference_list)

    if difference_list.count(0) != len(difference_list):
        final_difference = find_differences(difference_list)
    else:
        final_difference = differences.copy()
        differences = []  # resets the global list, so that it can be used again, whe the dataset gets evaluated

    return final_difference


def predict_value(difference_list: list[list[int]]) -> int:
    """Takes a list that has integer lists in it, extracts the last values of them and sums them up
    (to predict the next one). returns that prediction"""
    items_to_sum = [sublist[-1] for sublist in difference_list]
    return sum(items_to_sum)


def main(day) -> None:
    """main function: iterates through every dataset and predicts the next value. sums them up and prints the sum"""
    # TODO: structure Data
    data = generalMethods.getInputArray(day)
    difference_sum = 0
    for dataset in data:
        dataset = list(map(int, dataset.split(" ")))

        # TODO: find differences
        dataset_differences = find_differences(dataset)
        difference_list = [dataset] + (dataset_differences.copy())

        # TODO: predict Value and calculate Sum
        difference_sum += (predict_value(difference_list))

    print(difference_sum)
    # print(difference_sum == 1901217887 or difference_sum == 114)


differences = []
if __name__ == '__main__':
    main(9)
