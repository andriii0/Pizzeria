from flask import Flask, render_template

app = Flask(__name__)

products = [

    #all the images are 800x800. To fill the webpage just google "product name" 800x800
    #pizzas
    {"name": "Pizza Margarita", "type": "Pizza", "section": "Vegetarian", "price": 10, "image": "margarita.jpg"},
    {"name": "Pizza Salami", "type": "Pizza", "section": "Meat", "price": 15, "image": "salami.jpg"},
    {"name": "Pizza Diavollo", "type": "Pizza", "section": "Meat", "price": 12, "image": "diavollo.jpg"},
    {"name": "Pizza Tuna", "type": "Pizza", "section": "Meat", "price": 10, "image": "tuna.jpg"},
    {"name": "Pizza Bolonieze", "type": "Pizza", "section": "Meat", "price": 10, "image": "bolonieze.jpg"},
    {"name": "Pizza Speciale", "type": "Pizza", "section": "Meat", "price": 10, "image": "speciale.jpg"},
    {"name": "Pizza Hawaii", "type": "Pizza", "section": "Meat", "price": 10, "image": "hawaii.jpg"},
    {"name": "Pizza Quadro Formacci", "type": "Pizza", "section": "Vegetarian", "price": 10,
     "image": "quadroformacci.jpg"},
    {"name": "Pizza Quadro Stagione", "type": "Pizza", "section": "Vegetarian", "price": 10,
     "image": "quadrostagione.jpg"},
    {"name": "Pizza Francesko", "type": "Pizza", "section": "Vegetarian", "price": 10, "image": "francesko.jpg"},

    {"name": "Coca Cola", "type": "Drinks", "section": "Cold", "price": 6, "image": "cocacola.jpg"},
    {"name": "Pepsi", "type": "Drinks", "section": "Cold", "price": 5, "image": "pepsi.jpg"},
    {"name": "Sprite", "type": "Drinks", "section": "Cold", "price": 5, "image": "sprite.jpg"},
    {"name": "Fanta", "type": "Drinks", "section": "Cold", "price": 5, "image": "fanta.jpg"},
    {"name": "Lemonade", "type": "Drinks", "section": "Cold", "price": 4, "image": "lemonade.jpg"},
    {"name": "Iced Tea", "type": "Drinks", "section": "Cold", "price": 4, "image": "icedtea.jpg"},
    {"name": "Orange Juice", "type": "Drinks", "section": "Cold", "price": 7, "image": "orangejuice.jpg"},
    {"name": "Apple Juice", "type": "Drinks", "section": "Cold", "price": 7, "image": "applejuice.jpg"},
    {"name": "Mineral Water", "type": "Drinks", "section": "Cold", "price": 3, "image": "mineralwater.jpg"},
    {"name": "Milkshake", "type": "Drinks", "section": "Cold", "price": 8, "image": "milkshake.jpg"}

# we can add more products or categories
]

orders = []

@app.route('/')
def index():
    return render_template('index.html', products=products, orders=orders)

if __name__ == '__main__':
    app.run(debug=True)
