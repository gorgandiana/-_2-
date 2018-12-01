import csv
import matplotlib.pyplot as plt
import numpy as np
import json


def in_csv(name, surname, lang, ans_list, com_list):
    line = [name, surname, lang]
    i = 0
    for ans in ans_list:
        line.append(ans)
        line.append(com_list[i])
        i += 1

    with open('data.csv', mode='a', newline='',
              encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(line)


def graph():
    lang_list = []
    with open('data.csv', mode='r', encoding='utf-8') as csvfile:
        data = csv.reader(csvfile)
        next(data, None)
        for row in data:
            lang_list.append(row[2])

    counts = dict()
    for i in lang_list:
        counts[i] = counts.get(i, 0) + 1

    keys = []
    items = []
    for key, item in counts.items():
        keys.append(key)
        items.append(item)
    keyst = tuple(keys)
    y_pos = np.arange(len(keyst))
    plt.bar(y_pos, items, align='center')
    plt.xticks(y_pos, keyst)
    plt.ylabel('count')
    plt.title('Langs')

    plt.savefig('static/stat.png')


def csv_json():
    fieldnames = ("name", "surname", "lang", "ans1", "com1",
                  "ans2", "com2", "ans3", "com3", "ans4", "com4",
                  "ans5", "com5", "ans6", "com6", "ans7", "com7",
                  "ans8", "com8", "ans9", "com9", "ans10", "com10")
    with open('data.csv', mode='r', encoding='utf-8') as csvfile:
        data = csv.DictReader(csvfile, fieldnames)
        next(data, None)
        re = json.dumps(list(data), indent=2, ensure_ascii=False)
    return re


def search(word, lang):
    res = []
    with open('data.csv', mode='r', encoding='utf-8') as csvfile:
        data = csv.reader(csvfile)
        next(data, None)
        if lang == '':
            for row in list(data):
                for item in row:
                    if word == item:
                        res.append(row[0] + ' ' + row[1])
                        break
        else:
            for row in list(data):
                if row[2] == lang:
                    for item in row:
                        if word == item:
                            res.append(row[0] + ' ' + row[1])
                            break
    return res


def search_L():
    langs = []
    with open('data.csv', mode='r', encoding='utf-8') as csvfile:
        data = csv.reader(csvfile)
        next(data, None)
        for row in list(data):
            if row[2] not in langs:
                langs.append(row[2])
    return langs
