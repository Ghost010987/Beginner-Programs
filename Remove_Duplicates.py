# Function to remove duplicates from a mixed data list.

def remove_duplicates(original_lst):
    new_lst = []
    for items in original_lst:
        if items not in new_lst:
            new_lst.append(items)
    return new_lst

# This below function is for user to input mixed data in the original list.

def list_data():
    raw_input = input("Enter the data: ") # This line will include data as strings only.
    result = []
# The below condition is to include integres as well.
    for items in raw_input:
        items = items.strip()
        try:
            items = int(items) # If the items in the list is numbers 
        except ValueError:
            pass               # Exception handeling to ignore the error. 
        result.append(items)   # Add the numbers data in the list as well.

    return result              # Finally the data will be returned with both int and str. 

if __name__ == "__main__":
    print(remove_duplicates(list_data())) 

