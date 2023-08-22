# https://numpy.org/doc/stable/user/quickstart.html
import numpy as np

arr = np.arange(15).reshape(3,5)
print(arr)
print(arr.ndim)   #2
print(arr.shape)  #(3,5)
print(arr.dtype)  #int32
print(arr.itemsize)  #4 
print(arr.size)    #15
print(type(arr))   #<class 'numpy.ndarray'>

c = np.arange(24).reshape(2, 3, 4)
print(c)
print(c.shape)  #(2,3,4)
print(c.ndim)    #3

#Array creation
a= np.array([1,2,3])
print(a)  #[1,2,3]
print(a.dtype)  #int32  
b = np.array([1.5, 2, 3.5])
print(b.dtype)  #float64

#Note: we can't pass the array value like this :
#a = np.array(1,2,3,4)

# The type of the array can also be explicitly specified at creation time:
c = np.array([[1,2], [3,4]], dtype = complex)
print(c)


#zeros array 
z = np.zeros((3,4))
print(z)

#ones array 
o = np.ones((2,2))
print(o)

#  np.empty creates an array whose initial content is random and depends on the state of the memory. 
# By default, the dtype of the created array is float64, but it can be specified via the key word argument dtype.

e = np.empty((2,3))
print(e)
print(e.dtype)

e= np.empty((2,3), dtype=np.int64)
print(e)


# If an array is too large to be printed, 
# NumPy automatically skips the central part of the array and only prints the corners:
# To disable this behaviour and force NumPy to print the entire array,
#  you can change the printing options using set_printoptions.
      # np.set_printoptions(threshold=sys.maxsize)  # sys module should be imported



#Basic operations

a = np.array([20,30,40,50])
b = np.arange(4)
c= a - b 
print(c)

print(b ** 2)

print( 10 * np.sin(a))

# Unlike in many matrix languages, the product operator * operates elementwise in NumPy arrays. 
# The matrix product can be performed using the @ operator (in python >=3.5) or the dot function or method:

A = np.array([[1, 1],
              [0, 1]])
B = np.array([[2, 0],
              [3, 4]])

print(A * B) #element wise product array([[2, 0],[0, 4]])

print( A @ B)  #array([[5, 4],[3, 4]])

print(A.dot(B))  #array([[5, 4],[3, 4]]) Same as above i.e., (A @ B)

print(A.sum(), A.min(), A.max())

b = np.arange(12).reshape(3,4)

print(b.sum(axis=0)) #sum of each column
print(b.sum(axis=1)) #sum of each row 
print(b.min(axis=1))

##########Indexing, Slicing and iterating 

a= np.arange(10)**3
print(a)  #[  0   1   8  27  64 125 216 343 512 729]

print(a[2])  #8
print(a[2:5])  #[8 7 24]

a[:6:2]=1000  #From statr to sixth, exclusive, set every 2nd element to 1000
print(a)  #[1000    1 1000   27 1000  125  216  343  512  729]


def f(x,y):
    return 10 * x + y


# The numpy.fromfunction() method is used to construct an array by executing a 
# function over each coordinate of the array.
# In the above code, the function is defined using a lambda function that 
# takes in two arguments i and j, which represent the row and column indices of the array, 
b = np.fromfunction(f, (5,4), dtype=int)
print(b)


##############################################Shape Manipulation

a=np.arange(15).reshape(3,5)
print(a)

print(a.ravel())  # returns the array, flattened

# When the total size of the array does not change reshape should be used.

a=np.array([[0,1],[2,3]])
print(np.resize(a,(2,3)))  #If the new array is larger than the original array,
                            #then the new array is filled with repeated copies of a

print(a.resize(2,3))     #a.resize(new_shape) which fills with zeros instead of repeated copies of a.

# Stacking together different arrays

a= [[9,7],
    [5,2]]

b = [[1,9],
     [5,1]]
print(np.vstack((a,b)))

print(np.hstack((a,b)))


# Copies and Views

# Simple assignments make no copy of objects or their data.
a=np.array([[ 0,  1,  2,  3],
            [ 4,  5,  6,  7],
            [ 8,  9, 10, 11]])

b = a  # # no new object is created
print(b is a)  #True , a and b are two names for the same ndarray object

#View or Shallow copy 
c = a.view()
print(c is a)  #False 
print(c.base is a) #True, c is a view of the data owned by a
print(c.flags.owndata) 

c= c.reshape((2,6))  #a shape doesn;t chnage
print(c)
print(a)

c[0,4]=1234
print(a)  #s's data changes

##deep copy 
d = a.copy() #a new array object with new data is created
print(d is a)  #False 
print(d.base is a)  #False, d doesn't share anything with a
d[0,0] = 9999 #a's data won;t change 

# ##################Tricks and Tips
# "Automatic” Reshaping

# To change the dimensions of an array, you can omit one of the sizes which will then be deduced automatically:
a = np.arange(30)
b = a.reshape((2,-1,3))    # -1 means "whatever is needed"
print(b.shape)

