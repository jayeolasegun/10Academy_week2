# -*- coding: utf-8 -*-

# writes a class that preprocesses columns in my dataframe
# check missing values
# check for the data type
# check replace missing values
# 

# would the class be specific to this data or modify it more
# let me write a function specefic to my data and then a function that is not so
# i can easily maitain the code


def dataframe_dtype(df, dtype = None):
    
    categorical_features = []
    numerical_features = []
    datetime_feature = []

    feature = df.columns.to_series().groupby(df.dtypes).groups
    for name , value in feature.items():
        if name.name == 'object':
            categorical_features.append(value)
        elif name.name in ['int64','int32','float64','float32']:
            numerical_features.append(value)
        elif name.name == 'datetime64[ns]':
            datetime_feature.append(value)
            
    if dtype == 'category':
        return categorical_features
    
    elif dtype == 'numbers':
        return numerical_features
    
    elif dtype == 'datetime':
        
        return datetime_feature
    
    
    