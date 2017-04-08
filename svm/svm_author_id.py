#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
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
#features_train = features_train[:len(features_train)/100]
#labels_train = labels_train[:len(labels_train)/100]
from sklearn import svm
clf = svm.SVC(kernel="rbf",C=10000)
clf.fit(features_train, labels_train)
pre1=clf.predict(features_test)
for pre in pre1:
  if pre==1:
      chris=chris+1
  else:
      sara=sara+1
print("Chris",chris)
print("Sarah",sara)
#from sklearn.metrics import accuracy_score
#print(pre1[10],pre1[26],pre1[50])

#print(accuracy_score(labels_test,pre1))

#########################################################


