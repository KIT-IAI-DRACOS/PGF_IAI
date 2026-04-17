import pickle, json

with open("example_metadata_iceland.pkl", "rb") as f:
    data = pickle.load(f)

with open("iceland.json", "w") as f:
    json.dump(data, f)