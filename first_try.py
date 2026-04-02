
with open(input(), 'r', encoding='utf-8') as input_file:
    grand_list = [item.strip() for item in input_file.readlines()]
    filtered_list = list(filter(lambda item: 'def ' in item or '#' in item, grand_list))
    final_list = list()
    for i in range(len(filtered_list)):
        final_list.append(filtered_list[i]) if filtered_list[i][0] != '#' else None
        if i > 0:
            if filtered_list[i - 1][0] == '#':
                final_list.pop()

    if final_list == []:
        filtered_list = list()
        filtered_list.append('Best Programming Team')
    else:
        filtered_list = [item[:item.index('(')].replace('def ', ' ').strip() for item in final_list]

    print(*filtered_list, sep ='\n')
