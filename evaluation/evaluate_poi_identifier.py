#!/usr/bin/python


"""
    Starter code for the evaluation mini-project.
    Start by copying your trained/tested POI identifier from
    that which you built in the validation mini-project.

    This is the second step toward building your POI identifier!

    Start by loading/formatting the data...
"""

import pickle
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "r") )

### add more features to features_list!
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list)
labels, features = targetFeatureSplit(data)
poiCount=0
totalCount=0
rightCount_p=0
rightCount_n=0
### your code goes here 
from feature_format import featureFormat, targetFeatureSplit
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.cross_validation import train_test_split


features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size=0.30, random_state=42)

#get poi number in test set
for eachPerson in labels_test:
    totalCount=totalCount+1
    if eachPerson == 1.0:
        poiCount = poiCount + 1

print "poi number in the test set:",poiCount
print "total number of people in the test set:",totalCount
allZeros=[0]*29
clf2 = DecisionTreeClassifier()
clf2.fit(features_train, labels_train)
pred2 = clf2.predict(features_test)
print "accuracy 2:", accuracy_score(labels_test, pred2)
print "accuracty if all zeros",accuracy_score(labels_test,allZeros)

#compare for true positives
for i in range(0,29):
    if pred2[i]==1.0==labels_test[i]:
        rightCount_p=rightCount_p+1
    if pred2[i]==0.0==labels_test[i]:
        rightCount_n=rightCount_n+1
print rightCount_p
print rightCount_n

#exercise
cp=0
cn=0
fp=0
fn=0
predictions = [0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1]
true_labels = [0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0]
for j in range (0,len(predictions)):
    if predictions[j]==0==true_labels[j]:
        cn=cn+1
    if predictions[j]==1==true_labels[j]:
        cp=cp+1
    if predictions[j]==1 and true_labels[j]==0:
        fp=fp+1
    if predictions[j]==0 and true_labels[j]==1:
        fn=fn+1
print "true negative",cn
print "true positive",cp
print "false negative",fn
print "false positive",fp