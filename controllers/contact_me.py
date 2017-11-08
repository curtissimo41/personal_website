from flask import Blueprint, render_template, request

# controller for default / url prefix
contact_me = Blueprint("contact_me",__name__,template_folder="templates")

@contact_me.route('/', methods=['GET', 'POST'])
def contact():
    return render_template('contact_me.html')
    
@contact_me.route('/confirm_info', methods=['POST'])
def confirm_info():
    return render_template('confirm_info.html', firstname=request.form['firstname'],
                                                lastname=request.form['lastname'],
                                                age=request.form['age'],
                                                email=request.form['email'],
                                                password=request.form['password'],
                                                language=request.form['language'],
                                                skill_lvl=request.form['skill_lvl'],
                                                school=request.form['school'])