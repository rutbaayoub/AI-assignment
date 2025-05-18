# using for loop and keys() function to access keys in dictionary 
weekly_schedule = {
    "Monday" : "Physics" ,
    "Tuesday" : "Organic chemistry" ,
    "Wednesday" : "Physical chemistry" ,
    "Thursday" : "Information practices" ,
    "Friday" : "Maths"
}
print( "Days in Weekly Schedule:" )
for key in weekly_schedule.keys():
     print(key)