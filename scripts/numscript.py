import numpy as np

# Create numpy arrays, list and change elements

a=np.array([1,2,3]) # create a 1D array
print('Dimensions of the array = ',a.ndim) # print the dimensions of the array
print('Shape of the array = ', a.shape) # print the shape of the array
a=np.array([ [1,2,3] ])
print('Dimensions of the array = ', a.ndim) # print the dimensions of the array
print('Shape of the array = ', a.shape) # print the shape of the array

b = np.array([[1,2,3],[4,5,6]])   # Create a rank 2 array
print('Shape of the array = ',b.shape)                     # Prints "(2, 3)"
print('Print select elements of b array')
print(b[0, 0], b[0, 1], b[1, 0])   # Prints "1 2 4"
print(b[0][0], b[0][1], b[0][1])   # Prints "1 2 4"
print('Modify array elements in location 0,2')
b[0,2]=999
print('New value in b[0,2] = ', b[0,2])  # [[  1   2   3]
 				         # [  4   5 999]]
print('New b array = ')
print(b)
print()
print('Create an array of zeros')
a = np.zeros((2,2))  # Create an array of all zeros
print(a)             # Prints "[[ 0.  0.]
                     #          [ 0.  0.]]"
    
print()
print('Create an array of ones')
b = np.ones((1,2))   # Create an array of all ones
print(b)             # Prints "[[ 1.  1.]]"
print()
print('Create an identity matrix')
d = np.eye(2)        # Create a 2x2 identity matrix
print(d)              # Prints "[[ 1.  0.]
                     #          [ 0.  1.]]"
print()
print('Create a random 2x2 array')
e = np.random.random((2,2)) # Create an array filled with random values
print(e)                     # Might print "[[ 0.91940167  0.08143941]
                            #               [ 0.68744134  0.87236687]]"
print()
print('Create a 1D random integer array between 10-100')
e = np.random.random_integers(10,100,10) # print 10 random integers between 10 to 100
print(e)
print()
print('Create a 10x10 random integer array between 10-100')
e = np.random.random_integers(10,100,(10,10)) # print 100 random integers and place them in 10x10 array
print(e) 
print()
wait = input("PRESS ENTER TO CONTINUE.")

#Slicing: Numpy arrays can be sliced. Since arrays may be multidimensional, you must specify a slice for each dimension of the array:

print('Create a 3x4 array')
a = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])
print(a)
# [[ 1  2  3  4]
#  [ 5  6  7  8]
#  [ 9 10 11 12]]
print()
print('Pull out subarray first 2 rows and columns 1-2')
# Use slicing to pull out the subarray consisting of the first 2 rows
# and columns 1 and 2; b is the following array of shape (2, 2):
b = a[:2, 1:3] # [[2 3]
               #  [6 7]]
print(b)
print()

# Modifying a slice of an array modifies the original array 
print('Modify a slice and compare to the original array')
print('Value of element 0,1 of a is',a[0, 1])   # Prints "2"
print('Modify 0,0 of array b to value 77')
b[0, 0] = 77    # b[0, 0] is the same piece of data as a[0, 1]
print('Value of element 0,1 of a is now ',a[0, 1])   # Prints "77"
print()

# Create the following rank 2 array with shape (3, 4)
# [[ 1  2  3  4]
#  [ 5  6  7  8]
#  [ 9 10 11 12]]
a = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])
print()

wait = input("PRESS ENTER TO CONTINUE.")

# Two ways of accessing the data in the middle row of the array.
# Mixing integer indexing with slices yields an array of lower rank,
# while using only slices yields an array of the same rank as the
# original array:
row_r1 = a[1, :]    # Rank 1 view of the second row of a  
row_r2 = a[1:2, :]  # Rank 2 view of the second row of a
print('Print extracted row, shape and dims = ',row_r1, row_r1.shape,row_r1.ndim)  # Prints "[5 6 7 8] (4,) 1"
print('Print extracted row, shape and dims = ',row_r2, row_r2.shape,row_r2.ndim)  # Prints "[[5 6 7 8]] (1, 4) 2"

