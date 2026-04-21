info = {
    "name" : "srinivas",
    "cgpa" : 7.1,
    "subjects" : ["maths","science"],
    3.14 : "PI"
}
print(info)

print(info["subjects"])
print(info[3.14])

#updating the value
info["cgpa"] = 6.4
print(info)

#printing the all keys
print(info.keys())
print(list(info.keys())) #converting into list

#printing the values
print(info.values())

#returns key value pairs
print(info.items())

#we can access key values via get function
'''info["cgpa2"]    #we will get error
print("the code was completed")  #it wont run
'''

info.get("cgpa2")    #we wont get error
print("the code was completed")  #it wont run

#adding new item to dictionary
info.update({
    "city" : "delhi"
})
print(info)