// cart.js

// Initialize cart from local storage or create a new one
let cart = JSON.parse(localStorage.getItem('cart')) || [];

// Save the cart back to local storage
function saveCart() {
    localStorage.setItem('cart', JSON.stringify(cart));
}

// Add item to cart
function addToCart(id, title, price, dis_price, image) {
    let cartItems = JSON.parse(localStorage.getItem('cart')) || [];
    const existingItemIndex = cartItems.findIndex(item => item.id === id);

    if (existingItemIndex > -1) {
        // If the item already exists in the cart, increase the quantity
        cartItems[existingItemIndex].quantity += 1;
    } else {
        // If the item is new, add it to the cart
        cartItems.push({
            id: id,
            title: title,
            price: dis_price || price,
            image: image,
            quantity: 1
        });
    }

    // Save the updated cart back to local storage
    localStorage.setItem('cart', JSON.stringify(cartItems));

    // Update the cart count in the header
    updateCartCount();
}

function updateCartCount() {
    const cartItems = JSON.parse(localStorage.getItem('cart')) || [];
    const cartCount = cartItems.reduce((total, item) => total + (item.quantity || 1), 0);
    document.getElementById('cart-count').textContent = cartCount;
}

// Remove item from cart
function removeFromCart(id) {
    cart = cart.filter(item => item.id !== id);
    saveCart();
}

// Retrieve items in cart
function getCartItems() {
    return cart;
}

// Clear cart
function clearCart() {
    cart = [];
    saveCart();
}

// Display cart items (example for displaying in console)
function displayCart() {
    console.log("Your Cart:", cart);
}