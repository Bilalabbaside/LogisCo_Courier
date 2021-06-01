from sklearn.datasets import load_iris
from sklearn import tree
import numpy as np
iris = load_iris()
print(iris.feature_names)
print(iris.target_names)

print(iris.data[0])
print(iris.target[0])


removed = [0,40,120]

new_data = np.delete(iris.data , removed , axis = 0)
new_target = np.delete(iris.target , removed )

clf = tree.DecisionTreeClassifier()
clf = clf.fit(new_data , new_target)
prediction = clf.predict(iris.data[removed])
print("Orignal labels as per data are "  , iris.target[removed])
print("Orignal labels as per data are "  , prediction)




