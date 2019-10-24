# import numpy as np
# from sklearn.svm import SVC
# X = np.array([[-1, -1], [-2, -1], [1, 1], [2, 1]])
# y = np.array([1, 1, 2, 2])
# clf = SVC()
# clf.fit(X, y)
# SVC(C=1.0, cache_size=200, class_weight=None, coef0=0.0, decision_function_shape='ovr', degree=3, gamma='auto',
#   kernel='rbf', max_iter=-1, probability=False, random_state=None, shrinking=True, tol=0.001, verbose=False)
# print(clf.predict([[-0.8, -1]]))

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
style.use("ggplot")
from sklearn import svm
from sklearn.svm import SVC
print('svm\n')
X = np.array([[1, 2], [5, 8], [1.5, 1.8], [8, 8], [1, 0.6], [9, 11]])
# following command is used after scikit 0.19 version to pass 1D array
# X = X.reshape(1, -1)
y = [0, 1, 0, 1, 0, 1]
clf = svm.SVC(kernel='linear', C=1.0)
clf.fit(X, y)
print(clf.predict(X))
w = clf.coef_[0]
print(w)

a = -w[0] / w[1]

xx = np.linspace(0, 12)
yy = a * xx - clf.intercept_[0] / w[1]

h0 = plt.plot(xx, yy, 'k-', label="non weighted div")

plt.scatter(X[:, 0], X[:, 1], c=y)
plt.legend()
plt.show()

# SVC
print('\nsvc\n')
A = np.array([[-1, -1], [-2, -1], [1, 1], [2, 1]])
B = np.array([1, 1, 2, 2])
clf = SVC()
clf.fit(A, B)
print(clf.predict(A))

