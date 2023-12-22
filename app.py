from flask import Flask, app, render_template, request, url_for, redirect

from flask import Flask
app = Flask(__name__)






@app.route('/')
def home():
    return render_template ('home.html')




@app.route('/login_menu')
@login_required
def login_menu():
    return render_template ('login_menu.html')


@app.route('/menu')
def menu():
    return render_template ('menu.html')


@app.route('/enquete')
def enquete():
    return render_template ('enquete.html')


@app.route('/enquete_lounge')
def enquete_lounge():
    return render_template ('lounge.html')


@app.route('/metingen')
def metingen():
     return render_template ('metingen.html')




if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')


