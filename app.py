from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Lista de moedas disponíveis
coins_list = ['bitcoin', 'ethereum', 'litecoin', 'dogecoin', 'ripple']

@app.route('/', methods=['GET'])
def index():
    coin = request.args.get('coin', 'bitcoin')
    if coin not in coins_list:
        coin = 'bitcoin'
    
    url = f'https://api.coingecko.com/api/v3/coins/{coin}/market_chart?vs_currency=usd&days=7'
    response = requests.get(url).json()
    prices = response.get('prices', [])
    
    labels = [p[0] for p in prices]
    data = [p[1] for p in prices]
    
    return render_template('index.html', labels=labels, data=data, coin=coin, coins_list=coins_list)
    
if __name__ == '__main__':
    app.run(debug=True)
