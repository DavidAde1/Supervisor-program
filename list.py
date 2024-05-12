my_list = ["January", "February", "March"]

# Print function will print March from the list above
print(my_list[1])

# append function adds April the list making it 4 elements in the list
my_list.append("April")
print(my_list[2])

#prints the element in the last position of current list 
print(my_list[-1])

#insert function adds May to the index position of 3 in the list
my_list.insert(3, "May")
print(my_list)

#remove the last element in the list with pop
my_list.pop(4)
print(my_list)
