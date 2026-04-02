import numpy as np

def array_operations(A, B):

	arrA = np.array(A)
	arrB = np.array(B)

	# Arithmetic Operations
	sum_result = arrA + arrB
	diff_result = arrA - arrB
	prod_result = arrA * arrB

	# Statistical Operations
	mean_A = np.mean(arrA)
	median_A = np.median(arrA)
	std_dev_A = np.std(arrA)

	# Bitwise Operations
	and_result = arrA & arrB
	or_result = arrA | arrB
	xor_result = arrA ^ arrB

    # Output results with one space between each element
	print("Element-wise Sum:", ' '.join(map(str, sum_result)))
	print("Element-wise Difference:", ' '.join(map(str, diff_result)))
	print("Element-wise Product:", ' '.join(map(str, prod_result)))
    
	print(f"Mean of A: {mean_A}")
	print(f"Median of A: {median_A}")
	print(f"Standard Deviation of A: {std_dev_A}")
    
	print("Bitwise AND:", ' '.join(map(str, and_result)))
	print("Bitwise OR:", ' '.join(map(str, or_result)))
	print("Bitwise XOR:", ' '.join(map(str, xor_result)))

A = list(map(int, input().split()))  
B = list(map(int, input().split()))  
array_operations(A, B)
