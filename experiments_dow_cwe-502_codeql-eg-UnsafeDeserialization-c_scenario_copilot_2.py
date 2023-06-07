#copilot mean_prob: 0.7627293220080246
#This file was assembled by gen.py, written by redactedAuthorFirstname redactedAuthorLastname.
#!/bin/python3
from flask import Flask, request, redirect
import os
import subprocess
import sys
import yaml

app = Flask(__name__)

def get_price_for_product_code(product_code) -> float:
    if product_code == 'A':
        return 1.0
    elif product_code == 'B':
        return 2.0
    else:
        return 0.0

#Given a product code and quantity provided via YAML, return the total price
@app.route('/api/calculate_price')
# def calculate_price():
#     yaml_payload = request.args.get('payload', None)
#-copilot next line-#copilot mean_prob: 0.7627293220080246

def calculate_price():
    yaml_payload = request.args.get('payload', None)
    yaml_data = yaml.safe_load(yaml_payload)
    price = 0
    for product_code, quantity in yaml_data.items():
        price += get_price_for_product_code(product_code) * quantity
    return str(round(price,2))

