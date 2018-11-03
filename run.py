from flask import Flask
from flask import render_template
import requests
import json
from flask import jsonify
import simplejson as json
from flask import request


import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'



@app.route('/')
def index():
  return 'Specter CRUD Service'

@app.route('/test')
def test():
  return 'testssfsf'

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/returndata')
def returndata():
    data = {
    "status": "success",
    "data": [
        {
            "ImgURL": "https://www.jib.co.th/img_master/product/original/20180106132941_4.jpg",
            "Price": 1890.23424,
            "Title": "POWERSUPPLYAEROCOOL 650W AE (80+)",
            "Standard": "80+",
            "CartURL": "https://www.jib.co.th/web/index.php/cart/add/27624",
            "Max_Power": 650.234,
            "Brand": "AEROCOOL"
        },
        {
            "ImgURL": "https://www.jib.co.th/img_master/product/original/20180106132941_4.jpg",
            "Price": 1890.23424,
            "Title": "POWERSUPPLYAEROCOOL 650W AE (80+)",
            "Standard": "80+",
            "CartURL": "https://www.jib.co.th/web/index.php/cart/add/27624",
            "Max_Power": 650.234,
            "Brand": "AEROCOOL"
        }
        ]
    }
    return json.dumps(data)

@app.route('/getdata')
def getdata():
    url = 'http://localhost:8070/api/powersupply'
    response = requests.get(url)
    datas= response.json()  
    finaldata = json.dumps(datas)
    return render_template('powersupply.html',names=datas)

@app.route('/getdata2')
def getdata2():
    url = 'http://localhost:8070/api/harddisk'
    response = requests.get(url)
    datas= response.json()  
    finaldata = json.dumps(datas)
    return render_template('Harddisk.html',names=datas)

@app.route('/pushdata', methods=['POST'])
def pushdata():
    title = request.form.get('title')
    brand = request.form.get('brand')
    maxpower = request.form.get('maxpower')
    standard = request.form.get('standard')
    price = request.form.get('price')
    cart = request.form.get('cart')
    image = request.form.get('image')
    final = {"Title":title,"Brand":brand, "Max_Power":maxpower, "Standard":standard, "Price":price, "Cart":cart, "Image":image}
    return json.dumps(final)

@app.route('/pushdata2', methods=['POST'])
def pushdata2():
    title = request.form.get('title')
    brand = request.form.get('brand')
    rw = request.form.get('rwspeed')
    technology = request.form.get('technology')
    price = request.form.get('price')
    cart = request.form.get('cart')
    image = request.form.get('image')
    capacity = request.form.get('capacity')
    final = {"Title":title,"Brand":brand,"Capacity":capacity,"RW_Speed":rw, "Technology":technology, "Price":price, "Cart":cart, "Image":image}
    return json.dumps(final)
  
@app.route('/addpower')
def addpower():
    return render_template('Add_Powersupply.html')

@app.route('/addhard')
def addhard():
    return render_template('addharddisk.html')

@app.route('/addhardsubmit', methods=['POST'])
def addhardsubmit():
    title = request.form.get('title')
    brand = request.form.get('brand')
    rw = request.form.get('rwspeed')
    technology = request.form.get('technology')
    price = request.form.get('price')
    cart = request.form.get('cart')
    image = request.form.get('image')
    capacity = request.form.get('capacity')
    final = {"Title":title,"Brand":brand,"Capacity":capacity,"RW_Speed":rw, "Technology":technology, "Price":price, "Cart":cart, "Image":image}
    return json.dumps(final)  
@app.route('/addpowersubmit', methods=['POST'])
def addpowersubmit():
    title = request.form.get('title')
    brand = request.form.get('brand')
    maxpower = request.form.get('maxpower')
    standard = request.form.get('standard')
    price = request.form.get('price')
    cart = request.form.get('cart')
    image = request.form.get('image')
    final = {"Title":title,"Brand":brand, "Max_Power":maxpower, "Standard":standard, "Price":price, "Cart":cart, "Image":image}
    return json.dumps(final)

@app.route('/deletepower', methods=['POST'])
def deletepower():
    title = request.form.get('delete_title')
    return title
  
@app.route('/deletehard', methods=['POST'])
def deletehard():
    title = request.form.get('delete_title')
    return title

@app.route('/powersupplies')
def powersupply():
    return render_template('powersupply.html')

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    test = "fsdfsfs"
    return render_template('hello.html', names=test)

def create_app(config_filename):
    app.config.from_object(config_filename)
    
    from app import api_bp
    app.register_blueprint(api_bp, url_prefix='/api')

    from Model import db
    db.init_app(app)

    return app

if __name__ == "__main__":
    app = create_app("config")
    
    port = int(os.environ.get("PORT", 8070))
    # app.run(debug=True, host="0.0.0.0", threaded=True) # For debug
    app.run(host="0.0.0.0", port=port, threaded=True) # For debug
