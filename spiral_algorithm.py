def counter_clock_spiral(arr: list[int], size: int) -> list[int]:

    # Checks if there are numbers in passed list
    if not arr:
        return 'Empty matrix passed'

    answer = []
    first_row = first_column = counter = 0
    last_row = last_column = size
    total = len(arr)

    # In cycle goes through the indexes of list and builds a new list of integers as if they were placed
    # in counter clockwise spiral order
    while (first_row < last_row and first_column < last_column):

        for i in range(first_row, last_row):
            answer.append(arr[i * size + first_column])
            counter += 1
        first_column += 1

        if (counter == total):
            break

        for i in range(first_column, last_column):
            answer.append(arr[(last_row - 1) * size + i])
            counter += 1
        last_row -= 1

        if (counter == total):
            break

        if (first_row < last_row):
            for i in range(last_row - 1, first_row - 1, -1):
                answer.append(arr[i * size + last_column - 1])
                counter += 1
            last_column -= 1

        if (counter == total):
            break

        if (first_column < last_column):
            for i in range(last_column - 1, first_column - 1, -1):
                answer.append(arr[first_row * size + i])
                counter += 1
            first_row += 1

        if (counter == total):
            break

    return answer