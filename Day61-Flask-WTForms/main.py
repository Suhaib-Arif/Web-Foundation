import flask
from flask import Flask, render_template
from forms import MyForm
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)



@app.route("/",methods=["GET", "POST"])
def home():

    return render_template('index.html')


@app.route("/login", methods=["GET", "POST"])
def user_login():
    forms = MyForm(meta={'csrf': False})
    if forms.validate_on_submit():
        if forms.email.data == "admin@email.com" and forms.password.data == "12345678":
            return render_template('success.html')
        else:
            return render_template('denied.html')

    return render_template('login.html', forms=forms)


if __name__ == '__main__':
    app.run(debug=True)
