from flask import Flask, render_template

app = Flask(__name__)

products = [

    #all the images are 800x800. To fill the webpage just google "product name" 800x800
    #pizzas
    {"name": "Pizza Margarita", "type": "Pizza", "price": 10, "image": "margarita.jpg"},
    {"name": "Pizza Salami", "type": "Pizza", "price": 15, "image": "salami.jpg"},
    {"name": "Pizza Diavollo", "type": "Pizza", "price": 12, "image": "diavollo.jpg"},
    {"name": "Pizza Tuna", "type": "Pizza", "price": 10, "image": "tuna.jpg"},
    {"name": "Pizza Bolonieze", "type": "Pizza", "price": 10, "image": "bolonieze.jpg"},
    {"name": "Pizza Speciale", "type": "Pizza", "price": 10, "image": "speciale.jpg"},
    {"name": "Pizza Hawaii", "type": "Pizza", "price": 10, "image": "hawaii.jpg"},
    {"name": "Pizza Quadro Formacci", "type": "Pizza", "price": 10, "image": "quadroformacci.jpg"},
    {"name": "Pizza Quadro Stagione", "type": "Pizza", "price": 10, "image": "quadrostagione.jpg"},
    {"name": "Pizza Francesko", "type": "Pizza", "price": 10, "image": "francesko.jpg"},

    #drinks
    {"name": "Coca Cola", "type": "Drinks", "price": 6, "image": "cocacola.jpg"},
    {"name": "Pepsi", "type": "Drinks", "price": 5, "image": "pepsi.jpg"},
    {"name": "Sprite", "type": "Drinks", "price": 5, "image": "sprite.jpg"},
    {"name": "Fanta", "type": "Drinks", "price": 5, "image": "fanta.jpg"},
    {"name": "Lemonade", "type": "Drinks", "price": 4, "image": "lemonade.jpg"},
    {"name": "Iced Tea", "type": "Drinks", "price": 4, "image": "icedtea.jpg"},
    {"name": "Orange Juice", "type": "Drinks", "price": 7, "image": "orangejuice.jpg"},
    {"name": "Apple Juice", "type": "Drinks", "price": 7, "image": "applejuice.jpg"},
    {"name": "Mineral Water", "type": "Drinks", "price": 3, "image": "mineralwater.jpg"},
    {"name": "Milkshake", "type": "Drinks", "price": 8, "image": "milkshake.jpg"}

    # we can add more products or categories
]

orders = []

@app.route('/')
def index():
    return render_template('index.html', products=products, orders=orders)

if __name__ == '__main__':
    app.run(debug=True)
