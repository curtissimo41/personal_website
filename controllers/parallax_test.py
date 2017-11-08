from flask import Blueprint, render_template, request

# controller for default / url prefix
parallax_test = Blueprint("parallax_test",__name__,template_folder="templates")

@parallax_test.route('/', methods=['GET', 'POST'])
def parallax():
    return render_template('parallax_test.html')