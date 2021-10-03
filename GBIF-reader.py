import csv 

Perdita = []

bbsl_count = 0
source_of_us_bees = {}
all_genera = {}

with open(r'C:\Users\zport\Downloads\0058082-200221144449610/0058082-200221144449610.csv', "r", encoding='utf-8') as csv_file:
    #csv_reader = csv.reader(csv_file, delimiter=',')
    csv_reader = csv.reader(csv_file, delimiter='\t', quoting=csv.QUOTE_NONE)
    
    i = 0

    for row in csv_reader:
        
        # count number of bbsl records
        if row[37] == "BBSL":
            bbsl_count = bbsl_count + 1
            
            
        # find sourca of bees from US   
        if row[15] == "US":
            if row[7] == "Apidae" or row[7] == "Andrenidae" or row[7] == "Megachilidae" or row[7] == "Halictidae" or row[7] == "Colletidae" or row[7] == "Melittidae": #only bees
                if row[11] == "SPECIES": # only if ID'd to species
                    #if int(row[32]) > 2005 and int(row[32]) < 2016: # only bees in the 2006-2015 timeperiod
                    if int(row[32]) > 1950 and int(row[32]) < 1991: # only bees in the 1950-1990 timeperiod
                        if row[37] not in source_of_us_bees: 
                            source_of_us_bees[row[37]] = 1
                        else: # it's already in
                            source_of_us_bees[row[37]] += 1
        
        #if row[8]=="Capicola":
        if row[7]=="Melittidae":
        #if "Perdita" in row[12]:
            Perdita += [row]
        if row[8] not in all_genera:
            all_genera[row[8]] = 1
        else:
            all_genera[row[8]] += 1
        i = i + 1
        #if i == 10000:
        if i%10000 ==0:
            print(i)
            
        #    break
        

        
"""
print (all_genera)
with open('all_genera.csv','w', newline='') as result_file:
    wr = csv.writer(result_file, dialect='excel')
    for item in all_genera:
        wr.writerow([item, all_genera[item]])
"""
    
with open('Melittidae.csv','w', newline='', encoding='utf-8') as result_file:
    wr = csv.writer(result_file, dialect='excel')
    for row in Perdita:
        wr.writerow(row)
        
        
print ("total bbsl count", bbsl_count)
print ("source of US bees", source_of_us_bees)