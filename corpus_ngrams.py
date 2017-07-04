from nltk.corpus import PlaintextCorpusReader
from nltk import ngrams
from nltk.collections import Counter
from nltk.metrics import edit_distance
from nltk.probability import LidstoneProbDist, WittenBellProbDist
import nltk
import csv
import sqlite3
import copy





# corpus_root = '/home/kamila/Desktop/otherlang'
# files = PlaintextCorpusReader(corpus_root, '.*')
# print(files.fileids())
#
# corpus = []
# for i in files.fileids():
#     f = open('/home/kamila/Desktop/otherlang/'+i)
#     corpus.append(f.read())
#
# frequencies = Counter([])
# freq_bi = Counter([])
# freq_tr = Counter([])
# freq_fo = Counter([])
# freq_fi = Counter([])
# for text in corpus:
#     token = nltk.word_tokenize(text)
#
#     unigram = ngrams(token, 1)
#     bigrams = ngrams(token, 2)
#     trigrams = ngrams(token, 3)
#     fourgrams = ngrams(token, 4)
#     fivegrams = ngrams(token, 5)
#
#     frequencies+=Counter(unigram)
#     freq_bi+=Counter(bigrams)
#     freq_tr+=Counter(trigrams)
#     freq_fo+=Counter(fourgrams)
#     freq_fi+=Counter(fivegrams)



# for row in freq_fo:
#     print(str(str(row)[2:str(row).__len__()-2].split("', '")) + ' ' + str(freq_fo[row]))

# def intoCSV():
#     with open("csv's/unigram.csv",'w') as out:
#         csv_out=csv.writer(out)
#         for row in frequencies:
#             csv_out.writerow([str(row)[2:str(row).__len__() - 3], str(frequencies[row])])
#
#     with open("csv's/bigram.csv",'w') as out:
#         csv_out=csv.writer(out)
#         for row in freq_bi:
#             element = str(row)[2:str(row).__len__()-2].split("', '")
#             csv_out.writerow([element[0], element[1], str(freq_bi[row])])
#
#     with open("csv's/trigram.csv",'w') as out:
#         csv_out=csv.writer(out)
#         for row in freq_tr:
#             element = str(row)[2:str(row).__len__()-2].split("', '")
#             csv_out.writerow([element[0], element[1], element[2], str(freq_tr[row])])
#
#     with open("csv's/fourgram.csv",'w') as out:
#         csv_out=csv.writer(out)
#         for row in freq_fo:
#             element = str(row)[2:str(row).__len__()-2].split("', '")
#             csv_out.writerow([element[0], element[1], element[2], element[3], str(freq_fo[row])])
#
#     with open("csv's/fivegram.csv",'w') as out:
#         csv_out=csv.writer(out)
#         for row in freq_fi:
#             element = str(row)[2:str(row).__len__()-2].split("', '")
#             csv_out.writerow([element[0], element[1], element[2], element[3], element[4], str(freq_fi[row])])


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



def checkSentenceUni(sentence, size, ref, ref_tot):
    trueWord = ref
    totalNumberOfWords = ref_tot


    for a in range(0, size):

        bestSuite = {}
        checkWord = sentence.split(' ')[a]
        bestSuite[checkWord] = []


        for i in trueWord.keys():
            word = i
            if checkWord in trueWord:
                bestSuite.pop(checkWord)
                break
            if (edit_distance(word, checkWord) == 1) and not (checkWord in trueWord):
                bestSuite[checkWord].append({word: int(trueWord[i])})

        # for a in bestSuite:
        #     for l in bestSuite[a]:
        #         for s in l:
        #             print(a)
        #             print(bestSuite[a])
        #             print(l)
        #             print(s)
        #             print(l[s])
        #     if checkWord.lower() != a.lower():
        #         for corrs in bestSuite[a]:
        #             for w in corrs.keys():
        #                 print(str(checkWord) + " ---> " + str(w) + " " + str(corrs[w] / totalNumberOfWords))

        for key in bestSuite:
            if (key == ''):
                break
            for dic_in_list in bestSuite[key]:
                for kay in dic_in_list:
                    print(str(key) + " ---> " + str(kay) + " " + str(dic_in_list[kay] / totalNumberOfWords))

    return

