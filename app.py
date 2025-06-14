from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allows requests from your frontend

# 🔍 Simple keyword extraction
def extract_keyword(message):
    words = message.strip().split()
    return words[-1] if words else "product"

@app.route('/search', methods=['POST'])
def search():
    data = request.get_json()
    message = data.get("message", "")
    keyword = extract_keyword(message)

    # 🧪 Dummy product data (later replace with API result)
    product = {
        "name": f"Best deal for {keyword}",
        "price": "₹1,499",
        "link": f"https://www.amazon.in/s?k={keyword}&tag=your-affiliate-id",
        "image": "https://via.placeholder.com/150"
    }

    return jsonify({
        "response": f'I found a great deal for "{keyword}"!',
        "product": product
    })

if __name__ == '__main__':
    app.run(debug=True)
