set={
    "Amit":15,
    "Ani":45,
    "Sid":25,
    "Soub":35

    }
# print(set.items())
# print(set.keys())
# print(set.values())
# set.update({"soub":40})
# set.update({"Moon":50})
# print(set)
print(set.get("Soub"))  #it return the none value if the name doesn't exist
print(set["Soub"])  #it return error if the name is not exist