# We can make the same distinction when accessing columns of an array:
col_r1 = a[:, 1]
col_r2 = a[:, 1:2]
print('Print extracted column = ') # Prints "[ 2  6 10]"
print(col_r1)
print('Print shape and dims of extracted column =', col_r1.shape,col_r1.ndim)  # Prints "(3,) 1"
print('Print extracted column = ') # Prints "[[ 2]
                                   #          [ 6]
                                   #          [10]] (3, 1)"
print(col_r2)
print('Print shape and dims of extracted column = ', col_r2.shape,col_r1.ndim)  # Print "(3,1) 2"


wait = input("PRESS ENTER TO CONTINUE.")

#Array indexing: 

print('Create an 4x3 integer array')
a = np.array([[1,2,3], [4,5,6], [7,8,9], [10, 11, 12]])
print('Shape of the array is =', a.shape)
print()
# Create an array of indices
print('Create 1D index array')
b = np.array([0, 2, 0, 1])
print(b)
print()

# Select one element from each row of a using the indices in b
print('Create a range of indices from 0-3 using arange = ', np.arange(4))
print('Use this range to reference indices of the a array')
print(a[np.arange(4), b])  # Prints "[ 1  6  7 11]"

# Mutate one element from each row of a using the indices in b
print('Modify the indexed elements by adding 10')
a[np.arange(4), b] += 10

print('Modified array then becomes = ',a)  # prints "array([[11,  2,  3],
         #                [ 4,  5, 16],
         #                [17,  8,  9],
         #                [10, 21, 12]])

wait = input("PRESS ENTER TO CONTINUE.")

#Reference elements by boolean masks
print('Create an 3x2 numpy array')
a = np.array([[1,2], [3, 4], [5, 6]])

print('Apply a logical mask for all elements that larger than 2')
bool_idx = (a > 2)  # Find the elements of a that are bigger than 2;
                    # this returns a numpy array of Booleans of the same
                    # shape as a, where each slot of bool_idx tells
                    # whether that element of a is > 2.
            
print(bool_idx)      # Prints "[[False False]
                    #          [ True  True]
                    #          [ True  True]]"

# We use boolean array indexing to construct a rank 1 array
# consisting of the elements of a corresponding to the True values
# of bool_idx
print('Extracted array elements where boolean condition is true = ',a[bool_idx])  # Prints "[3 4 5 6]"

# We can do all of the above in a single concise statement:
print('The boolean condition can be an input to the array')
print(a[a > 2])     # Prints "[3 4 5 6]"

wait = input("PRESS ENTER TO CONTINUE.")

#Some arithmetic
print('Create two 2x2 arrays')
x = np.array([[1,2],[3,4]], dtype=np.float64)
y = np.array([[5,6],[7,8]], dtype=np.float64)
print()
# Elementwise sum; both produce the array
# [[ 6.0  8.0]
#  [10.0 12.0]]
#print x + y
print('Add them')
print(np.add(x, y))
print()
# Elementwise difference; both produce the array
# [[-4.0 -4.0]
#  [-4.0 -4.0]]
#print x - y
print('Subtracted them')
print(np.subtract(x, y))
print()

# Elementwise product; both produce the array
# [[ 5.0 12.0]
#  [21.0 32.0]]
#print x * y
print('Multiply by elements')
print(np.multiply(x, y))
print()

# Elementwise division; both produce the array
# [[ 0.2         0.33333333]
#  [ 0.42857143  0.5       ]]
#print x / y
print('Divide by elements')
print(np.divide(x, y))

# Elementwise square root; produces the array
# [[ 1.          1.41421356]
#  [ 1.73205081  2.        ]]
print('Square root')
print(np.sqrt(x))


x = np.array([[1,2],[3,4]])
y = np.array([[5,6],[7,8]])

print()
print('Create two 1D arrays and treat them as vectors')
v = np.array([9,10])
print(v)
w = np.array([11, 12])
print(w)
print()

# Inner product of vectors; both produce 219
#print v.dot(w)
print('Inner product = ',np.dot(v, w))

# Matrix / vector product; both produce the rank 1 array [29 67]
#print x.dot(v)
print('Matrix * vector product =',np.dot(x, v))

# Matrix / matrix product; both produce the rank 2 array
# [[19 22]
#  [43 50]]
#print(x.dot(y))
print('Matrix * Matrix product')
print(np.dot(x, y))

wait = input("PRESS ENTER TO CONTINUE.")

