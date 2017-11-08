from flask import Blueprint, render_template

# controller for default / url prefix
experience = Blueprint("experience",__name__,template_folder="templates")

@experience.route('/', methods=['GET', 'POST'])
def experience_view():
    return render_template('experience.html')