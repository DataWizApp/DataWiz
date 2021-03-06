from .utils import find_in_vardict
from .var_dict import VarDict
from sklearn.preprocessing import MinMaxScaler, StandardScaler, OneHotEncoder
import numpy as np

class Processor():
    def __init__(self, vardict=VarDict()):
        self.vardict = vardict
    
    def standardizer(self, var_name, col_name, new_var=True, new_var_name="_"):
        if((new_var==True) and (new_var_name=="_")):
            print("A null variable is created with name '_'.\n Please move it to some other variable name.\n Using method move_empty()")    

        scale = StandardScaler()
        
        var = find_in_vardict(self.vardict, var_name)
        
        if col_name:
            var_data = var["data"][col_name]
        else:
            var_data = var["data"].select_dtypes(include=['float64', 'int64'])

        scaled_data_values = scale.fit_transform(np.array(var_data.values).reshape(-1, 1))
        scaled_data = var['data']
        scaled_data['{}_Scaled'.format(col_name)] = scaled_data_values
        self.vardict.add(scaled_data.round(2), new_var_name)

    def normalize(self, var_name, col_name, new_var=True, new_var_name="_"):
        if((new_var==True) and (new_var_name=="_")):
            print("A null variable is created with name '_'.\n Please move it to some other variable name.\n Using method move_empty()")    
       
        scale = MinMaxScaler()
        
        var = find_in_vardict(self.vardict, var_name)
        if col_name:
            var_data = var["data"][col_name]
        else:
            var_data = var["data"].select_dtypes(include=['float64', 'int64'])

        scaled_data_values = scale.fit_transform(np.array(var_data.values).reshape(-1, 1))
        scaled_data = var['data']
        scaled_data['{}_Normalized'.format(col_name)] = scaled_data_values
        self.vardict.add(scaled_data.round(2), new_var_name)
    
    # def onehotencoder(self, var_name, col_name, new_var=True, new_var_name="_"):
    #     if((new_var==True) and (new_var_name=="_")):
    #         print("A null variable is created with name '_'.\n Please move it to some other variable name.\n Using method move_empty()")    
       
    #     enc = OneHotEncoder()
        
    #     var = find_in_vardict(self.vardict, var_name)
    #     var_data = var["data"][col_name]
    #     if col_name:
    #         var_data = var["data"][col_name]
    #     else:
    #         var_data = var["data"].select_dtypes(include=['object'])
    #     encoded_data_values = enc.fit_transform([var_data.values])
    #     encoded_data = var
    #     encoded_data['{}_Category1'.format(col_name)] = scaled_data_values

    #     self.vardict.add(encoded_data, new_var_name)

    def label_encoder(self, var_name, col_name, new_var=True, new_var_name="_"):
        if((new_var==True) and (new_var_name=="_")):
            print("A null variable is created with name '_'.\n Please move it to some other variable name.\n Using method move_empty()")    
        
        var = find_in_vardict(self.vardict, var_name)
        if col_name:
            var_data = var["data"][col_name]
        else:
            var_data = var["data"].select_dtypes(include=['float64', 'int64'])


        categories = var_data.unique()
        cat_list = dict(zip(categories, range((len(categories)))))
        scaled_data = var["data"]
        scaled_data['{}_Encoded'.format(col_name)] = scaled_data[col_name].map(cat_list)
        self.vardict.add(scaled_data, new_var_name)