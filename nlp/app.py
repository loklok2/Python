from flask import Flask, render_template, request #객체다 class!!
from konlpy.tag import Okt
import joblib
import os
import re

app = Flask(__name__)
app.debug = True

tfidf_vector = None
model_lr = None

okt = Okt()

def tw_tokenzier(text):
    tokenzier_ko = okt.morphs(text)
    return tokenzier_ko

def load_lr():
    global tfidf_vector, model_lr #전역변수
    tfidf_vector = joblib.load(os.path.join(app.root_path, "model/tfidf_vect.pkl"))
    model_lr = joblib.load(os.path.join(app.root_path, "model/lr.pkl"))
    #루트폴더join해서 지정

def lr_transform(review):
    review = re.sub(r"\d+", " ", review)
    test_matrix = tfidf_vector.transform([review])
    return test_matrix

@app.route("/predict", methods=["GET","POST"])
def nlp_predict():
    if request.method == "GET":
        return render_template("predict.html")
    else:
        review = request.form["review"]
        return render_template("predict_result.html", review=review)
@app.route("/")
def index():
    # 해당 테스트 코드는 잘 작동하지만
    # 별도의 함수로 빠져나가야함
    test_str ="이 영화 재미있어요! 하하하!"
    test_matrix = tfidf_vector.transform([test_str])
    result = model_lr.predict(test_matrix)
    print(result)
    return render_template("index.html") #render_template는 이미 폴더구조가 결정되어 있으니, 따로 생성 필요 X

if __name__ == "__main__":    #python .\app.py 
    load_lr()
    app.run()