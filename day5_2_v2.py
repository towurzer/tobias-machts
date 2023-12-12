import generalMethods


def main(day) -> None:
    data = [map_i.split("\n") for map_i in generalMethods.getInputString(day).split("\n\n")]
    print(data)


if __name__ == '__main__':
    main(0)
