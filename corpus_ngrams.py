from nltk.corpus import PlaintextCorpusReader
from nltk import ngrams
from nltk.collections import Counter
from nltk.metrics import edit_distance
from nltk.probability import LidstoneProbDist, WittenBellProbDist
import nltk
import csv
import sqlite3
import copy





corpus_root = '/home/kamila/Desktop/otherlang'
files = PlaintextCorpusReader(corpus_root, '.*')
print(files.fileids())

corpus = []
for i in files.fileids():
    f = open('/home/kamila/Desktop/otherlang/'+i)
    corpus.append(f.read())

frequencies = Counter([])
freq_bi = Counter([])
freq_tr = Counter([])
freq_fo = Counter([])
freq_fi = Counter([])
for text in corpus:
    token = nltk.word_tokenize(text)

    unigram = ngrams(token, 1)
    bigrams = ngrams(token, 2)
    trigrams = ngrams(token, 3)
    fourgrams = ngrams(token, 4)
    fivegrams = ngrams(token, 5)

    frequencies+=Counter(unigram)
    freq_bi+=Counter(bigrams)
    freq_tr+=Counter(trigrams)
    freq_fo+=Counter(fourgrams)
    freq_fi+=Counter(fivegrams)



# for row in freq_fo:
#     print(str(str(row)[2:str(row).__len__()-2].split("', '")) + ' ' + str(freq_fo[row]))

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


db = sqlite3.connect('db/database.db')

cursor = db.cursor()

# cursor.execute('''DROP TABLE unigram''')
# cursor.execute('''DROP TABLE bigram''')
# cursor.execute('''DROP TABLE trigram''')
# cursor.execute('''DROP TABLE fourgram''')
# cursor.execute('''DROP TABLE fivegram''')
# db.commit()
# db.close()


# TABLE CREATION AND INSERTION
# cursor.execute('''CREATE TABLE unigram(first TEXT, occurence INTEGER)''')
# cursor.execute('''CREATE TABLE bigram(first TEXT, second TEXT, occurence INTEGER)''')
# cursor.execute('''CREATE TABLE trigram(first TEXT, second TEXT, third TEXT, occurence INTEGER)''')
# cursor.execute('''CREATE TABLE fourgram(first TEXT, second TEXT, third TEXT, fourth TEXT, occurence INTEGER)''')
# cursor.execute('''CREATE TABLE fivegram(first TEXT, second TEXT, third TEXT, fourth TEXT, fifth TEXT, occurence INTEGER)''')
# db.commit()
#
# with open("csv's/unigram.csv", 'r') as file:
#     reader = csv.reader(file)
#     for row in reader:
#         # print(row)
#         cursor.execute('''INSERT INTO unigram(first, occurence) VALUES(?,?)''', (row[0], row[1]))
#
# with open("csv's/bigram.csv", 'r') as file:
#     reader = csv.reader(file)
#     for row in reader:
#         # print(row)
#         cursor.execute('''INSERT INTO bigram(first, second, occurence) VALUES(?,?,?)''', (row[0], row[1], row[2]))
#
# with open("csv's/trigram.csv", 'r') as file:
#     reader = csv.reader(file)
#     for row in reader:
#         # print(row)
#         cursor.execute('''INSERT INTO trigram(first, second, third, occurence) VALUES(?,?,?,?)''', (row[0], row[1], row[2], row[3]))
#
# with open("csv's/fourgram.csv", 'r') as file:
#     reader = csv.reader(file)
#     for row in reader:
#         # print(row)
#         cursor.execute('''INSERT INTO fourgram(first, second, third, fourth, occurence) VALUES(?,?,?,?,?)''',
#                        (row[0], row[1], row[2], row[3], row[4]))
#
# with open("csv's/fivegram.csv", 'r') as file:
#     reader = csv.reader(file)
#     for row in reader:
#         # print(row)
#         cursor.execute('''INSERT INTO fivegram(first, second, third, fourth, fifth, occurence) VALUES(?,?,?,?,?,?)''',
#                        (row[0], row[1], row[2], row[3], row[4], row[5]))
#
# db.commit()
# db.close()
# FINISH OF TABLE CREATION AND INSERTION





# cursor.execute('''SELECT * FROM bigram''')
# all_rows = cursor.fetchall()
# for i in all_rows:
#     print('{0} : {1} : {2}'.format(i[0], i[1], i[2]))

#
# cursor.execute('''SELECT * FROM trigram''')
# all_rows = cursor.fetchall()
# for i in all_rows:
#     print('{0} : {1} : {2} : {3}'.format(i[0], i[1], i[2], i[3]))

