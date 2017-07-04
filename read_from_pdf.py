import textract
import re
from nltk import ngrams
from nltk.collections import Counter
from nltk.metrics import edit_distance
import nltk
import csv
import sqlite3
from os import listdir

from os.path import isfile, join

def intoCSV():
    with open("csv's/unigram.csv",'w') as out:
        csv_out=csv.writer(out)
        for row in frequencies:
            csv_out.writerow([str(row)[2:str(row).__len__() - 3], str(frequencies[row])])

    with open("csv's/bigram.csv",'w') as out:
        csv_out=csv.writer(out)
        for row in freq_bi:
            element = str(row)[2:str(row).__len__()-2].split("', '")
            csv_out.writerow([element[0], element[1], str(freq_bi[row])])

    with open("csv's/trigram.csv",'w') as out:
        csv_out=csv.writer(out)
        for row in freq_tr:
            element = str(row)[2:str(row).__len__()-2].split("', '")
            csv_out.writerow([element[0], element[1], element[2], str(freq_tr[row])])

    with open("csv's/fourgram.csv",'w') as out:
        csv_out=csv.writer(out)
        for row in freq_fo:
            element = str(row)[2:str(row).__len__()-2].split("', '")
            csv_out.writerow([element[0], element[1], element[2], element[3], str(freq_fo[row])])

    with open("csv's/fivegram.csv",'w') as out:
        csv_out=csv.writer(out)
        for row in freq_fi:
            element = str(row)[2:str(row).__len__()-2].split("', '")
            csv_out.writerow([element[0], element[1], element[2], element[3], element[4], str(freq_fi[row])])


onlyfiles = [f for f in listdir('pdfs/') if isfile(join('pdfs/', f))]

db = sqlite3.connect('db/database.db')


for filename in onlyfiles:
    print('pdfs/'+filename)





    text = textract.process(
        'pdfs/'+filename
    )
    #
    # data = data.replace(u"\u000B", u"")

    out = text.decode('utf8').replace("\n", " ")
    temp = out.split(".")
    res = ""
    for sent in temp:
        if len(sent) != 0:
            res += "<s> " + sent + " <f> "
    print(res)



    data = []

    arr = nltk.word_tokenize(res)
    result = []
    for index in range(0, arr.__len__()):
        if(arr[index] == "<"):
            btw = arr[index] + arr[index+1] + arr[index+2]
            result.append(btw)
        elif arr[index] == ">" or arr[index] == "s" or arr[index] == "f":
            continue
        else:
            result.append(arr[index])

    data.append(result)

    frequencies = Counter([])
    freq_bi = Counter([])
    freq_tr = Counter([])
    freq_fo = Counter([])
    freq_fi = Counter([])



    unigram = ngrams(result, 1)
    bigrams = ngrams(result, 2)
    trigrams = ngrams(result, 3)
    fourgrams = ngrams(result, 4)
    fivegrams = ngrams(result, 5)

    frequencies+=Counter(unigram)
    freq_bi+=Counter(bigrams)
    freq_tr+=Counter(trigrams)
    freq_fo+=Counter(fourgrams)
    freq_fi+=Counter(fivegrams)

    print(frequencies)


    intoCSV()


    cursor = db.cursor()

    with open("csv's/unigram.csv", 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            # print(row)
            cursor.execute('''INSERT INTO unigram(first, occurence) VALUES(?,?)''', (row[0], row[1]))

    with open("csv's/bigram.csv", 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            # print(row)
            cursor.execute('''INSERT INTO bigram(first, second, occurence) VALUES(?,?,?)''', (row[0], row[1], row[2]))

    with open("csv's/trigram.csv", 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            # print(row)
            cursor.execute('''INSERT INTO trigram(first, second, third, occurence) VALUES(?,?,?,?)''', (row[0], row[1], row[2], row[3]))

    with open("csv's/fourgram.csv", 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            # print(row)
            cursor.execute('''INSERT INTO fourgram(first, second, third, fourth, occurence) VALUES(?,?,?,?,?)''',
                           (row[0], row[1], row[2], row[3], row[4]))

    with open("csv's/fivegram.csv", 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            # print(row)
            cursor.execute('''INSERT INTO fivegram(first, second, third, fourth, fifth, occurence) VALUES(?,?,?,?,?,?)''',
                           (row[0], row[1], row[2], row[3], row[4], row[5]))

    db.commit()

db.close()

