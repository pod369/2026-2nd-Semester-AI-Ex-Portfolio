import numpy as np
import matplotlib.pyplot as plt


a = np.array([1, 2, 3], dtype=float)
print("a =", a)
print("차원:", a.ndim)
print("dtype:", a.dtype)
print("shape:", a.shape)


b = np.array([(1.5, 2, 3), (4, 5, 6)], dtype=float)
print("b.shape =", b.shape)


data = np.array([1.0, 2.0])
print("data * 1.6 =", data * 1.6)


c = np.array([[0, 0, 0],
              [10, 10, 10],
              [20, 20, 20],
              [30, 30, 30]])
d = np.array([1, 2, 3])
print("c.shape =", c.shape, " d.shape =", d.shape)
print("c + d =\n", c + d)


e = np.array([1, 2, 3, 4])
print("e.shape =", e.shape)
try:
    print(c + e)
except ValueError as err:
    print("Error:", err)


print("max(a) =", max(a))
print("a.max() =", a.max())
print("min(a) =", min(a))
print("a.sum() =", a.sum())


s = [[10, 20, 30],
     [30, 40, 50],
     [50, 60, 70],
     [70, 80, 90]]

print("2차원 배열 :", s)
print("열 평균:", np.mean(s, axis=0))
print("행 평균:", np.mean(s, axis=1))


print("np.where(a < 3):", np.where(a < 3))


d = np.random.random((2, 2))
print("랜덤 배열 d:\n", d)

e = np.random.normal(0, 2, (2, 3))
print("정규분포 난수 e:\n", e)


plt.hist(np.random.normal(loc=0.0, scale=1.0, size=100000), bins=100)
plt.show()
