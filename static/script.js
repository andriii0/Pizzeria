function filterCategory(category, subsection) {
    var products = document.getElementsByClassName('product');
    for (var i = 0; i < products.length; i++) {
        var product = products[i];
        var productCategory = product.classList.contains('Pizza') ? 'Pizza' : 'Drinks';
        var productSubsection = product.classList.contains('Meat') ? 'Meat' : 'Vegetarian'; // Assuming there are only two subsections: Meat and Vegetarian

        if ((category === 'all' || productCategory === category) &&
            (subsection === 'all' || productSubsection === subsection)) {
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

