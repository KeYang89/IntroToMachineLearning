#!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit


### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )
features = ["salary", "bonus"]
data_dict.pop('TOTAL',0)
data = featureFormat(data_dict, features)
#labels=data_dict.keys()

### your code below

for point in data:
    salary = point[0]
    bonus = point[1]
    matplotlib.pyplot.scatter( salary, bonus )
    #for label in labels:
    #     matplotlib.pyplot.annotate(
    #         label,
    #         xy=(salary, bonus), xytext=(-20, 20),
    #         textcoords='offset points', ha='right', va='bottom',
    #         bbox=dict(boxstyle='round,pad=0.5', fc='yellow', alpha=0.5),
    #         arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=0'))

matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("bonus")

matplotlib.pyplot.show()
print data