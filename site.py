from flask import Flask, render_template
from urllib.parse import unquote
import json
import xgboost as xgb
import numpy as np
import pickle
import predict


app = Flask(__name__)
app.config["DEBUG"] = True

@app.route("/")
def hello():
    return render_template('index.html')

@app.route("/predict/<string:inputStr>", methods=['GET'])
def predictor(inputStr):
    decoded_str = unquote(inputStr)
    input = convertJSONtoINPUT(decoded_str)
    # print(input)
    if input[0] == 2:
        return "Sorry, not enough data to predict."

    # pred = [0,2,1,1,0,1,0,0,0,2,4]
    ans = predict.xgb_predict(model, features, input)


    return str(ans)

def convertJSONtoINPUT(decodedstr):

    d_salarymap = {
        'Contract':2,
        'Full Time':3,
        'PRN':4,
        'Part Time':5,
        'Per Visit':6,
        'Salary':7,
        'Self Employed':8,
    }


    pred = [0]*11
    d = json.loads(decodedstr)

    pred[0] = int(d['gender'])
    pred[1] = int(d['otcota'])
    pred[-1] = int(d['education'])
    pred[-2] = int(d['yearsofedu'])
    pred[d_salarymap[d['payrate']]] = 1

    return pred

if __name__ == "__main__":
    model = xgb.Booster()
    model.load_model("otsalary_xgbmodel.bst")
    with open('featname_simp.pkl', 'rb') as f:
        features = pickle.load(f)

    app.run()
