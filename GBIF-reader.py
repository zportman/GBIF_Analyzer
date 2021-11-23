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
    USGS[j] = 0
    BBSL[j] = 0
    SEMC[j] = 0
    IC[j] = 0 
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
            #if row[15] == "US" and row[17] == "Utah": # alternate if statement to use to choose a specific state
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
                        
                        if int(row[32]) > 1950 and int(row[32]) < 2001: # only bees in the 1950-2000 timeperiod, which goes in slot 2  
                            source_of_us_bees[row[37]][2] += 1 
                            
                            # count number of speices pre 2000
                            if row[37] == "USGS PWRC - Native Bee Inventory and Monitoring Lab (BIML)":
                                if row[9] not in USGS_species_pre_2000:
                                    USGS_species_pre_2000.append(row[9])
                            
                            elif row[37] == "BBSL":  
                                if row[9] not in BBSL_species_pre_2000:
                                    BBSL_species_pre_2000.append(row[9])
                                    if row[9] not in BBSL_SEMC_IC_species_pre_2000:
                                        BBSL_SEMC_IC_species_pre_2000.append(row[9])                                         
                                    
                            elif row[37] == "SEMC":
                                if row[9] not in SEMC_species_pre_2000:
                                    SEMC_species_pre_2000.append(row[9]) 
                                    if row[9] not in BBSL_SEMC_IC_species_pre_2000:
                                    
                                        BBSL_SEMC_IC_species_pre_2000.append(row[9])  
                                    
                            elif row[37] == "Insect Collection":
                                    
                                if row[9] not in IC_species_pre_2000:
                                    IC_species_pre_2000.append(row[9]) 
                                    if row[9] not in BBSL_SEMC_IC_species_pre_2000:
                                    
                                        BBSL_SEMC_IC_species_pre_2000.append(row[9])  
                             
                        
                        
                        
                        if int(row[32]) > 2000 and int(row[32]) < 2016: # only bees in the 2001-2015 timeperiod, which goes in slot 3
                            source_of_us_bees[row[37]][3] += 1   
                            
                            # count number of speices post 2000. I now regret deciding to add this in this way but it's too late to back out now
                            if row[37] == "USGS PWRC - Native Bee Inventory and Monitoring Lab (BIML)":
                                if row[9] not in USGS_species_post_2000:
                                    USGS_species_post_2000.append(row[9])
                            elif row[37] == "BBSL":  
                                if row[9] not in BBSL_species_post_2000:
                                    BBSL_species_post_2000.append(row[9]) 
                                    if row[9] not in BBSL_SEMC_IC_species_post_2000:
                                        BBSL_SEMC_IC_species_post_2000.append(row[9])                                
                                    
                            elif row[37] == "SEMC":
                                if row[9] not in SEMC_species_post_2000:
                                    SEMC_species_post_2000.append(row[9]) 
                                    if row[9] not in BBSL_SEMC_IC_species_post_2000:
                                        BBSL_SEMC_IC_species_post_2000.append(row[9])                              
                                     
                            elif row[37] == "Insect Collection":
                                if row[9] not in IC_species_post_2000:
                                    IC_species_post_2000.append(row[9])
                                    if row[9] not in BBSL_SEMC_IC_species_post_2000:
                                        BBSL_SEMC_IC_species_post_2000.append(row[9])                              
                                    
                                                          
                         
                        # doing 2 things here, adding counts per year to the top 4 museums and also reating a full species list.    
                        if int(row[32]) > 1950:
                            if row[37] == "USGS PWRC - Native Bee Inventory and Monitoring Lab (BIML)":
                                USGS[int(row[32])] += 1
                                if row[9] not in USGS_species:
                                    USGS_species.append(row[9])
                            elif row[37] == "BBSL":
                                BBSL[int(row[32])] += 1
                                if row[9] not in BBSL_species:
                                    BBSL_species.append(row[9])
                            elif row[37] == "SEMC":
                                SEMC[int(row[32])] += 1
                                if row[9] not in SEMC_species:
                                    SEMC_species.append(row[9])                                
                            elif row[37] == "Insect Collection":
                                IC[int(row[32])] += 1
                                if row[9] not in IC_species:
                                    IC_species.append(row[9])                                
                        
        

        
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

# This part creates the output file that can be plugged into GBIF-analyzer.py    
with open('Melittidae.csv','w', newline='', encoding='utf-8') as result_file:
    wr = csv.writer(result_file, dialect='excel')
    for row in Perdita:
        wr.writerow(row)
        
# This is the output for the data sources. col1: source, col2: total records, col3: total records to species, col4: historic to species, col5: recent to species        
with open('data_sources.csv','w', newline='', encoding='utf-8') as result_file:
    wr = csv.writer(result_file, dialect='excel')
    for thingy in source_of_us_bees:
        wr.writerow([thingy] + source_of_us_bees[thingy])
        
        
#here output the data per year for the top 4 collection sources

with open('data_sources_by_year.csv','w', newline='', encoding='utf-8') as result_file:
    wr = csv.writer(result_file, dialect='excel')
    j = 1951
    
    while j < 2021:
        wr.writerow([j] + [USGS[j]] + [BBSL[j]] + [SEMC[j]] + [IC[j]])
        j = j + 1
        
        
        

print ("1. Total number of bees in dataset:", total_bee_records)
print ("2. Total number of bees in dataset identified to species:", total_bee_records_to_species)
print ("3. Total number of bee records from the US:", total_us_bee_records)
print ("4. Total number of US bee records identified to species:", total_us_bee_records_to_species)

        
print ("source of US bees", source_of_us_bees)

print ("USGS bees", USGS_species)
print ("# USGS species", len(USGS_species))
print ("# BBSL species", len(BBSL_species))
print ("# SEMC species", len(SEMC_species))
print ("# IC species", len(IC_species))


print ("# USGS species pre 2000", len(USGS_species_pre_2000))
print ("# BBSL species pre 2000", len(BBSL_species_pre_2000))
print ("# SEMC species pre 2000", len(SEMC_species_pre_2000))
print ("# IC species pre 2000", len(IC_species_pre_2000))
print ("# BBSL SEMC IC species pre 2000", len(BBSL_SEMC_IC_species_pre_2000))


print ("# USGS species post 2000", len(USGS_species_post_2000))
print ("# BBSL species post 2000", len(BBSL_species_post_2000))
print ("# SEMC species post 2000", len(SEMC_species_post_2000))
print ("# IC species post 2000", len(IC_species_post_2000))
print ("# BBSL SEMC IC species post 2000", len(BBSL_SEMC_IC_species_post_2000))