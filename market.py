from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')

@app.route('/products')
def products_page():
    items = [
        {'productID': 1, 'item_name': 'Cerave Hydrating Cleanser with Hyaluronic Acid', 'quantity': '50', 'price': '9.99', 'Location': 'North London'},
        {'productID': 2, 'item_name': 'Cerave Hydrating Cleanser with Hyaluronic Acid', 'quantity': '50',
         'price': '9.99', 'Location': 'North London'},
        {'productID': 3, 'item_name': 'Cerave Hydrating Cleanser with Hyaluronic Acid', 'quantity': '50',
         'price': '9.99', 'Location': 'North London'},
        {'productID': 4, 'item_name': 'Cerave Hydrating Cleanser with Hyaluronic Acid', 'quantity': '50',
         'price': '9.99', 'Location': 'North London'},
        {'productID': 5, 'item_name': 'Cerave Hydrating Cleanser with Hyaluronic Acid', 'quantity': '50',
         'price': '9.99', 'Location': 'North London'},
    ]
    return render_template('products.html', items=items)




if __name__ == "__main__":
    app.run()