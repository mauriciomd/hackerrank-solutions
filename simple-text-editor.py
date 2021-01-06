def simpleTextEditor(queries, values):
    stack = []
    string = ""
    value_index = 0

    for q in queries:
        if q == 1:
            stack.append(string)
            string += values[value_index]
            value_index += 1
        elif q == 2:
            k = int(values[value_index])
            value_index += 1

            str_size = len(string)
            stack.append(string)
            if str_size == k:
                string = ""
            else:
                string = string[0:str_size - k]
        elif q == 3:
            index = int(values[value_index]) - 1
            value_index += 1
            print(string[index])
        elif q == 4:
            string = stack.pop()


if __name__ == '__main__':
    n_queries = int(input())
    queries = []
    values = []

    for _ in range(n_queries):
        line = input().rstrip().split(' ')

        queries.append(int(line[0]))
        if len(line) > 1:
            values.append(line[1])

    simpleTextEditor(queries, values)
