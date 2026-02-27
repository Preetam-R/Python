#dictionaries

info = {
    "name" : "Preetam",
    "Age" : 19,
    "fav color" : "Blue"
}

print(info["name"])  #to get particular values from dictionary
print(info["Age"])

#Dictionaries can be nested like

clg = {
    "Name" : "Preetam",
    "Subject" : {
        "DDCO" : 99,
        "OS" : 89,
        "Python" : 90,
        "DSA" : 97
    }
}

#to Access this just type
print(clg["Subject"])

#if you want to access particular key in nested dictionary 
print(clg["Subject"]["DDCO"])

#methods of Dictionaries

print(clg.keys()) #returns outer layer of keys
print(info.keys())

print(clg.items()) #returns key:value in pairs 
print(info.items())

#we can update are value using update method

new_dict = {
    "name" : "Rupasing",
    "Age": 52
}                               #upadte the dictionaries like this 

info.update(new_dict)

print(info)

#from list we can create keys 
#lets assume the lst

lst = [1,2,3,4]
d = dict.fromkeys(lst)
print(d)

#in the same way value can also be assigned 
#but its default will be set for all

d = dict.fromkeys(lst,10)
print(d)
