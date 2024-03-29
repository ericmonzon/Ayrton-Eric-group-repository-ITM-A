from flask import Flask, render_template, request
import database as db

app = Flask(__name__)

# @app.route('/')
# def helloWorld():
#     return'<h1>Hello!</h1>' 

navbar = """
<a href='/'>Home</a> | <a href='/products'>Products</a> |
<a href='/branches'>Branches</a> | <a href='/aboutus'>About
Us</a>
<p/>
"""
@app.route('/')
def index():    
    return render_template('index.html', page="Index")
@app.route('/products')
def products():
    code = request.args.get('code', '')
    product_list = db.get_products()
    return render_template('products.html', page="Products", product_list=product_list)
@app.route('/productdetails')
def productdetails():
    code = request.args.get('code', '')
    product = db.get_product(int(code))
    return render_template('productdetails.html', code=code,product=product)
@app.route('/branches')
def branches():
    code = request.args.get('code', '')
    branch_list = db.get_branches()
    return render_template('branches.html', page="Branches", branch_list=branch_list)
@app.route('/branchdetails')
def branchdetails():
    code = request.args.get('code', '')
    branch = db.get_branch(int(code))
    return render_template('branchdetails.html', code=code,branch=branch)
@app.route('/aboutus')
def aboutus():
    return render_template('aboutus.html', page="About Us")
