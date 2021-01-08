def maximumElement(queries, values):
    stack = []
    value_index = 0

    for q in queries:
        stack_size = len(stack)

        if q == 1:
            new_value = values[value_index]
            if stack_size == 0:
                stack.append(new_value)
            else:
                top_element = stack[stack_size - 1]
                max_value = max(new_value, top_element)
                stack.append(max_value)

            value_index += 1

        elif q == 2:
            stack.pop()
        elif q == 3:
            print(stack[stack_size - 1])


if __name__ == '__main__':
    n = int(input())

    queries = []
    values = []

    for _ in range(n):
        line = list(map(int, input().rstrip().split()))

        queries.append(line[0])
        if len(line) > 1:
            values.append(line[1])

    maximumElement(queries, values)
