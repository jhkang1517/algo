books = dict()
most_selling = ['z', 0]
for _ in range(int(input())):
    x = input()

    if x not in books:
        books[x] = 1
    books[x] += 1

    if books[x] > most_selling[1]:
        most_selling[0] = x
        most_selling[1] = books[x]

    elif books[x] == most_selling[1]:
        if most_selling[0] > x:
            most_selling[0] = x
            most_selling[1] = books[x]

print(most_selling[0])