/*!
* Start Bootstrap - Shop Item v5.0.6 (https://startbootstrap.com/template/shop-item)
* Copyright 2013-2023 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-shop-item/blob/master/LICENSE)
*/
// This file is intentionally blank
// Use this file to add JavaScript to your project

// Récupérer le bouton "Add to cart"
// Récupérez le bouton "Add to cart"
var addToCartButton = document.querySelector('.btn.btn-outline-dark');

// Ajoutez un événement de clic au bouton
addToCartButton.addEventListener('click', function() {
    // Récupérez les informations du produit
    var productName = document.querySelector('.display-5').innerText;
    var productPrice = document.querySelector('.fs-5 span').innerText;
    var productQuantity = document.querySelector('#inputQuantity').value;

    // Créez une nouvelle ligne pour le produit dans le panier
    var newRow = document.createElement('tr');

    // Remplissez la ligne avec les informations du produit
    newRow.innerHTML = `
        <td data-th="Product">
            <div class="row">
                <div class="col-md-3 text-left">
                    <img src="https://via.placeholder.com/250x250/5fa9f8/ffffff" alt="" class="img-fluid d-none d-md-block rounded mb-2 shadow">
                </div>
                <div class="col-md-9 text-left mt-sm-2">
                    <h4>${productName}</h4>
                    <p class="font-weight-light">Brand &amp; Name</p>
                </div>
            </div>
        </td>
        <td data-th="Price">${productPrice}</td>
        <td data-th="Quantity">${productQuantity}</td>
        <td class="actions" data-th="">
            <div class="text-right">
                <button class="btn btn-white border-secondary bg-white btn-md mb-2">
                    <i class="fas fa-sync"></i>
                </button>
                <button class="btn btn-white border-secondary bg-white btn-md mb-2">
                    <i class="fas fa-trash"></i>
                </button>
            </div>
        </td>
    `;

    // Ajoutez la nouvelle ligne au tableau du panier
    var shoppingCartTable = document.querySelector('#shoppingCart tbody');
    shoppingCartTable.appendChild(newRow);
});
