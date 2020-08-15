from flask import Flask, render_template, request
import gov_data


app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
    return render_template('index.html')

@app.route('/catalog', methods=['GET', 'POST'])
def catalog():
    filtro = request.form['filtro']
    results_catalog = gov_data.results_from_catalog(filtro)
    return render_template('catalog.html', filtro = filtro, results=results_catalog, total_results = len(results_catalog))

if __name__=='__main__':
    app.run(debug=True)