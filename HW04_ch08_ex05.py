# Structure this script entirely on your own.
# See Chapter 8: Strings Exercise 5 for the task.
# Please do provide function calls that test/demonstrate your
# function.


def cypher(s,c):
	code='' 										#Initialising the final encrypted code
	for i in range(len(s)):		
		new_char_num = ord(s[i]) + c % 26 			#c % 26 because 'z' shifted 26 times should be 'z' itself
		if 65 <= ord(s[i]) <= 90:					# For capital letters		
			if  new_char_num > 90: 					# For letters going being 'Z'
				new_char = chr(new_char_num - 26) 	# To reset the capital letters going beyond limit to capital letters itself
			else: 	
				new_char = chr(new_char_num)
		else:										# Similar logic for small letters
			if  new_char_num > 122:					
				new_char = chr(new_char_num - 26)
			else: 	
				new_char = chr(new_char_num)
		code = code + new_char						#Concatenating letter by letter
	return code
		


def main():
	print(cypher("A",3))
	print(cypher("Z",27))
	print(cypher("z",25))
	print(cypher("AB",-1))
	print(cypher("AB",3))
	print(cypher("Cheer", 7))
	print(cypher("Melon",-10))
	print(cypher("IBM",-1))


if __name__ == '__main__':
    main()
