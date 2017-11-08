from flask import Blueprint, render_template
import random  # for generating random numbers
import string  # for string operations

# controller for default / url prefix
homepage = Blueprint("homepage",__name__,template_folder="templates")

# Main view that shows index.html
@homepage.route("/",methods=["GET"])
def main_view():
	return render_template("homepage.html")
