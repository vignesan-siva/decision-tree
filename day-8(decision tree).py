import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


data=pd.read_csv("C:\\Users\\elcot\\Desktop\\machine learning tutorial\\classification\\SVM & Decision tree\\Wine.csv")


x=data.iloc[:,0:12].values
y=data.iloc[:,[-1]].values

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.25,random_state=0)

from sklearn.preprocessing import StandardScaler
sc=StandardScaler()
x_train=sc.fit_transform(x_train)
x_test=sc.transform(x_test)


#training your dataset

from sklearn.tree import DecisionTreeClassifier
classifier=DecisionTreeClassifier( criterion="gini",random_state=0)
classifier.fit(x_train,y_train)
y_pred=classifier.predict(x_test)

#find confusion matrix
from sklearn.metrics import confusion_matrix
cm=confusion_matrix(y_test,y_pred)
acc=(sum(np.diag(cm))/len(y_test))


#visualization

feature_col=data
feature_col=feature_col.drop('customer_segment',axis=1)



from sklearn.tree import plot_tree
plt.figure(dpi=300)
plot_tree(decision_tree=classifier,max_depth=20,
                   feature_names=feature_col.columns,class_names=["1","2","3"],filled=True)

plt.show()










