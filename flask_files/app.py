from flask import Flask, jsonify, render_template
app = Flask(__name__)

@app.route('/')
def index():
    try:
        return render_template('index.html')

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
	app.run(host="127.0.0.1", port=8080, debug=True)

