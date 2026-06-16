my_dict = {
    "name": "Abhishek",
     "age":25,
     "city":"faridabad"
}

# d.keys() -> return all keys
print(my_dict.keys())

# d.values() -> return all values
print(my_dict.values())

# d.items() -> return key,value pair
print(my_dict.items())

# d.get(val) -> return value according to key
print(my_dict.get("age"))

# d.update(new_item) -> add new item 
my_dict.update({
    "degree":"mca"
})
print(my_dict)