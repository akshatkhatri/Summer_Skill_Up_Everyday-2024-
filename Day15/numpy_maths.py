import numpy as np

arr = np.array([[1,2],[3,4]])

# print(repr(arr + 1))
# print(repr(arr - 1.2))
# print(repr(arr * 2))
# print(repr(arr / 5))
# print(repr(arr // 2))
# print(repr(arr ** 2))
# print(repr(arr ** 0.5))


def f2c(temps):
  return (5/9)*(temps-32)

fahrenheits = np.array([32, -4, 144, -40])
celsius = f2c(fahrenheits)
print('Celsius: {}'.format(repr(celsius)))

## to find power 'e' and log we use

print(repr(np.exp(arr))) # calculates e^x
print(repr(np.exp2(arr))) # calculates 2^x

arr2 = np.array([[1,3],[np.e,np.pi]])

print(repr(np.log(arr2)))

print(repr(np.power(3,arr2)))

matrix1 = np.array([[1,2],[3,4],[5,6]])
matrix2 = np.array([[1,2,3],[4,5,6]])

print(repr(np.matmul(matrix1,matrix2)))