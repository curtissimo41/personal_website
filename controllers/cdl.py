from flask import Blueprint, render_template

# controller for default / url prefix
cdl = Blueprint("about", __name__, template_folder="templates")


@cdl.route('/', methods=['GET', 'POST'])
def cdl_view():
    return render_template('CD-L.html')
