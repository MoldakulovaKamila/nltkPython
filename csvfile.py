import  csv
f= open("/home/kamila/Desktop/outputs/output.txt")

data = f.read()



with open('file.csv','w') as out:
    writer=csv.writer(out,csv.QUOTE_NONE)
    writer.writerow(data)





