function filterCategory(category) {
    var products = document.getElementsByClassName('product');
    for (var i = 0; i < products.length; i++) {
        var product = products[i];
        if (category === 'all' || product.classList.contains(category)) {
            product.style.display = 'block';
        } else {
            product.style.display = 'none';
        }
    }
}

function addToCart(productName, price) {
    var cartList = document.getElementById('cart-list');
    var totalAmountElement = document.getElementById('total-amount');
    var totalAmount = parseFloat(totalAmountElement.textContent);
    totalAmount += price;
    totalAmountElement.textContent = totalAmount.toFixed(2);

    var listItem = document.createElement('li');
    listItem.textContent = productName + ' - $' + price;
    cartList.appendChild(listItem);
}