print('Create a 2x2 array')
x = np.array([[1,2],[3,4]])
print(x)
print()
print('Sum of all elements = ',np.sum(x))  # Compute sum of all elements; prints "10"
print('Sum of all columns =',np.sum(x, axis=0))  # Compute sum of each column; prints "[4 6]"
print('Sum of all rows = ',np.sum(x, axis=1))  # Compute sum of each row; prints "[3 7]"


x = np.array([[1,2], [3,4]])
#print x    # Prints "[[1 2]
           #          [3 4]]"
print('Transpose Matrix = ',x.T)  # Prints "[[1 3]
           #          [2 4]]"
print('Transpose Matrix (alt)= ',np.transpose(x)) # transpose matrix x using transpose

wait = input("PRESS ENTER TO CONTINUE.")

# We will add the vector v to each row of the matrix x,
# storing the result in the matrix y
print('Create a 4x3 array')
x = np.array([[1,2,3], [4,5,6], [7,8,9], [10, 11, 12]])
print(x)
print()
print('Create a vector with the same number of row elements')
v = np.array([1, 0, 1])
print(v)
print()
print('Create an empty matrix with the same shape as x')
y = np.empty_like(x)   # Create an empty matrix with the same shape as x
print(y)
print()

# Add the vector v to each row of the matrix x with an explicit loop
print('Add the vector to each extracted row i x[i,:]')
for i in range(4):
    y[i, :] = x[i, :] + v

# Now y is the following
# [[ 2  2  4]
#  [ 5  5  7]
#  [ 8  8 10]
#  [11 11 13]]
print('Modified array')
print(y)
print()

wait = input("PRESS ENTER TO CONTINUE.")

print('Add vector to all matrix rows using tile')
# We will add the vector v to each row of the matrix x,
# storing the result in the matrix y
x = np.array([[1,2,3], [4,5,6], [7,8,9], [10, 11, 12]])
print('1D vector - same number of elements as the row elements of the target array')
v = np.array([1, 0, 1])
print(v)
print('tile the vector - replicate the vector 4 times and stack it to form an array')
vv = np.tile(v, (4, 1))  # Stack 4 copies of v on top of each other
print(vv)                 # Prints "[[1 0 1]
                         #          [1 0 1]
                         #          [1 0 1]
                         #          [1 0 1]]"
print('tiled vector can directly added to matrix')
y = x + vv  # Add x and vv elementwise
print(y)  # Prints "[[ 2  2  4
         #          [ 5  5  7]
         #          [ 8  8 10]
         #          [11 11 13]]"


wait = input("PRESS ENTER TO CONTINUE.")

print('Compute outer product of vectors')
print('Create vector 1x3 and vector 1x2')
v = np.array([1,2,3])  # v has shape (3,)
w = np.array([4,5])    # w has shape (2,)
print(v)
print(w)
print()


# To compute an outer product, we first reshape v to be a column
# vector of shape (3, 1); we can then broadcast it against w to yield
# an output of shape (3, 2), which is the outer product of v and w:
# [[ 4  5]
#  [ 8 10]
#  [12 15]]
print('Compute outer/tensor product v^T.w')
print('reshape vector v = ')
print(np.reshape(v,(3,1)))
print('Directly multiply 3x1 to 1x2 vectors to yield 3x2 matrix')
print(np.reshape(v, (3, 1)) * w)

wait = input("PRESS ENTER TO CONTINUE.")


print('Add a vector to each column of a matrix')
print('Create a 2x3 matrix')
x = np.array([[1,2,3], [4,5,6]])
print(x)
print()
print('Create a 1x2 vector')
w = np.array([4,5])
print(w)
print()
# x has shape (2, 3) and w has shape (2,).
# If we transpose x then it has shape (3, 2) and can be broadcast
# against w to yield a result of shape (3, 2); transposing this result
# yields the final result of shape (2, 3) which is the matrix x with
# the vector w added to each column. Gives the following matrix:
# [[ 5  6  7]
#  [ 9 10 11]]
print('Transpose x')
print(x.T)
print()
print('We can add the 1x2 vector')
print(x.T+w)
print()
print('We can transpose the 3x2 matrix back to 2x3') 
print((x.T + w).T)
print()
