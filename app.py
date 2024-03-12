from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    context = {'title': 'Главная'}
    return render_template('index.html', **context)


@app.route('/clothes/')
def clothes():
    context = {'title': 'Одежда'}
    clothes_items = [
        {
            "title": "рубашка",
            "description": "description1",
        },
        {
            "title": "юбка",
            "description": "description2",
        },
        {
            "title": "брюки",
            "description": "description3",
        },
    ]
    return render_template('clothes.html', **context, clothes=clothes_items)


@app.route('/shoes/')
def shoes():
    context = {'title': 'Обувь'}
    shoes_items = [
        {
            "title": "туфли1",
            "description": "description1",
        },
        {
            "title": "туфли2",
            "description": "description2",
        },
        {
            "title": "туфли3",
            "description": "description3",
        },
    ]
    return render_template('shoes.html', **context, shoes=shoes_items)


@app.route('/jackets/')
def jackets():
    context = {'title': 'Куртки'}
    jackets_items = [
        {
            "title": "jacket1",
            "description": "description1",
        },
        {
            "title": "jacket2",
            "description": "description2",
        },
        {
            "title": "jacket3",
            "description": "description3",
        },
    ]
    return render_template('jackets.html', **context, jackets=jackets_items)


if __name__ == '__main__':
    app.run(debug=True)
