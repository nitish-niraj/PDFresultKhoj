from flask import Flask, render_template, request
import csv, os

app = Flask(__name__)
CSV_PATH = os.path.join("data", "data.csv")

def search_data(roll, name, father):
    results = []
    with open(CSV_PATH, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            match = True
            if roll   and roll   != row["ROLL"]:
                match = False
            if name   and name.lower()   not in row["NAME"].lower():
                match = False
            if father and father.lower() not in row["FATHERNAME"].lower():
                match = False
            if match:
                results.append(row)
    return results

@app.route('/', methods=['GET','POST'])
def index():
    results = []
    if request.method == 'POST':
        roll   = request.form.get('roll','').strip()
        name   = request.form.get('name','').strip()
        father = request.form.get('father','').strip()
        results = search_data(roll, name, father)
    return render_template('index.html', results=results)

if __name__ == '__main__':
    app.run(debug=True)
