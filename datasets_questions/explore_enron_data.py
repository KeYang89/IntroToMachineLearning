#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))
# get total number of people
# print(len(enron_data))
#print(list(enron_data))
#print(len(list(enron_data)))

#get total number of features for each person
#print(len(enron_data.values()[0]))

#get total poi==True in the pkl
# poiCount=0
# for person in enron_data.values():
#     poiValue = person['poi']
#     if poiValue==True:
#         poiCount=poiCount+1
# print(poiCount)

#get total poi==True in the text file
#name_file = open("../final_project/poi_names.txt", "r")
#name_list=name_file.read()
#in the text file, each person is one line, each POI line start with a '(y)' or a '(n)'
#therefore '(' is what all POI lines started with
#so we just need to count the '(' to get the total number of POI in the text file
#sub='('
#print(name_list.count(sub))

#get total_stock_value by James Prentice
#print(enron_data['PRENTICE JAMES']['total_stock_value'])

#get from_this_person_to_poi by Wesley Colwell
#print(enron_data['COLWELL WESLEY']['from_this_person_to_poi'])

#get exercised_stock_options by Jeffrey K Skilling
#print(enron_data['SKILLING JEFFREY K']['exercised_stock_options'])