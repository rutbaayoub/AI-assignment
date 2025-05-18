# creating a dictionary of 10 elements and deleting item using popitems() funtions
new_dictionary = {
    "K" : 11 ,
    "L" : 12 ,
    "M" : 13 , 
    'N' : 14 , 
    "O" : 15 ,
    "P" : 16 ,
    "Q" : 17 ,
    "R" : 18 ,
    "S" : 19 ,
    "T" : 20 
}

print("Original Dictionary:")
print(new_dictionary)

removed_item = new_dictionary.popitem()

print( "\nDictionary after using popitem():" )
print(new_dictionary)

print( "\nRemoved item:" )
print(removed_item)