from sklearn.linear_model import LogisticRegression
import joblib

def train_baseline(X_train, y_train):
    model = LogisticRegression()
    model.fit(X_train, y_train)

    joblib.dump(model, "models/model_baseline.pkl")
    return model
