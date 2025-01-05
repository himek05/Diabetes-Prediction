from django.shortcuts import render
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

def home(request):
    return render(request, 'home.html') 

def about(request):
    return render(request, 'about.html') 

def predict(request):
    return render(request, 'predict.html') 

def result(request):
    dataset = pd.read_csv(r"C:\Users\himek\Desktop\ML-Project\Dpc\diabetes.csv")

    x = dataset.drop(columns="Outcome",axis=1)
    y = dataset["Outcome"]

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=99)

    ln = LogisticRegression()
    ln.fit(x_train, y_train)

    val1 = float(request.POST['n1'])
    val2 = float(request.POST['n2'])
    val3 = float(request.POST['n3'])
    val4 = float(request.POST['n4'])
    val5 = float(request.POST['n5'])
    val6 = float(request.POST['n6'])
    val7 = float(request.POST['n7'])
    val8 = float(request.POST['n8'])

    pred = ln.predict([[val1, val2, val3, val4, val5, val6, val7,val8]])

    result2 = "Positive" if pred == [1] else "Negative"

    return render(request, 'predict.html', {'result2': result2})