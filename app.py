from flask import Flask, request, redirect, render_template
import urllib3

app = Flask(__name__)


def parse(url):
    http = urllib3.PoolManager()
    r = http.request('GET', url)
    return r


@app.route('/')
def index():
    statisticsArr = [
        ['Age group', 'IFR'],
        ['0–19', '0.002%–0.01%'],
        ['20–49', '0.007%–0.03%'],
        ['50–69', '0.25%–1.0%'],
        ['70+', '2.8%–9.3%'],
    ]
    return render_template('index.html', statisticsArr=statisticsArr)


@app.route('/about/')
def about():
    statisticsArr = [
        ['#', 'Country', 'Total Cases', 'Total Deaths', 'Total Recovered'],
        ['1', 'USA', '21,865,323', '370,071', '13,025,931'],
        ['2', 'India', '10,405,097', '150,470', '10,026,751'],
        ['3', 'Brazil', '7,874,539', '199,044', '7,036,530'],
        ['4', 'Russia', '3,332,142', '60,457', '2,709,452'],
        ['5', 'UK', '2,836,801', '77,346', '1,345,824'],
        ['6', 'France', '2,705,618', '66,565', '198,756'],
        ['7', 'Turkey', '2,283,931', '22,070', '2,164,040'],
        ['8', 'Italy', '2,201,945', '76,877', '1,556,356'],
        ['9', 'Spain', '1,982,544', '51,430', '1,405,456'],
        ['10', 'Germany', '1,848,621', '38,436', '1,474,048'],
        ['11', 'Colombia', '1,719,771', '44,723', '1,569,578'],
        ['12', 'Argentina', '1,676,171', '43,976', '1,474,048'],
        ['13', 'Mexico', '1,479,835', '129,987', '1,119,968'],
        ['14', 'Poland', '1,356,882', '30,241', '1,095,616'],
        ['15', 'Iran', '1,268,263', '55,933', '1,050,533'],
        ['16', 'South Africa', '1,149,591', '31,368', '929,239'],
        ['17', 'Ukraine', '1,009,493', '19,505', '773,214'],
    ]
    return render_template('about.html', statisticsArr=statisticsArr)


@app.route('/contact/', methods=['POST', 'GET'])
def contact():  # TODO Если не получиться с БД оптимизировать код
    if request.method == 'POST':
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        username = request.form['username']
        city = request.form['city']
        state = request.form['state']
        zip = request.form['zip']
        comment = request.form['comment']
        with open('data.txt', 'w')as f:
            f.write(f'firstname={firstname}\n'
                    f'lastname={lastname}\n'
                    f'username={username}\n'
                    f'city={city}\n'
                    f'state={state}\n'
                    f'zip={zip}\n'
                    f'comment={comment}\n')
        return redirect('/')
    else:
        return render_template('contact.html')


@app.errorhandler(404)
def error404(error):
    return render_template('error404.html'), 404


@app.errorhandler(500)
def error500(error):
    return render_template('error500.html'), 500


if __name__ == '__main__':
    app.run()
