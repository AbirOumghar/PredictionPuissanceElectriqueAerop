import pickle
import json
import numpy as np

__moiss = None
__data_columns = None
__model = None

def get_estimated_price(mois,moyenne_saisonniere,heures_de_pointe,heures_pleines,heures_creuses):
    try:
        loc_index = __data_columns.index(mois.lower())
    except:
        loc_index = -1

    x = np.zeros(len(__data_columns))
    x[0] = moyenne_saisonniere
    x[1] = heures_de_pointe
    x[2] = heures_pleines
    x[3] = heures_creuses
    if loc_index>=0:
        x[loc_index] = 1

    return round(__model.predict([x])[0],3)


def load_saved_artifacts():
    print("loading saved artifacts...start")
    global  __data_columns
    global __moiss
    with open("./artifacts/columns.json", "r") as f:
        __data_columns = json.load(f)['data_columns']
        __moiss = __data_columns[4:]  # first 3 columns are sqft, bath, bhk

    global __model
    if __model is None:
        with open('./artifacts/prediction.pickle', 'rb') as f:
            __model = pickle.load(f)
    print("loading saved artifacts...done")

def get_location_names():
    return __moiss

def get_data_columns():
    return __data_columns

if __name__ == '__main__':
    load_saved_artifacts()
    print(get_location_names())
    print(get_estimated_price('avril',1000, 3, 3,3))
