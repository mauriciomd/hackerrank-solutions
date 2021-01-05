def queueUsingTwoStacks(queries, values):
    main_stack = []
    aux_stack = []
    value_index = 0

    for q in queries:
        if q == 1:
            main_stack.append(values[value_index])
            value_index += 1
        else:
            # We only shift date when the current queue is empty
            if len(aux_stack) == 0:
                while len(main_stack) > 0:
                    item = main_stack.pop()
                    aux_stack.append(item)

        if q == 2:
            aux_stack.pop()

        if q == 3:
            last_element_index = len(aux_stack) - 1
            print(aux_stack[last_element_index])


if __name__ == '__main__':
    n_queries = int(input())

    queries = []
    values = []

    for _ in range(n_queries):
        line = list(map(int, input().split(' ')))

        queries.append(line[0])
        if len(line) > 1:
            values.append(line[1])

    queueUsingTwoStacks(queries, values)
