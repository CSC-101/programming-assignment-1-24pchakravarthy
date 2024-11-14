import data

# Write your functions for each part in the space below.

# Part 1
def vowel_count(s: str) -> int:
    count = 0
    for i in range(len(s)):
        if (s[i] in "aeiou"):
            count += 1
        if (s[i] in "AEIOU"):
            count += 1
    return count
# Part 2
def short_lists(clist: list) -> list:
    newList = []
    for sublist in clist:
        if (len(sublist) == 2):
            newList.append(sublist)
    return newList



# Part 3
def ascending_pairs(vlist : list) -> list:
    resultList = []
    for sublist in vlist:
        if len(sublist) == 2:
            resultList.append(sorted(sublist))
        else:
            resultList.append(sublist)
    resultList.sort()
    return resultList



# Part 4
def add_prices(p1 : data.Price, p2 : data.Price) -> data.Price:
    totaldollars = p1.dollars + p2.dollars
    totalcents = p1.cents + p2.cents
    if totalcents >= 100:
        totaldollars += totalcents // 100
        totalcents = totalcents % 100

    return data.Price(totaldollars, totalcents)
# Part 5
def rectangle_area(box : data.Rectangle) -> int:
    width = box.bottom_right.x - box.top_left.x
    height = box.top_left.y - box.bottom_right.y
    return (width * height * -1)



# Part 6
def books_by_author(authorName : str, bookList : list[data.Book]) -> list[data.Book]:
    newList = []
    for i in range(len(bookList)):
        if authorName in data.Book.authors:
            newList.append(bookList[i])
    return newList



# Part 7
def circle_bound(r1 : data.Rectangle) -> data.Circle:
    xCenter = (r1.top_left.x + r1.bottom_right.x) / 2
    yCenter = (r1.top_left.y + r1.bottom_right.y) / 2
    center = data.Point(xCenter, yCenter)
    radius = ((xCenter - r1.top_left.x) ** 2 + (yCenter - r1.top_left.y) ** 2)**0.5
    return data.Circle(center, radius)



# Part 8
def below_pay_average(employees : list) -> list:
    paymoreList = []
    if employees == []:
        return []
    totalpay = 0
    for i in range(len(employees)):
        totalpay += employees[i].pay_rate
    averagepay = totalpay / len(employees)
    for x in range(len(employees)):
        if employees[x].pay_rate < averagepay:
            paymoreList.append(employees[x].name)
    return paymoreList



