from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

responses = {

    "hello": "Hello! Welcome to Pizza Outlet 🍕",

    "hi": "Hi there 👋",

    "menu": "Chicken Pizza, Cheese Pizza, Pepperoni Pizza 🍕",

    "price": "Small = $5, Medium = $8, Large = $12 💰",

    "offers": "Buy 1 Get 1 Free 🔥",

    "drink": "Coke, Pepsi, Sprite 🥤",

    "burger": "Yes! Burgers available 🍔",

    "fries": "Crispy fries available 🍟",

    "delivery": "Home delivery available 🚗",

    "location": "We are in Main City Center 📍",

    "order chicken pizza": "Chicken Pizza ordered successfully ✅",

    "order cheese pizza": "Cheese Pizza ordered successfully ✅",

    "thanks": "You're welcome ❤️",

    "bye": "Thank you for visiting Pizza Outlet 👋"
}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get", methods=["POST"])
def chatbot():

    user_message = request.form["msg"].lower()

    response = responses.get(
        user_message,
        "Sorry, I didn't understand 😅"
    )

    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True)