
# Data Preprocessing Template

# Importing the libraries
import numpy as np
import excel
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split

import pandas as pd
from tablib import Dataset
import numpy as np
import matplotlib.pyplot as plt



# Importing the dataset
dataset = pd.read_csv('Data.xlsx', error_bad_lines=False)
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values
dates_row = dataset.loc[4, :]
xt = pd.Series(dates_row).values
nx = pd.read_excel('Data.xlsx')
# it must be the same header in the excel to get the data don't forget to edit it
df = pd.DataFrame(nx, columns= ['Name', 'Price'])


print df



print xt
# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)