def checkSentenceBi(sentence, size, ref, ref_tot):
    trueWord = ref
    totalNumberOfWords = ref_tot


    for a in range(0, size-1):
        bestSuite = {}
        checkWord1 = sentence.split(' ')[a]
        checkWord2 = sentence.split(' ')[a+1]
        checkWord = checkWord1 + ' ' + checkWord2
        bestSuite[checkWord] = []

        for i in trueWord.keys():
            word = i
            if checkWord in trueWord:
                bestSuite.pop(checkWord)
                break
            if (edit_distance(word, checkWord) <= 3) and (edit_distance(word, checkWord) > 1) and (not checkWord in trueWord):
                bestSuite[checkWord].append({word: int(trueWord[i])})

        for key in bestSuite:
            if(key == ''):
                break
            for dic_in_list in bestSuite[key]:
                for kay in dic_in_list:
                    print(str(key) + " ---> " + str(kay) + " " + str(dic_in_list[kay] / totalNumberOfWords))
    return

def checkSentenceTri(sentence, size, ref, ref_tot):
    trueWord = ref
    totalNumberOfWords = ref_tot

    for a in range(0, size - 2):
        bestSuite = {}
        checkWord1 = sentence.split(' ')[a]
        checkWord2 = sentence.split(' ')[a + 1]
        checkWord3 = sentence.split(' ')[a + 2]
        checkWord = checkWord1 + ' ' + checkWord2 + ' ' + checkWord3
        bestSuite[checkWord] = []


        for i in trueWord.keys():
            word = i
            if checkWord in trueWord:
                bestSuite.pop(checkWord)
                break
            if (edit_distance(word, checkWord) <= 5) and (edit_distance(word, checkWord) > 2) and (
            not checkWord in trueWord):
                bestSuite[checkWord].append({word: int(trueWord[i])})

        for key in bestSuite:
            if (key == ''):
                break
            for dic_in_list in bestSuite[key]:
                for kay in dic_in_list:
                    print(str(key) + " ---> " + str(kay) + " " + str(dic_in_list[kay] / totalNumberOfWords))
    return



def checkSentences(text, ar1, ar2, ar3, tot1, tot2, tot3):
    sentences = text.split('.')
    print(sentences)
    for sentence in sentences:
        size = sentence.__len__()

        checkSentenceUni(sentence, sentence.split(' ').__len__(), ar1, tot1)
        checkSentenceBi(sentence, sentence.split(' ').__len__(), ar2, tot2)
        checkSentenceTri(sentence, sentence.split(' ').__len__(), ar3, tot3)  # Processing speed is decreasing

    return


def prepArrs(ar1, ar2, ar3, tots):
    cursor.execute('''SELECT * FROM unigram''')
    all_rows_uni = cursor.fetchall()
    for l in all_rows_uni:

        word = l[0]
        occur = l[1]
        if word != "" and occur != "":
            if not '.' in word and not ',' in word and not '<s>' in word and not'<f>' in word and not ':' in word:
                ar1[word] = occur
                tots[0] += occur


    cursor.execute('''SELECT * FROM bigram''')
    all_rows_bi = cursor.fetchall()
    for l in all_rows_bi:
        word = l[0] + ' ' + l[1]
        occur = l[2]
        if word != "" and occur != "":
            if not '.' in word and not ',' in word and not '<s>' in word and not'<f>' in word and not ':' in word:
                ar2[word] = occur
                tots[1] += occur


    cursor.execute('''SELECT * FROM trigram''')
    all_rows_tri = cursor.fetchall()
    for l in all_rows_tri:
        word = l[0] + ' ' + l[1] + ' ' + l[2]
        occur = l[3]
        if word != "" and occur == "":
            if not '.' in word and not ',' in word and not '<s>' in word and not'<f>' in word and not ':' in word:
                ar3[word] = occur
                tots[2] += occur


true_word1 = {}
true_word2 = {}
true_word3 = {}
totals = []
totals.append(0)
totals.append(0)
totals.append(0)
prepArrs(true_word1, true_word2, true_word3, totals)
print(true_word1)
print(true_word2)
print(true_word3)
userWord = input('Enter your sentence: ')



checkSentences(userWord, true_word1, true_word2, true_word3, totals[0], totals[1], totals[2])
db.close()


