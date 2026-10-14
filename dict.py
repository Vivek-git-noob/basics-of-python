dict={
    "name":"Vivek kumar",
    "age":22,
    "college":"Bit mesra",
    "hobbies":["gym","music","movies","content"],
    "is_adult":True,
    "CGPA":7.1,
}
# DICTIONARY METHODS
print(dict.keys())
print(len(dict.keys()))
print(dict.values())
print(dict.items())
print(dict.get("hobbies"))
new_dict={
    "virat":100,
    "hope":100,
}
dict.update({"city":"asansol"})
dict.update(new_dict)
print(dict)





# null_dict={}

# print(type(dict))
# print(dict["hobbies"])
# dict["CGPA"]=7.4
# print(dict["CGPA"])
# dict["name"]="xhoot paglu"   # overwrites the values
# dict["gender"]="male"        # adding new value
# print(dict)
# print(null_dict)


# NESTED DICTIONARY
# student={
#     "name":"Vivek kumar",
#     "marks":{
#         "phy":67,
#         "maths":57,
#         "chem":50,
#         "eng":54,
#     }
# }
# print(student)
# print(student["name"])
# print(student["marks"])
# print(student["marks"]["phy"])