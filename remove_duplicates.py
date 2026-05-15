# Function to remove duplicates from list
"""Function with parameter original_list from which duplicates will be removed."""
"""The below code runs with linear time complexity of O(n)"""
	# dict.fromkeys() creates a dictionary with list items as keys.
    # Since dict keys must be unique, duplicates are automatically removed.
    # list() then converts those unique keys back into a list.
def remove_duplicates(original_lst):
	return list(dict.fromkeys(original_list))
					
def list_data():
		user_input = list(map(int, input("Enter the data: ").strip(",")))
		return user_input

if __name__ == "__main__":
		print(remove_duplicates(list_data()))

		
