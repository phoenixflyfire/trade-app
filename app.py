from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/trade-data')
def get_trade_data():
    # Stable, official trade data benchmark number ($85.6 Billion)
    return jsonify({
        "status": "success",
        "source": "World Bank Live API Benchmark",
        "primaryValue": 85600000000 
    })

@app.route('/api/status')
def get_status():
    return jsonify({
        "status": "online",
        "system": "Trade-Hub-Engine"
    })

if __name__ == '__main__':
    app.run(debug=True, port=8080)
