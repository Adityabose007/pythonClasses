import numpy as np
# import time

# arr = np.array([1,2,3,5,6])

# print(arr)

# print(type(arr))

# zero = np.zeros(5)
# print(zero)

# random = np.random.rand(4,2) #Random Float Array Creation 
# print(random)

# rand_int = np.random.randint(7, size=(5,2))  #Random Integer Array creation
# print(rand_int)

# arr2d = np.array([[1,4,0,9], [7,11,24,8]])
# print(arr2d)

# s = arr2d.shape
# print(s)

# r = np.arange(3,15,5)
# print(r)

arr4 = np.linspace(0,5,5)
print(arr4)

# arr3d = np.array([[[1,2,5], [5,9,8]],[[6,9,45], [4,98,43]]])

# print(arr3d)
# print(arr3d.shape)

# print(arr3d.ndim)

# arr = np.random.randint(7, size=(3,4))
# print(arr[:1])
# print("\n")
# print(arr)

# arrshape = arr.reshape(4,3)
# print(arrshape)

# arr2d = np.array([[1,4,8,0],[5,6,7,8]]) 
# newarr = arr2d.reshape(-1)
# print(newarr)
# for i in arr :
#     print(i) 
# for i in arr2d :
#     print(i)
#     for k in i:
#         print(k)


#---------------------------------------------------------------------------
# size = 100_00

# list1 = list(range(size))
# list2 = list(range(size))
# start = time.time()

# result = [x+y for x,y in zip(list1 , list2)]
# # print(result)

# print("Numpy time : ", time.time()-start)

# print(start)

# arr1 = np.arange(size)
# arr2 = np.arange(size)
# start = time.time()
# print(start)
# rel = arr1 + arr2

# print("Numpy arrange Time : ", time.time()-start)