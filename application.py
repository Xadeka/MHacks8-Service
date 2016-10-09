from flask import Flask

application = Flask(__name__)

@application.route('/alexa', methods=['GET', 'POST'])
def ask_alexa():
    return 'I am processing your request'

# application.add_url_rule('/alexa', '', (lambda:
#    ask_alexa()))

# run the app.
if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    application.debug = True
    application.run()
