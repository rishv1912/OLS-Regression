import pandas as pd
from sklearn.preprocessing import OneHotEncoder

def bin_to_num(data):
    binnedinc = []
    for i in data['binnedic']:
        i = i.strip["()[]"]
        print(i)
        i = i.split(",")

        i = tuple(i)

        i = tuple(map(float,i))

        i = list(i)

        binnedinc.append(i)
    data["binnedic"] = binnedic

    data["lower_bound"] = [i[0] for i in data["binnedic"]]
    data["upper_bound"] = [i[1] for i in data["binnedic"]]

    data["median"] = (data["lower_bound"] + data["upper_bound"])/2

    data.drop("binnedic",axis=1,inplace=True)
    return data

def cat_to_cal(data):
    data["county"] = [i.split(",")[0] for i in data["geography"]]
    data["state"] = [i.split(",")[1] for i in data["geography"]]

    data.drop("geography",axis =1 ,inplace =True)
    return data

def one_hot_encoding(X):
    categorical_columns = X.select_dtypes(include=["object"]).columns
    one_hot_encoder = OneHotEncoder(sparse=False,handle_unknown='ignore')
    one_hot_encoded = one_hot_encoder.fit_transform(X[categorical_columns])

    one_hot_encoded = pd.DataFrame(one_hot_encoded,columns = one_hot_encoder.get_feature_names_out(categorical_columns))

    X = X.drop(categorical_columns,axis=1)
    X = pd.concat([X,one_hot_encoded],axis=1)
    return X
