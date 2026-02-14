with open('energy_model.pkl', 'wb') as f:
    pickle.dump(model, f)

print("Model trained and saved as energy_model.pkl")