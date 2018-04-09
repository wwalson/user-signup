from flask import Flask, request, redirect, render_template
import cgi
import os
import jinja2

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader= jinja2.FileSystemLoader
(template_dir))

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    template = jinja_env.get_template('sign_up.html')
    return template.render()

@app.route("/", methods =['POST'])
def usename():

    user_name = request.form['user_name']
    psw = request.form['psw']
    vpsw = request.form['vpsw']
    mail = request.form['mail']
    
    error_name = ''
    error_psw = ''
    error_vpsw = ''
    error_mail =''


    if len(user_name) < 3 or len(user_name) > 20 or user_name.count(' ') > 0:
        user_name = user_name
        error_name = "Not a valid Username"
    elif user_name.isspace() != 0:
        user_name = user_name
        error_name = "Not a valid Username"
    else:
        user_name = user_name
    
    if len(psw) < 3 or len(psw) > 20 or psw.count(' ') > 0:
        psw = ''
        error_psw = "Not a valid Password"
    elif psw.isspace() != 0:
        psw = ''
        error_psw = "Not a valid Password"
    else:
        psw = psw

    if psw != vpsw or len(vpsw) < 3 or len(vpsw) > 20 or vpsw.count (' ') > 0:
        psw = ''
        vpsw = ''
        error_vpsw = " Passwords do not match"
    else:
        vpsw=vpsw

    
    
    if mail == '' or mail.count('@') == 1 and mail.count ('.') == 1 and 2 < len(mail) < 21:
        mail=mail
        error_mail = ''
    else:
        mail = mail
        error_mail = "Not a valid email"
    

    if error_name=='' and error_psw == '' and error_vpsw == '' and error_mail=='':
        #success message
        usename = user_name
        return render_template('sign_up_greet.html', name=usename)

    else:
        template = jinja_env.get_template('sign_up.html')
        return template.render(error_name=error_name, error_psw=error_psw,
        error_vpsw = error_vpsw, error_mail = error_mail,user_name =user_name, 
        psw = psw, vpsw =vpsw, mail = mail)


app.run()