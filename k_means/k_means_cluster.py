#!/usr/bin/python 

""" 
    Skeleton code for k-means clustering mini-project.
"""




import pickle
import numpy
import matplotlib.pyplot as plt
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit
from sklearn.preprocessing import MinMaxScaler




def Draw(pred, features, poi, mark_poi=False, name="image.png", f1_name="feature 1", f2_name="feature 2"):
    """ some plotting code designed to help you visualize your clusters """

    ### plot each cluster with a different color--add more colors for
    ### drawing more than five clusters
    colors = ["b", "c", "k", "m", "g"]
    for ii, pp in enumerate(pred):
        plt.scatter(features[ii][0], features[ii][1], color = colors[pred[ii]])

    ### if you like, place red stars over points that are POIs (just for funsies)
    if mark_poi:
        for ii, pp in enumerate(pred):
            if poi[ii]:
                plt.scatter(features[ii][0], features[ii][1], color="r", marker="*")
    plt.xlabel(f1_name)
    plt.ylabel(f2_name)
    plt.savefig(name)
    plt.show()



### load in the dict of dicts containing all the data on each person in the dataset
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )
### there's an outlier--remove it! 
data_dict.pop("TOTAL", 0)


### the input features we want to use 
### can be any key in the person-level dictionary (salary, director_fees, etc.) 
feature_1 = "salary"
feature_2 = "exercised_stock_options"
#feature_3 = "total_payments"
poi  = "poi"
stock=[]
salary=[]
#features_list = [poi, feature_1, feature_2, feature_3]
features_list = [poi, feature_1, feature_2]
data = featureFormat(data_dict, features_list)
poi, finance_features = targetFeatureSplit( data )
#get stock list
for eachdata in data:
    stock.append(float(eachdata[2]))
rescaled_stock = MinMaxScaler().fit_transform(stock)

# print stock
# print max(stock)
# print min(i for i in stock if i > 0)

st_min=float(min(i for i in stock if i > 0));
st_max=float(max(stock))
rescaled_stock1000000=(1000000.0-st_min)/(st_max-st_min)
print "rescaled_stock1000000",rescaled_stock1000000
#get salary list
for eachdata in data:
    salary.append(float(eachdata[1]))
rescaled_salary= MinMaxScaler().fit_transform(salary)

# print salary
# print max(salary)
# print min(i for i in salary if i > 0)

sa_min=float(min(i for i in salary if i > 0));
sa_max=float(max(salary))
rescaled_salary200000=(200000.0-sa_min)/(sa_max-sa_min)
print "rescaled_salary200000",rescaled_salary200000

### in the "clustering with 3 features" part of the mini-project,
### you'll want to change this line to 
### for f1, f2, _ in finance_features:
### (as it's currently written, the line below assumes 2 features)

######
#_ has 3 main conventional uses in Python:
#To hold the result of the last executed statement in an interactive interpreter session.
# This precedent was set by the standard CPython interpreter, and other interpreters have followed suit
#For translation lookup in i18n (see the gettext documentation for example), as in code like: raise forms.
# ValidationError(_("Please enter a correct username"))
#As a general purpose "throwaway" variable name to indicate that part of a function result is being deliberately ignored,
# as in code like: label, has_label, _ = text.partition(':')
#The latter two purposes can conflict, so it is necessary to avoid using _ as a throwaway variable
# in any code block that also uses it for i18n translation (many folks prefer a double-underscore, __,
# as their throwaway variable for exactly this reason).
for f1, f2 in finance_features:
#for f1, f2, _ in finance_features:
    plt.scatter( f1, f2)
plt.show()

### cluster here; create predictions of the cluster labels
### for the data and store them to a list called pred

from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters=2, random_state=0).fit(data)
#kmeans.labels_
pred=kmeans.predict(data)
#kmeans.cluster_centers_

### rename the "name" parameter when you change the number of features
### so that the figure gets saved to a different file
try:
    Draw(pred, finance_features, poi, mark_poi=False, name="clusters.pdf", f1_name=feature_1, f2_name=feature_2)
except NameError:
    print "no predictions object named pred found, no clusters to plot"
