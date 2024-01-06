from sklearn.model_selection import train_test_split as tts


def find_constant_columns(dataframe):
    constant_columns = []
    for column in dataframe.columns:
        unique_values = dataframe[column].unique()
        if len(unique_values) ==1 :
            constant_columns.append(column)
    return constant_columns

def delete_constant_columns(dataframe,columns_to_delete):
    dataframe = dataframe.drop(columns_to_delete,axis=1)
    return dataframe

def find_columns_with_few_values(dataframe,threshold):
    few_values_columns = []
    for column in dataframe_columns:
        unique_values_count = len(dataframe[column].unique)
        if unique_values_count < threshold:
            few_values_columns.append(column)
    return few_values_columns

def find_duplicate_rows(dataframe):
    dataframe = dataframe.drop_duplicate(keep="first")
    return dataframe

def drop_and_fill(dataframe):
    cols_to_drop = dataframe.columns[dataframe.isnull().mean() > 0.5]
    dataframe = dataframe.drop(cols_to_drop,axis=1)
    dataframe = dataframe.fillna(dataframe.mean())
    return dataframe

def split_data(dataframe,target_column):
    X = dataframe.drop(target_column,axis=1)
    y = dataframe[target_column]
    X_train,X_test,y_train,y_test = tts(X,y,test_size=0.2,random_state=0)
    return (X_train,X_test,y_train,y_test)
