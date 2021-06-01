from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics
from sklearn.model_selection import cross_val_score

wine=datasets.load_wine()
X_train,X_test,y_train,y_test=train_test_split(wine.data,wine.target,test_size=0.3)
knn=KNeighborsClassifier(n_neighbors=13)
knn.fit(X_train,y_train)
y_pred=knn.predict(X_test)
print("Accuracy:",metrics.accuracy_score(y_test,y_pred))
scores=cross_val_score(knn,wine.data,wine.target,cv=5)
print("3-fold cross validation:",scores)
print("3-fold mean cross validation",scores.mean())