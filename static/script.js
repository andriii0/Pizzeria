function filterCategory(category, subsection) {
    var products = document.getElementsByClassName('product');
    for (var i = 0; i < products.length; i++) {
        var product = products[i];
        var productCategory = product.classList.contains('Pizza') ? 'Pizza' : 'Drinks';
        var productSubsection = product.classList.contains('Pizza') ?
                                (product.classList.contains('Meat') ? 'Meat' : 'Vegetarian') :
                                (product.classList.contains('Hot') ? 'Hot' : 'Cold');

        if ((category === 'all' || productCategory === category) &&
            (subsection === 'all' || productSubsection === subsection)) {
            product.style.display = 'block';
        } else {
            product.style.display = 'none';
        }
    }

    var pizzasubcategories = document.querySelector('.subcategories-pizzas');
    var drinkssubcategories = document.querySelector('.subcategories-drinks');

    if (category === 'Pizza') {
        pizzasubcategories.style.display = 'block';
        drinkssubcategories.style.display = 'none';
    } else if (category === 'Drinks') {
        pizzasubcategories.style.display = 'none';
        drinkssubcategories.style.display = 'block';
    } else {
        pizzasubcategories.style.display = 'none';
        drinkssubcategories.style.display = 'none';
    }
}

function addToCart(productName, price) {
    var xhr = new XMLHttpRequest();
    var url = "/add_to_cart?cache=" + new Date().getTime();
    xhr.open("POST", url, true);
    xhr.setRequestHeader("Content-Type", "application/json");

    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4 && xhr.status === 200) {
            var response = JSON.parse(xhr.responseText);
            updateCartUI(response.cart, response.totalAmount);
        }
    };

    var data = {
        name: productName,
        price: price
    };

    xhr.send(JSON.stringify(data));
}

function clearCart() {
    var xhr = new XMLHttpRequest();
    var url = "/clear_cart?cache=" + new Date().getTime();
    xhr.open("POST", url, true);
    xhr.setRequestHeader("Content-Type", "application/json");

    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4 && xhr.status === 200) {
            var response = JSON.parse(xhr.responseText);
            updateCartUI(response.cart, response.totalAmount);
        }
    };

    xhr.send();
}

function updateCartUI(cartItems, totalAmount) {
    var cartList = document.querySelector('.cart-panel ul');
    var totalAmountElement = document.querySelector('.cart-panel p');

    cartList.innerHTML = '';
    for (var productName in cartItems) {
        if (cartItems.hasOwnProperty(productName)) {
            var item = cartItems[productName];
            var listItem = document.createElement('li');
            listItem.textContent = item.name + ' - $' + item.price + ' x' + item.quantity;
            cartList.appendChild(listItem);
        }
    }

    totalAmountElement.textContent = 'Total amount: $' + totalAmount.toFixed(2);
}

function redirectToCheckout() {
    window.location.href = '/cart';
}

function redirectToMenu() {
    window.location.href = '/';
}

function openPaymentModal() {
    var modal = document.getElementById('payment-modal');
    modal.style.display = 'block';
}

var closeButton = document.querySelector('.close');
closeButton.addEventListener('click', function() {
    var modal = document.getElementById('payment-modal');
    modal.style.display = 'none';
});

function processPayment(method) {
    var modal = document.getElementById('payment-modal');
    modal.style.display = 'none';

    var orderedItems = [];
    var cartItems = document.querySelectorAll('.cart-panel ul li');
    cartItems.forEach(function (cartItem) {
        var itemDetails = cartItem.textContent.split(' - ');
        var itemName = itemDetails[0];
        var itemPrice = parseFloat(itemDetails[1].split(' $')[1]);
        var itemQuantity = parseInt(itemDetails[1].split(' x')[1]);
        orderedItems.push({ name: itemName, price: itemPrice, quantity: itemQuantity });
    });

    var data = {
        paymentMethod: method,
        orderedItems: orderedItems
    };

    var xhr = new XMLHttpRequest();
    var url = "/process_order";
    xhr.open("POST", url, true);
    xhr.setRequestHeader("Content-Type", "application/json");

    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4 && xhr.status === 200) {
            console.log('Order processed successfully:', xhr.responseText);
        }
    };

    xhr.send(JSON.stringify(data));
}



var modal = document.getElementById('payment-modal');
var closeButton = modal.querySelector('.close');
closeButton.addEventListener('click', function() {
    modal.style.display = 'none';
});

window.onclick = function(event) {
    if (event.target === modal) {
        modal.style.display = 'none';
    }
};

function closePaymentModal() {
    var closeButton = document.querySelector('.close');
    closeButton.addEventListener('click', closePaymentModal);
    var modal = document.getElementById('payment-modal');
    modal.style.display = 'none';
}