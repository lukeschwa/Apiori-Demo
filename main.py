# Luke Schauble
from apyori import apriori
import pandas as pd
import csv


def insert(list, subList):
    i = 0
    length = len(list)
    while i < length:
        if float(list[i][2]) > subList[2]:
            break
        i += 1

    list = list[:i] + [subList] + list[i:]
    return list


def main():
    support = 100
    baskets = []
    with open("browsing-data.txt", "r") as a_file:
        for line in a_file:
            baskets.append(line.split(' ')[:-1])

    index = 0
    temp = 0

    with open('browsing-data.txt', 'r') as csvfile:
        hw1reader = csv.reader(csvfile, delimiter=' ')
        for row in hw1reader:
            new_str = ''
            if index == 0:
                temp = len(row)
            elif len(row) > temp:
                temp = len(row)
            index = index + 1

            for x in range(len(row)):
                if (row[x] != ''):
                    new_str += row[x]
                    new_str += ', '

    print('Maximum Length: ', temp)

    maxLength = temp

    index = 0
    temp = 0

    new_file = ''

    with open('browsing-data.txt', 'r') as csvfile:
        hw1reader = csv.reader(csvfile, delimiter=' ')
        for row in hw1reader:
            new_str = ''
            index += 1

            for x in range(len(row)):
                if (row[x] != ''):
                    new_str += row[x]
                    new_str += ', '



            if (len(row) < maxLength):
                diff = maxLength - len(row)
                for x in range(len(row), maxLength):
                    new_str += ', '


            new_file = new_file + '\n' + new_str + '\n'




    with open("browsing-data-fixed.txt", "w+") as f:
        f.write(new_file)

    data = pd.read_csv('browsing-data-fixed.txt', header=None)
    data.head()

    data.dropna()
    data.head()
    data.info()

    records = []
    rows = data.shape[0]
    cols = data.shape[1]
    print(rows)
    print(cols)

    for i in range(0, rows):
        records.append([str(data.values[i, j]) for j in range(0, cols)])
    sup = 100 / rows

    hw1rules = apriori(records, min_support=sup, min_confidence=0.4, min_lift=3, min_length=2)
    hw1results = list(hw1rules)


    pairs = []
    triples = []

    for item in hw1results:

        pair = item[0]
        items = [i for i in pair]

        if (len(items) == 2 and items[0] != ' ' and items[1] != ' '):
            sub = [str(items[0]), str(items[1]), float(item[2][0][2])]
            pairs = insert(pairs, sub)

        if (len(items) == 3 and items[0] != ' ' and items[1] != ' ' and items[2] != ' '):
            sub = [str(items[0]), str(items[1]), float(item[2][0][2]), str(items[2])]
            triples = insert(triples, sub)

    with open("output.txt", 'w+') as f:
        length_pair = len(pairs)
        length_triple = len(triples)
        i = 1
        i2 = 1
        f.write("OUTPUT A\n")
        while i < 6:
            f.write(pairs[length_pair - i][0] + " " + pairs[length_pair - i][1] + " " + str(pairs[length_pair - i][2]) + "\n")
            i += 1
        f.write("OUTPUT B\n")
        while i2 < 6:
            f.write(triples[length_triple - i2][0] + " " + triples[length_triple - i2][1] + " " + triples[length_triple - i2][3] + " " + str(
                triples[length_triple - i2][2]) + "\n")
            i2 += 1


if __name__ == "__main__":
    main()