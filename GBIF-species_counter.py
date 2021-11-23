import csv 

Perdita = []

source_of_us_bees = {}
all_genera = {}

i = 0
total_bee_records = 0
total_bee_records_to_species = 0
total_us_bee_records = 0
total_us_bee_records_to_species = 0


#set up some dictionaries to coutn years for the top 4 sources because I don't know how to use pandas
j = 1951

USGS = {}
BBSL = {}
SEMC= {}
IC = {}
while j < 2021:
    USGS[j] = []
    BBSL[j] = []
    SEMC[j] = []
    IC[j] = [] 
    j = j + 1

USGS_species = []
USGS_species_pre_2000 = []
USGS_species_post_2000 = []
BBSL_species = []
BBSL_species_pre_2000 = []
BBSL_species_post_2000 = []
SEMC_species = []
SEMC_species_pre_2000 = []
SEMC_species_post_2000 = []
IC_species = []
IC_species_pre_2000 = []
IC_species_post_2000 = []
BBSL_SEMC_IC_species_pre_2000 =[]
BBSL_SEMC_IC_species_post_2000 =[]

USGS_Utah = []
BBSL_Utah = []


with open(r'0058082-200221144449610/0058082-200221144449610.csv', "r", encoding='utf-8') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter='\t', quoting=csv.QUOTE_NONE)
    for row in csv_reader:

        #1. How many bees are in the entire dataset?
        if row[7] == "Apidae" or row[7] == "Andrenidae" or row[7] == "Megachilidae" or row[7] == "Halictidae" or row[7] == "Colletidae" or row[7] == "Melittidae": #only bees
            total_bee_records += 1 
                        
            #2. How many bees in the entire dataset are identified to species level?           
            if row[11] == "SPECIES": # only if ID'd to species
                total_bee_records_to_species += 1
                
            #3. How many bee records are from the US?
            if row[15] == "US":
                total_us_bee_records += 1
                
    
                #here we set up the source of US bees data structures. I'm doing a dumb dictionary of institutions, with a list that will hold different
                # things so that it can just be made into a nice table at the end. There's def a better way to do that, but oh well. 
                if row[37] not in source_of_us_bees: 
                    source_of_us_bees[row[37]] = [1, 0, 0, 0] #slot 0: total records, slot 1: total records to species, slot 2: historic to species, slot 3: recent to species
                else: # it's already in
                    source_of_us_bees[row[37]][0] += 1                
                
                    
                    #4. How many bee records from the US are identified to species?
                    if row[11] == "SPECIES": # only if ID'd to species
                        total_us_bee_records_to_species += 1   
                        
                        # add ID'd to species to istitutions slot 1
                        source_of_us_bees[row[37]][1] += 1   
                        
         
                        # doing 2 things here, adding counts per year to the top 4 museums and also reating a full species list.    
                        ##if int(row[32]) > 1950 and row[17] == "California":
                        if int(row[32]) > 1950:
                            if row[37] == "USGS PWRC - Native Bee Inventory and Monitoring Lab (BIML)":
                                #USGS[int(row[32])] += 1
                                if row[9] not in USGS[int(row[32])]:
                                    USGS[int(row[32])].append(row[9])
                                if row[9] not in USGS_Utah:
                                    USGS_Utah.append(row[9])
                            ##elif row[37] == "BBSL":
                            elif row[37] == "BBSL" or row[37] == "SEMC" or row[37] == "Insect Collection":
                                #BBSL[int(row[32])] += 1
                                if row[9] not in BBSL[int(row[32])]:
                                    BBSL[int(row[32])].append(row[9])
                                if row[9] not in BBSL_Utah:
                                    BBSL_Utah.append(row[9])
                                    
                            """
                            elif row[37] == "SEMC":
                                #SEMC[int(row[32])] += 1
                                if row[9] not in SEMC[int(row[32])]:
                                    SEMC[int(row[32])].append(row[9])                                
                            elif row[37] == "Insect Collection":
                                #IC[int(row[32])] += 1
                                if row[9] not in IC[int(row[32])]:
                                    IC[int(row[32])].append(row[9])                                
                            """
        

        
        if row[8]=="Perdita": # extract a given genus
        #if row[7]=="Melittidae": # extract a given family
        #if row[37] == "USGS PWRC - Native Bee Inventory and Monitoring Lab (BIML)": #extracting all records from a given data source
        #if "Perdita" in row[12]:
            Perdita += [row]
        if row[8] not in all_genera:
            all_genera[row[8]] = 1
        else:
            all_genera[row[8]] += 1
        i = i + 1

        #output so I know it hasn't frozen cuz this script is slow as shit and I don't know what optimization is. 9170000 is the last number output.
        if i%10000 ==0:
            print(i)
                    

        
"""
print (all_genera)
with open('all_genera.csv','w', newline='') as result_file:
    wr = csv.writer(result_file, dialect='excel')
    for item in all_genera:
        wr.writerow([item, all_genera[item]])
"""

"""
# This part creates the output file that can be plugged into GBIF-analyzer.py    
with open('Melittidae.csv','w', newline='', encoding='utf-8') as result_file:
    wr = csv.writer(result_file, dialect='excel')
    for row in Perdita:
        wr.writerow(row)
"""
        
# This is the output for the data sources. col1: source, col2: total records, col3: total records to species, col4: historic to species, col5: recent to species        
with open('data_sources.csv','w', newline='', encoding='utf-8') as result_file:
    wr = csv.writer(result_file, dialect='excel')
    for thingy in source_of_us_bees:
        wr.writerow([thingy] + source_of_us_bees[thingy])
        
        
#here output the data per year for the top 4 collection sources

with open('number_species_per_data_sources_by_year.csv','w', newline='', encoding='utf-8') as result_file:
    wr = csv.writer(result_file, dialect='excel')
    j = 1951
    
    while j < 2021:
        
        ##temp using IC as the union of USGS and BBSL combine
        IC[j] =   list( set(USGS[j]) & set(BBSL[j]))
        
        #list(set().union(USGS[j], BBSL[j]))
        
        wr.writerow([j] + [len(USGS[j])] + [len(BBSL[j])] + [len(SEMC[j])] + [len(IC[j])])
        j = j + 1
        
        
        

print ("1. Total number of bees in dataset:", total_bee_records)
print ("2. Total number of bees in dataset identified to species:", total_bee_records_to_species)
print ("3. Total number of bee records from the US:", total_us_bee_records)
print ("4. Total number of US bee records identified to species:", total_us_bee_records_to_species)

        
print ("source of US bees", source_of_us_bees)


print ("USGS Utah,", len(USGS_Utah))
print ("BBSL Utah,",len(BBSL_Utah))