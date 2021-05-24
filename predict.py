import xgboost as xgb
import numpy as np
import pickle


def xgb_predict(model, features, pred):
    pred = np.array(pred).reshape(1,-1)
    pred = xgb.DMatrix(pred, feature_names=features)
    return model.predict(pred)


if __name__ == "__main__":
    print("Hello!")

    # Array consists of:
    # GENDER[1], OT/COTA[1], !!LOCATION[4]!!, PAYRATE[7], YEARS EXP[1], EDUCATION[1]

    pred = np.array([1,1,0,1,0,0,0,0,0,2,2]).reshape(1,-1)
    with open('featname_simp.pkl', 'rb') as f:
        features = pickle.load(f)
        print(features)
    pred = xgb.DMatrix(pred, feature_names=features)

    model = xgb.Booster()
    model.load_model("otsalary_xgbmodel.bst")
    print(model.predict(pred))
