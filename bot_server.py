import os
from flask import Flask, request, jsonify, send_from_directory
from configs.response_handler import get_bot_response
from flask_cors import CORS

app = Flask(__name__, static_folder="server", static_url_path="")
CORS(app)

@app.route("/")
def index():
    return send_from_directory(app.static_folder, "index.html")

@app.route("/get", methods=["GET"])
def get_response():
    user_msg = request.args.get("msg")
    search = request.args.get("search") == "true"
    calculate = request.args.get("calculate") == "true"
    response = get_bot_response(user_msg, search=search, calculate=calculate)
    return jsonify({"response": response})


# Feedback server
feedback_app = Flask("feedback_server")
CORS(feedback_app)

@feedback_app.route("/", methods=["GET"])
def feedback_form():
    return '''
    <form method="POST">
        <h2>Feedback Form</h2>
        Name: <input name="name"><br>
        Description: <textarea name="desc"></textarea><br>
        Rating: <input name="rating"><br>
        <button type="submit">Submit</button>
    </form>
    '''

@feedback_app.route("/", methods=["POST"])
def save_feedback():
    name = request.form.get("name")
    desc = request.form.get("desc")
    rating = request.form.get("rating")

    os.makedirs("feedback", exist_ok=True)
    filename = os.path.join("feedback", f"{name.replace(' ', '_')}_feedback.txt")
    with open(filename, "w") as f:
        f.write(f"Name: {name}\nDescription: {desc}\nRating: {rating}")
    return "Thank you for your feedback!"


def print_banner():
    os.system("clear" if os.name != "nt" else "cls")
    print("\033[1;36m")
    print("██╗  ██╗   ███╗   ███╗   ███████╗")
    print("██║ ██╔╝   ████╗ ████║   ██╔════╝")
    print("█████╔╝    ██╔████╔██║   ███████╗")
    print("██╔═██╗    ██║╚██╔╝██║   ╚════██║")
    print("██║  ██╗██╗██║ ╚═╝ ██║██╗███████║")
    print("╚═╝  ╚═╝╚═╝╚═╝     ╚═╝╚═╝╚══════╝")
    print("\033[0m")
    print("[ * ] Feedback Server running successfully")
    print("[ * ] Access feedback page at: http://127.0.0.1:5001/")
    print("[ * ] Chatbot running at: http://127.0.0.1:5000/")

if __name__ == "__main__":
    from threading import Thread
    print_banner()
    Thread(target=lambda: feedback_app.run(port=5001)).start()
    app.run(port=5000)
