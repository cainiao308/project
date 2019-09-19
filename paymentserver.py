#!/usr/bin/env python
# -*- coding:utf-8 -*-

from alipay import AliPay
import  os
from flask import request , g , current_app , jsonify , session , Flask
from flask_cors import CORS


app = Flask(__name__)

CORS(app)

@app.route('/test')
def index():
    with open(os.path.join(os.path.dirname(__file__), 'api_1_0/keys/app_private_key.pem'), "r") as f:
        private_string = f.read()

    with open(os.path.join(os.path.dirname(__file__), 'api_1_0/keys/alipay.public_key.pem'), "r") as f:
        public_string = f.read()

    # data = request.get_json()
    # price = data.get('price')

    alipay_client = AliPay(
            appid="2016093000628052",
            app_notify_url=None,  # the default notify path
            app_private_key_string=private_string,
            # alipay public key, do not use your own public key!
            alipay_public_key_string=public_string,
            sign_type="RSA2", # RSA or RSA2
            debug=True  # False by default
        )

    order_string = alipay_client.api_alipay_trade_page_pay(
        out_trade_no='2222222',
        total_amount=str(1000),
        subject="租房222",
        return_url="http://10.90.94.155/orders.html",
        notify_url=None  # this is optional
    )

    ali_url = "https://openapi.alipaydev.com/gateway.do?" + order_string

    return  jsonify({"url":order_string})

app.run(host='0.0.0.0' , port=8888)
