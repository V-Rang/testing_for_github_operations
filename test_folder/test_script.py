import numpy as np
import pickle

with open('outputs.pickle', 'rb') as f:
    data = pickle.load(f)

arr_1 = data['arr_1']
arr_2 = data['arr_2']
value = data['val_1']

print("hello")