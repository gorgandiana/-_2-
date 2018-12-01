from flask import Flask
from flask import url_for, render_template, request, redirect
import file_functions

app = Flask(__name__)


# браузер не будет сохранять картинку со статистикой в кэше
@app.after_request
def set_response_headers(response):
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    return response


@app.route('/')
def index():
    urls = {'Заполнить анкету': url_for('form'),
            'Показать статистику': url_for('statistics'),
            'Вывод результатов в формате json': url_for('json_data'),
            'Поиск': url_for('search'), }
    return render_template('index.html', urls=urls)


@app.route('/form')
def form():
    if request.args:
        name = request.args['name']
        surname = request.args['surname']
        lang = request.args['lang']
        ans_list = [request.args['word1'], request.args['word2'],
                    request.args['word3'], request.args['word4'],
                    request.args['word5'], request.args['word6'],
                    request.args['word7'], request.args['word8'],
                    request.args['word9'], request.args['word10']]
        com_list = [request.args['com1'], request.args['com2'],
                    request.args['com3'], request.args['com4'],
                    request.args['com5'], request.args['com6'],
                    request.args['com7'], request.args['com8'],
                    request.args['com9'], request.args['com10']]
        if '' in ans_list or name == '' or surname == '' or lang == '':
            return render_template('form.html', error=True)
        file_functions.in_csv(name, surname, lang, ans_list, com_list)
        return redirect(url_for('index'))
    return render_template('form.html')


@app.route('/statistics')
def statistics():
    file_functions.graph()
    return render_template('statistics.html')


@app.route('/json_data')
def json_data():
    return '<pre>' + file_functions.csv_json() + '</pre>'


@app.route('/search')
def search():
    langs = file_functions.search_L()
    if request.args:
        list = file_functions.search(request.args['search'],
                                     request.args['lang'])
        return render_template('results.html', list=list)
    return render_template('search.html', langs=langs)


if __name__ == '__main__':
    app.run(debug=True)
