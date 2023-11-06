from flask import Flask, render_template, session, request, jsonify
import json


app = Flask(__name__)
app.secret_key = 'Mario&Luigi!'



with open('static/menu.json', 'r') as json_file:
    menu_data = json.load(json_file)

for product in menu_data['menu']:
    name = product['name']
    product_type = product['type']
    section = product['section']
    price = product['price']
    image = product['image']
    description = product['desc']
#all the images are 800x800. To fill the webpage just google "product name" 800x800

@app.route('/')
def index():
    cart_items = session.get('cart', {}).values()
    total_price = sum(item['price'] * item['quantity'] for item in cart_items)
    return render_template('index.html', products=menu_data['menu'], cart_items=cart_items, total_price=total_price)

@app.route('/cart')
def cart():
    cart_items = session.get('cart', {}).values()
    total_price = sum(item['price'] * item['quantity'] for item in cart_items)
    return render_template('cart.html', cart_items=cart_items, total_price=total_price)


@app.route('/add_to_cart', methods=['POST'])
def add_to_cart():
    data = request.get_json()
    product_name = data.get('name')
    price = data.get('price')

    cart = session.get('cart', {})

    # If product is already in cart, update the quantity
    if product_name in cart:
        cart[product_name]['quantity'] += 1
    else:
        # If product is not in cart, add it as a dictionary
        cart[product_name] = {'price': price, 'quantity': 1, 'name': product_name}

    session['cart'] = cart

    total_amount = sum(item['price'] * item['quantity'] for item in cart.values())
    return jsonify(cart=session['cart'], totalAmount=total_amount)

@app.route('/process_order', methods=['POST'])
def process_order():
    data = request.get_json()
    payment_method = data.get('paymentMethod')
    ordered_items = data.get('orderedItems')

    for item in ordered_items:
        item_name = item['name']
        item_quantity = item['quantity']
        item_price = item['price']
        print(f"Item: {item_name}, Quantity: {item_quantity}")

    # Process the payment and handle other order-related tasks here

    return jsonify(message="Order processed successfully")
@app.route('/clear_cart', methods=['POST'])
def clear_cart():
    session['cart'] = {}
    total_amount = 0
    return jsonify(cart=session['cart'], totalAmount=total_amount)

if __name__ == '__main__':
    app.run(debug=True)