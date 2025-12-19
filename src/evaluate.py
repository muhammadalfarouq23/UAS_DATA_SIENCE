from sklearn.metrics import accuracy_score, mean_absolute_error

def evaluate_model(model, X_test, y_test):
    y_pred = model.predict(X_test)
    return accuracy_score(y_test, y_pred)
