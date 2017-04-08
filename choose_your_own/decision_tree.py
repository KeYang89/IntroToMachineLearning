#!/usr/bin/python
import numpy as np
import matplotlib.pyplot as plt
from prep_terrain_data import makeTerrainData
from class_vis import prettyPicture
from sklearn import tree
from matplotlib.colors import ListedColormap
features_train, labels_train, features_test, labels_test = makeTerrainData()


### the training data (features_train, labels_train) have both "fast" and "slow"
### points mixed together--separate them so we can give them different colors
### in the scatterplot and identify them visually
grade_fast = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==0]
bumpy_fast = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==0]
grade_slow = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==1]
bumpy_slow = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==1]


#### initial visualization
plt.xlim(0.0, 1.0)
plt.ylim(0.0, 1.0)
plt.scatter(bumpy_fast, grade_fast, color = "b", label="fast")
plt.scatter(grade_slow, bumpy_slow, color = "r", label="slow")
plt.legend()
plt.xlabel("bumpiness")
plt.ylabel("grade")
plt.show()
################################################################################


### your code here!  name your classifier object clf if you want the 
### visualization code (prettyPicture) to show you the decision boundary



h = 0.01
cmap_light = ListedColormap(['#FFAAAA', '#AAFFAA']) #get a different pair of background colors


clf = tree.DecisionTreeClassifier(min_samples_split=20)
clf.fit(features_train, labels_train)
pre = clf.predict(features_test)


xx, yy = np.meshgrid(np.arange(0.0,1.0, h),
                     np.arange(0.0,1.0, h))
Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])

# Put the result into a color plot
Z = Z.reshape(xx.shape)
plt.pcolormesh(xx, yy, Z, cmap=cmap_light)
plt.show()

from sklearn.metrics import accuracy_score
print(accuracy_score(labels_test,pre))
#accuracy=0.924 for Decision Tree h = 0.01


try:
    print("try adding colors")
    prettyPicture(clf, features_test, labels_test)
except NameError:
    pass
