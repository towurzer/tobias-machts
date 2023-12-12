import day9_1
import generalMethods


def predict_value(difference_list: list[list[int]]) -> int:
    """Takes a list that has integer lists in it, extracts the first values, predicts the 0th (previous) ones,
    sums them up and returns them"""
    items_to_sum = [sublist[0] for sublist in difference_list]
    items_to_sum.reverse()

    for i in range(1, len(items_to_sum)):
        items_to_sum[i] = items_to_sum[i]-items_to_sum[i-1]

    return items_to_sum[-1]


def main(day) -> None:
    """main function: iterates through every dataset and predicts the 0th value. sums them up and prints the sum"""
    # TODO: structure Data
    data = generalMethods.getInputArray(day)
    difference_sum = 0
    for dataset in data:
        dataset = list(map(int, dataset.split(" ")))

        # TODO: find differences
        dataset_differences = day9_1.find_differences(dataset)
        difference_list = [dataset] + (dataset_differences.copy())

        # TODO: predict Value and calculate Sum
        difference_sum += (predict_value(difference_list))

    print(difference_sum)
    # print(difference_sum == 905 or difference_sum == 2)


differences = []
if __name__ == '__main__':
    main(9)
