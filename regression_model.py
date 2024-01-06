import warnings 

warnings.filterwarnings("ignore")

import matplotlib.pyplot as plt
import pandas as pd
import statsmodel.api as sm

from data_processing import split_data

def correlation_among_numeric_features(df,cols):
    numeric_col = df[cols]
    corr = numeric_col.corr()

    corr_features = set()
    for i in range(len(corr.columns)):
        for j in range(i):
            if abs(corr.iloc[i,j]) > 0.8:
                colname = corr.columns[i]
                corr_features.add(columns)
    return corr_features



def lr_model(x_train,y_train):
    x_train_with_intercept = sm.add_constant(x_train)
    lr = sm.OLS(y_train,x_train_with_intercept).fit()
    return lr

def identify_significant_vars(lr,p_value_threshold=0.05):
    print(lr.values)
    print(lr.rsquared) 
