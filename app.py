# Importing controllers
from controllers.main import homepage
from controllers.experience import experience
from controllers.contact_me import contact_me
from controllers.cdl import cdl
from controllers.parallax_test import parallax_test

from flask import Flask
import os
from flask.json import jsonify
from flask.json import JSONEncoder

# import libraries
import libraries.word_gen as wg
import libraries.get_crypto as gc


app = Flask(__name__)


app.register_blueprint(homepage, url_prefix='/')
app.register_blueprint(experience, url_prefix='/experience')
app.register_blueprint(contact_me, url_prefix='/contact_me')
app.register_blueprint(cdl, url_prefix='/CD-L')
app.register_blueprint(parallax_test, url_prefix='/parallax_test')


class MyEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__


@app.route("/newWord", methods=["GET", "POST"])
def make_rand_word():
    return wg.generate_word()


@app.route("/get_crypto", methods=["GET", "POST"])
def display_crypto_prices():
    retrieved_list = gc.get_crypto_prices()
    serializable = MyEncoder().encode(retrieved_list)
    return jsonify({'items': serializable})


if __name__ == "__main__":
    # Starting with these values due to c9.io
    host = os.getenv("IP", "0.0.0.0")
    port = os.getenv("PORT", 8080)
    app.secret_key = 'teststring'
    app.run(host, port)
