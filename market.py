from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
db = SQLAlchemy(app)

class Item(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=30), nullable=False, unique=True)
    price = db.Column(db.Integer(), nullable=False)
    barcode = db.Column(db.String(length=12), nullable=False, unique=True)
    description = db.Column(db.String(length=1024), nullable=False, unique=True)

    def __repr__(self):
        return f'Item {self.name}'

@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')

@app.route('/')
@app.route('/login')
def login_page():
    return render_template('login.html')


@app.route('/')
@app.route('/checkout')
def checkout_page():
    return render_template('checkout.html')


@app.route('/products')
def products_page():
    items = [
        {'productID': 1, 'item_name': 'Cerave Hydrating Cleanser with Hyaluronic Acid', 'quantity': '50', 'price': '9.99', 'Location': 'North London'},
        {'productID': 2, 'item_name': 'Simple Kind To Skin Cleansing Wipes Biodegradable X50', 'quantity': '50', 'price': '9.99', 'Location': 'North London'},
        {'productID': 3, 'item_name': 'Simple Kind to Skin Refreshing Facial Wash Gel 50ml', 'quantity': '50', 'price': '9.99', 'Location': 'North London'},
        {'productID': 4, 'item_name': 'CeraVe Moisturising Lotion For Dry to Very Dry Skin 236ml', 'quantity': '50', 'price': '9.99', 'Location': 'North London'},
        {'productID': 5, 'item_name': "Burt's Bees® Beeswax Lip Balm 4.25g", 'quantity': '50', 'price': '9.99', 'Location': 'North London'},
        {'productID': 6, 'item_name': "NYX Professional Makeup Setting Spray Matte", 'quantity': '50', 'price': '9.99',
         'Location': 'North London'},
        {'productID': 7, 'item_name': "NYX Professional Makeup Micro Brow Pencil (Various Shades)", 'quantity': '50', 'price': '9.99',
         'Location': 'North London'},
        {'productID': 8, 'item_name': "NYX Professional Makeup Butter Gloss - Praline", 'quantity': '50', 'price': '9.99','Location': 'North London'},
        {'productID': 9, 'item_name': "Maybelline Lash Sensational Sky High Mascara 01 Black", 'quantity': '50', 'price': '9.99','Location': 'North London'},
        {'productID': 10, 'item_name': "NYX Professional Makeup Suede Matte Lip Liner (Various Shades)", 'quantity': '50', 'price': '9.99','Location': 'North London'},
        {'productID': 11, 'item_name': "Always Maxi Long Plus Sanitary Towels x12",'quantity': '50', 'price': '9.99', 'Location': 'North London'},
        {'productID': 12, 'item_name': "Always Ultra Secure Night Duo Sanitary Towels Multipack 18",'quantity': '50', 'price': '9.99', 'Location': 'North London'},
        {'productID': 13, 'item_name': "Always Sensitive Normal Ultra (Size 1) Sanitary Towels x16",'quantity': '50', 'price': '9.99', 'Location': 'North London'},
        {'productID': 14, 'item_name': "Tampax Compak Regular Tampons 18",'quantity': '50', 'price': '9.99', 'Location': 'North London'},
        {'productID': 15, 'item_name': "OrganiCup, Size A, Menstrual Cup, 1 unit", 'quantity': '50', 'price': '9.99', 'Location': 'North London'},
        {'productID': 16, 'item_name': "Bodyform So Slim Pantyliners 34 Pack", 'quantity': '50', 'price': '9.99', 'Location': 'North London'},
        {'productID': 17, 'item_name': "Tampax Compak Lite Applicator Tampon Single 18PK", 'quantity': '50','price': '9.99', 'Location': 'North London'},

    ]
    return render_template('products.html', items=items)


if __name__ == "__main__":
    app.run()