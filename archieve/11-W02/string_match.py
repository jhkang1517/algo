def string_match(a, b):
    count = 0
    temp_list1 = []
    temp_list2 = []

    for i in range(len(a)):
        if len(a[i:i + 2]) > 1:
            temp_list1.append(a[i:i + 2])
        if len(b[i:i + 2]) > 1:
            temp_list2.append(b[i:i + 2])

    try:
        for idx, val in enumerate(temp_list2):
            if temp_list1[idx] == temp_list2[idx]:
                count += 1
    except IndexError:
        pass

    return count