# cursor.execute('''SELECT * FROM fourgram''')
# all_rows = cursor.fetchall()
# for i in all_rows:
#     print('{0} : {1} : {2} : {3} | {4}'.format(i[0], i[1], i[2], i[3], i[4]))

# cursor.execute('''SELECT * FROM fivegram''')
# all_rows = cursor.fetchall()
# for i in all_rows:
#     print('{0} : {1} : {2} : {3} : {4} | {5}'.format(i[0], i[1], i[2], i[3], i[4], i[5]))
def unigramProb():
    bestSuite = {}
    totalNumberOfWords = 0;
    cursor.execute('''SELECT * FROM unigram''')
    all_rows = cursor.fetchall()
    for i in all_rows:
        totalNumberOfWords += i[1]
        word = i[0]
        if edit_distance(word, userWord) == 1:
            bestSuite[word] = i[1]

    for a in bestSuite.keys():
        print(str(a) + " " + str(bestSuite[a] / totalNumberOfWords))
    return

def bigramProb():
    bestSuite = {}
    totalNumberOfWords = 0;
    cursor.execute('''SELECT * FROM bigram''')
    all_rows = cursor.fetchall()
    for i in all_rows:
        totalNumberOfWords += i[2]
        word = i[0] + ' ' + i[1]
        if edit_distance(word, userWord) < 3:
            bestSuite[word] = i[2]

    for a in bestSuite.keys():
        print(str(a) + " " + str(bestSuite[a] / totalNumberOfWords))
    return bestSuite

def trigramProb():
    bestSuite = {}
    totalNumberOfWords = 0;
    cursor.execute('''SELECT * FROM trigram''')
    all_rows = cursor.fetchall()
    for i in all_rows:
        totalNumberOfWords += i[3]
        word = i[0] + ' ' + i[1] + ' ' + i[2]
        if edit_distance(word, userWord) < 5:
            bestSuite[word] = i[3]

    for a in bestSuite.keys():
        print(str(a) + " " + str(bestSuite[a] / totalNumberOfWords))
    return bestSuite

def fourgramProb():
    bestSuite = {}
    totalNumberOfWords = 0;
    cursor.execute('''SELECT * FROM fourgram''')
    all_rows = cursor.fetchall()
    for i in all_rows:
        totalNumberOfWords += i[4]
        word = i[0] + ' ' + i[1] + ' ' + i[2] + ' ' + i[3]
        if edit_distance(word, userWord) < 7:
            bestSuite[word] = i[4]

    for a in bestSuite.keys():
        print(str(a) + " " + str(bestSuite[a] / totalNumberOfWords))
    return bestSuite

def fivegramProb():
    bestSuite = {}
    totalNumberOfWords = 0;
    cursor.execute('''SELECT * FROM fivegram''')
    all_rows = cursor.fetchall()
    for i in all_rows:
        totalNumberOfWords += i[5]
        word = i[0] + ' ' + i[1] + ' ' + i[2] + ' ' + i[3] + ' ' + i[4]
        if edit_distance(word, userWord) < 10:
            bestSuite[word] = i[5]

    for a in bestSuite.keys():
        print(str(a) + " " + str(bestSuite[a] / totalNumberOfWords))
    return bestSuite

def checkUni(checkWord):
    trueWord = []
    index = 0
    bestSuite = {}
    totalNumberOfWords = 0;
    cursor.execute('''SELECT * FROM unigram''')
    all_rows = cursor.fetchall()
    for i in all_rows:
        totalNumberOfWords += i[1]
        word = i[0]
        if edit_distance(word, checkWord) == 0:
            print("inside")
            element = word
            # trueWord.append(copy.deepcopy(word))
            trueWord.insert(index, word)
            index+=1
            print(trueWord)
            print("<------>")
        elif (edit_distance(word, checkWord) == 1) and (not checkWord in trueWord):
            print(trueWord)
            print(edit_distance(word, checkWord) == 1)
            print(checkWord in trueWord)
            print((edit_distance(word, checkWord) == 1) and (checkWord in trueWord))
            print(' ----- ')
            bestSuite[word] = i[1]

    for a in bestSuite.keys():
        if checkWord.lower() != a.lower():
            print(str(checkWord) + " ---> " + str(a) + " " + str(bestSuite[a] / totalNumberOfWords))
    return

userWord = input('Enter your word: ')

lenght = userWord.split(' ').__len__();

# if lenght == 1:
#     unigramProb()
# elif lenght == 2:
#     bigramProb()
# elif lenght == 3:
#     trigramProb()
# elif lenght == 4:
#     fourgramProb()
# elif lenght == 5:
#     fivegramProb()
for a in range(0, lenght):
    checkUni(userWord.split(' ')[a])
db.close()


