string = 'azcbobohegbegghakl'

def longest_alphab(string):

	longest_str = ""
	current_str = ""
	
	for letter in string:
		if current_str == "": current_str = letter
		if letter >= current_str[-1]:
			current_str += letter
		else:
			if len(current_str) > len(longest_str):
				longest_str = current_str
	
			current_str = letter	
	
	if len(current_str) > len(longest_str):
		longest_str = current_str
	
	return longest_str
	
print longest_alphab(string)	
