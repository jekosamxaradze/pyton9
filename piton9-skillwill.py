# list


my_list_int = [1, 2, 3, 4, 5]
my_list_str = ["a", "b", "c", "d"]
my_list_mix = my_list_int + my_list_str
print(my_list_int[1:4:2])
my_list_int.append(7)
my_list_int.remove (3)

for number in my_list_int:
    print(number)

print(my_list_int)
print(hex(id(my_list_mix)))
print(my_list_mix)
print(type(my_list_mix))

  

# tuple

my_list = [5, 6, 7, 8]
my_tuple = (1, 2, 3)
my_tuple_two = tuple(my_list)
print(type(my_list))



# dictionary

my_dict = {
    "car_one" : "bmw",
    "car_two" : "mersedes"
}

my_dict.update({"car_three": "audi"})
print(type(my_dict))
print(my_dict)
print(my_dict["car_one"])
print(my_dict.get("car_two"))
print(hex(id(my_dict)))