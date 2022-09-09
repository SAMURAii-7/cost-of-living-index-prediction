import json
import pickle
import numpy as np

__data_columns = None
__model = None


def predict_coi(rent_ind, groceries_ind, rp_ind, ppi_ind):
    load_saved_artifacts()
    x = np.array([[rent_ind, groceries_ind, rp_ind, ppi_ind]])
    res = float(np.round(__model.predict(x), 2)[0])
    return res


def get_cols():
    return __data_columns


def load_saved_artifacts():
    print("loading saved artifacts...start")
    global __data_columns
    global __model

    with open("./artifacts/columns.json", "r") as f:
        __data_columns = json.load(f)["data_columns"]

    with open("./artifacts/cost_of_living_index.pickle", "rb") as f:
        __model = pickle.load(f)
    print("loading saved artifacts...done")


# if __name__ == "__main__":
# load_saved_artifacts()
# print(predict_coi(2, 11, 10, 25))
