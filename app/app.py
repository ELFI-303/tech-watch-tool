from flask import Flask, render_template

from datetime import datetime
import json

def sort_articles(json_data: list) -> list:
    a, b, c, d = [],[],[],[]
    for element in json_data:
        cat_list = element['categories']
        if cat_list == None:
            element['categories'] = ['']
        else:
            element['categories'] = cat_list
        if 'high' in (element['output']).lower() and 'moderate' in (element['output']).lower():
            b.append(element)
        elif 'high' in (element['output']).lower():
            a.append(element)
        elif 'moderate' in (element['output']).lower():
            c.append(element)
        else:
            d.append(element)
    a = sorted(a, key=lambda x: datetime.strptime(x['date'], '%d/%m/%Y'), reverse=True)
    b = sorted(b, key=lambda x: datetime.strptime(x['date'], '%d/%m/%Y'), reverse=True)
    c = sorted(c, key=lambda x: datetime.strptime(x['date'], '%d/%m/%Y'), reverse=True)
    d = sorted(d, key=lambda x: datetime.strptime(x['date'], '%d/%m/%Y'), reverse=True)
    sorted_data = a + b + c + d
    return sorted_data

def sort_post(json_data: list) -> list:
    a, b = [], []
    for element in json_data:
        if "yes" in element['analyze'].lower():
            a.append(element)
        else:
            b.append(element)
    a = sorted(a, key=lambda x: datetime.strptime(x['date'], '%d/%m/%Y'), reverse=True)
    b = sorted(b, key=lambda x: datetime.strptime(x['date'], '%d/%m/%Y'), reverse=True)
    return a + b

app = Flask(__name__)

@app.route("/")
def home(): 
    with open('results/result.json', 'r') as file:
        json_articles = json.load(file)
    sorted_articles = sort_articles(json_articles)
    return render_template('index.html',article_json=sorted_articles)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=25565, debug=True)