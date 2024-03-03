grocery_item = ""
grocery_list = []
while grocery_item != "done":
     grocery_item = input("Please enter grocery item to add in list: when you done with writing simply write:done")
     if grocery_item == "done":
         continue
     else:
         print("adding item into list")
         grocery_list.append(grocery_item)
print("here is your grocery list")
print(grocery_list)
print()

