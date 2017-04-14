#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    
    cleaned_data = []
    cleaned_tuple=()
    age=0
    net_worth=0
    error=0
    ### your code goes here
    for i in range(0,89):
        error = predictions[i][0]-net_worths[i][0]
        age=ages[i][0]
        net_worth=net_worths[i][0]

        cleaned_tuple=(age,net_worth,error)
        cleaned_data.append(cleaned_tuple)

    cleaned_data = sorted(cleaned_data, key=lambda tup: tup[2])
    cleaned_data = cleaned_data[:81]
    return cleaned_data

