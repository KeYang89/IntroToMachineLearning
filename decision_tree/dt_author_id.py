#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 3 (decision tree) mini-project.

    Use a Decision Tree to identify emails from the Enron corpus by author:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
### your code goes here ###
chris=0
sara=0
from sklearn import tree
clf = tree.DecisionTreeClassifier(min_samples_split=40)
clf = clf.fit(features_train, labels_train)
pre=clf.predict(features_test)
# for pre in pre1:
#   if pre==1:
#       chris=chris+1
#   else:
#       sara=sara+1
# print("Chris",chris)
# print("Sarah",sara)
#########################################################


from sklearn.metrics import accuracy_score
print(accuracy_score(labels_test,pre))