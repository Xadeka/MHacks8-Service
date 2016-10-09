from flask import Flask

app = Flask(__name__)

@app.route('/alexa', methods=['GET', 'POST'])
def ask_alexa():
    return 'I am processing your request'

# run the app.
if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    app.debug = True
    app.run()
