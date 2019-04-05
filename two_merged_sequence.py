# Function to print strictly Increasing and
# Strictly Decreasing sequence if possible
def Find_Sequence(array,n):

	# Arrays to store strictly Increasing and
	# Decreasing sequence 
	inc_arr,dec_arr=[],[]

	# Initializing last element of both sequence
	inc, dec = -1, 1e7

	# Iterating through the array
	for i in range(n):

		# If current element can be appended to both the sequences
		if inc < array[i] < dec:

			# If next element is greater than current element 
			# Then append it to the strictly increasing array 
			if array[i] < array[i + 1]:
				inc = array[i]
				inc_arr.append(array[i])

			# Otherwise append it to strictly decreasing one
			else:
				dec = array[i]
				dec_arr.append(array[i])

		# If current element can be appended to increasing sequence only
		elif inc < array[i]:
			inc = array[i]
			inc_arr.append(array[i])

		# If current element can be appended to decreasing sequence only
		elif dec > array[i]:
			dec = array[i]
			dec_arr.append(array[i])

		# Else we can not make two such sequence from the given array
		else:
			print('NO')
			break

	# Print strictly increasing and strictly decreasing sequence
	else:
		print('YES')
		print(inc_arr,dec_arr)

# Driver Code
if __name__=="__main__":
	n=9
	array=[5,1,3,6,8,2,9,0,10] + [0, ]
	Find_Sequence(array,n)