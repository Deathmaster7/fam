import pickle
with open("my_list.pkl", "rb") as f:
    my_list = pickle.load(f)


my_list[0] = 100


with open("my_list.pkl", "wb") as f:
    pickle. dump(my_list, f)

with open("my_list.pkl", "rb") as f:
    my_list = pickle.load(f)
    
print(my_list)