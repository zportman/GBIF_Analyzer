import csv 

Perdita = []

Perdita_species = set([])
Perdita_species_1950_1990 = set([])
Perdita_species_2006_2015 = set([])
Perdita_species_after_1990 = set([])

Perdita_identifiers = {}
Perdita_lastseen = {}

with open(r'Perdita.csv', "r", encoding="utf8") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    
    
    for row in csv_reader:
        Perdita += [row]    
        
        #row = row[0].split(',')
        #print(row)
        #if len(row) > 9:
        
        if row[9] == "": # skip if the species is blank
            continue
        
        Perdita_species.add(row[9])
        
        #print(row[32])
        year = int(row[32])# year is slot 32

        #if year > 1950 and year < 1990:
        if 1950 < year < 1990:
        #if 1950 < year:
        #if year in range(1950, 1990):
            Perdita_species_1950_1990.add(row[9])
        
        if 2005 < year < 2016:    
        #if year > 2005 and year < 2016:
        #if year in range (2005, 2015):
            Perdita_species_2006_2015.add(row[9])
            
        if year > 1990:
            Perdita_species_after_1990.add(row[9])
            
            
        #here we look at how many different identifiers there are for each species. 
        if row[9] not in Perdita_identifiers:
            Perdita_identifiers[row[9]] = [row[40]]
            Perdita_lastseen[row[9]] = [row[32]]
        else: #species is already in
            if row[40] not in Perdita_identifiers[row[9]]:
                Perdita_identifiers[row[9]].append(row[40])
            if row[31] != "" and int(row[32]) > int(Perdita_lastseen[row[9]][0]):
                Perdita_lastseen[row[9]]=([row[32]])
                

            
print(Perdita_species)
print(len(Perdita_species))


print ("Perdita_species_1950_1990" , Perdita_species_1950_1990)
print(len(Perdita_species_1950_1990))
        
print ("Perdita_species_2006_2015" , Perdita_species_2006_2015)
print(len(Perdita_species_2006_2015))
                
print ("Perdita species after 1990", Perdita_species_after_1990)
print(len(Perdita_species_after_1990))

list1950 = sorted(Perdita_species_1950_1990)
#for row in list1950:
#    print(row)

print("species found 1950-1990 but not after 1990:", len (Perdita_species_1950_1990 - Perdita_species_after_1990), Perdita_species_1950_1990 - Perdita_species_after_1990)

print("species found after 1990 but not 1950-1990:", len(Perdita_species_after_1990 - Perdita_species_1950_1990),Perdita_species_after_1990 - Perdita_species_1950_1990)

print("species found in BOTH 1950-1990 AND after 1990", len(Perdita_species_1950_1990.intersection(Perdita_species_after_1990)), Perdita_species_1950_1990.intersection(Perdita_species_after_1990))

print("species found 1950-1990 but not 2006-2015:", len(Perdita_species_1950_1990- Perdita_species_2006_2015),Perdita_species_1950_1990- Perdita_species_2006_2015)


print (Perdita_identifiers)


for species in Perdita_identifiers:
    if len(Perdita_identifiers[species] )<5:
        print (species, Perdita_identifiers[species])
        
for species in Perdita_lastseen:
    if len(Perdita_identifiers[species] )<3:
        print (species, Perdita_lastseen[species])