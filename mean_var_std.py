import numpy as np

def calculate(list):
    calculations = dict()
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")
    else:
        arr = np.array(list).reshape(3,3)

        #Finding mean for row and column
        mean_col = arr.mean(axis=0).tolist() #Axis 0 finds the mean for all values in the column and tolist() converts those values into a list
        mean_row = arr.mean(axis=1).tolist() #Axis 1 for values in the row
        mean = [mean_col,mean_row,arr.mean()]

        #Finding variance
        var_col = arr.var(axis=0).tolist()
        var_row = arr.var(axis=1).tolist()
        variance = [var_col,var_row,arr.var()]

        #Finding Standard Deviation
        std_col = arr.std(axis=0).tolist()
        std_row = arr.std(axis=1).tolist()
        std = [std_col,std_row,arr.std()]

        #Finding max values
        max_col = arr.max(axis=0).tolist()
        max_row = arr.max(axis=1).tolist()
        maxvals = [max_col,max_row,arr.max()]

        #Finding the minimum values
        min_col = arr.min(axis=0).tolist()
        min_row = arr.min(axis=1).tolist()
        minvals = [min_col,min_row,arr.min()]

        #Finding the sum
        sum_col = arr.sum(axis=0).tolist()
        sum_row = arr.sum(axis=1).tolist()
        sumvals = [sum_col,sum_row,arr.sum()]

        calculations = {
            'mean': mean,
            'variance': variance,
            'standard deviation': std,
            'max': maxvals,
            'min': minvals,
            'sum': sumvals
}

    return calculations