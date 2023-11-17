from flask import Flask, app, render_template, request, url_for, redirect, send_file, flash
from flask_sqlalchemy import SQLAlchemy

from flask import Flask
app = Flask(__name__)



from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os

import os

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://helmerc:6h7#e61CfWEFl#@oege.ie.hva.nl/zhelmerc"
app.config['SQLAlchemy TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'sdjhdjhsnkdnkdsnkshuhuhnn'
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'connect_args': {'ssl':{'fake_flag_to_enable_tls':True}}}
db = SQLAlchemy(app)



from io import BytesIO
import os
from flask import Flask, render_template, request, url_for, redirect, send_file, flash,session
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
from flask_login import UserMixin
from flask_login import login_required, current_user, logout_user
from werkzeug.security import generate_password_hash, check_password_hash

from flask_login import login_user

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

login_manager = LoginManager()



login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.init_app(app)

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(10000))
    name = db.Column(db.String(1000))

@login_manager.user_loader
def load_user(user_id):
   return User.query.get(int(user_id))


#login route 
@app.route('/login')
def login():
    return render_template('login.html')


#login route wannneer er wat verstuurd word
@app.route('/login', methods=['POST'])
def login_add():

    # haal de login code op
    email = request.form.get('email')
    password = request.form.get('password')
    
    user = User.query.filter_by(email=email).first()
   
    # vergelijk wachtwoord en hash het wachtwoord 
    if not user or not check_password_hash(user.password, password):
        # geef flash melding wanneer de user name of wachtwoord niet klopt
        flash('Please check your login details and try again.')
        # stuur hem naar de login terug
        return redirect(url_for('login')) 
    # wanneer user name en passwoord wel klopt geef user mee en redirect hem naar de pagina page
    login_user(user)
    return redirect(url_for('login_menu'))

# logout functie
@app.route('/logout')
@login_required
def logout():
    # haal de user uit de sessie
    logout_user()
    # stuur de user terug naar het login scherm
    return redirect(url_for('login'))


@app.route('/signup')
def signup():
    return render_template('signup.html')

# sign up pagina als er wat word verstuurd
@app.route('/signup', methods=['POST'])
def signup_post():
    # haal gegevens op die verstuurd zijn
    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')

# vergelijkt email in database of deze al bestaad 
    user = User.query.filter_by(email=email).first() 
    if user: 
        # als user al bestaad stuur hem terug naar de signup route
        return redirect(url_for('signup'))

    # maak user aan in user tabel en hash het wachtwoord zodat deze niet te lezen is in de database
    new_user = User(email=email, name=name, password=generate_password_hash(password, method='sha256'))

    # voeg nieuwe user toe
    db.session.add(new_user)
    db.session.commit()
    # stuur hem naar de login
    return redirect(url_for('login'))





class Metingen_Lounge_table(db.Model):
     id = db.Column(db.Integer, primary_key=True)
     naam_klant = db.Column(db.String(100), nullable=False)
     taal_klant = db.Column(db.String(100), nullable=False)
     soort_klant = db.Column(db.String(100), nullable=False)
     gem_leeftijd = db.Column(db.String(100), nullable=False)
     medewerker_id = db.Column(db.String(100), nullable=False)
     tafel_id = db.Column(db.String(100), nullable=False)  
     tafel_gestuurd_op_starttijd = db.Column(db.String(100), nullable=False)
     minuten_na_starttijd_sec  = db.Column(db.String(100), nullable=False)
     demonstratie_scherm_sec     = db.Column(db.String(100), nullable=False)
     is_er_uitleg_golf  = db.Column(db.String(100), nullable=False)
     uitleg_golf_tijd_sec      = db.Column(db.String(100), nullable=False)
     opnemen_sec   = db.Column(db.String(100), nullable=False)
     bereiden_sec = db.Column(db.String(100), nullable=False)
     klant_vetrekt_op_eindtijd = db.Column(db.String(100), nullable=False)
     klant_vetrek_eindtijd_sec   = db.Column(db.String(100), nullable=False)
     betaald =  db.Column(db.String(100), nullable=False)  
     betaalwijze =  db.Column(db.String(100), nullable=False)  
     afrekenen_sec =  db.Column(db.String(100), nullable=False)
     clubs_gesorteerd = db.Column(db.String(100), nullable=False)  
     clubs_sorteren_sec = db.Column(db.String(100), nullable=False)
     tafel_schoon_tijd_sec     = db.Column(db.String(100), nullable=False)
     
     def __repr__(self):
          return f'Response {self.name}'
     


     
     @app.route("/submit_metingen", methods=["POST"])
     def submit_metingen():
          naam_klant = request.form['naam_klant']
          taal_klant = request.form['taal_klant']
          soort_klant = request.form['soort_klant']
          gem_leeftijd = request.form['gem_leeftijd']
          medewerker_id = request.form['medewerker_id']
          tafel_id = request.form['tafel_id']
          tafel_gestuurd_op_starttijd = request.form['tafel_gestuurd_op_starttijd']
          minuten_na_starttijd_sec = request.form['minuten_na_starttijd_sec']
          demonstratie_scherm_sec = request.form['demonstratie_scherm_sec']
          is_er_uitleg_golf = request.form['is_er_uitleg_golf']
          uitleg_golf_tijd_sec = request.form['uitleg_golf_tijd_sec']
          opnemen_sec = request.form['opnemen_sec']
          bereiden_sec = request.form['bereiden_sec']
          klant_vetrekt_op_eindtijd = request.form['klant_vetrekt_op_eindtijd']
          klant_vetrek_eindtijd_sec = request.form['klant_vetrek_eindtijd_sec']
          betaald = request.form['betaald']
          betaalwijze = request.form['betaalwijze']
          afrekenen_sec = request.form['afrekenen_sec']
          clubs_gesorteerd = request.form['clubs_gesorteerd']
          clubs_sorteren_sec = request.form['clubs_sorteren_sec']
          tafel_schoon_tijd_sec = request.form['tafel_schoon_tijd_sec']

          metingen = Metingen_Lounge_table(naam_klant=naam_klant, taal_klant=taal_klant, soort_klant=soort_klant, gem_leeftijd=gem_leeftijd, medewerker_id=medewerker_id,tafel_id=tafel_id,
                              tafel_gestuurd_op_starttijd=tafel_gestuurd_op_starttijd, minuten_na_starttijd_sec=minuten_na_starttijd_sec, demonstratie_scherm_sec=demonstratie_scherm_sec,
                              is_er_uitleg_golf= is_er_uitleg_golf, uitleg_golf_tijd_sec=uitleg_golf_tijd_sec, opnemen_sec=opnemen_sec, bereiden_sec=bereiden_sec,
                              klant_vetrekt_op_eindtijd=klant_vetrekt_op_eindtijd, klant_vetrek_eindtijd_sec=klant_vetrek_eindtijd_sec, betaald=betaald, betaalwijze=betaalwijze,
                              afrekenen_sec=afrekenen_sec, clubs_gesorteerd=clubs_gesorteerd, clubs_sorteren_sec=clubs_sorteren_sec, tafel_schoon_tijd_sec=tafel_schoon_tijd_sec) 
          
          
          db.session.add(metingen)
          db.session.commit()

          flash('De Metingen zijn goed verstuurd')

          return redirect(url_for('metingen')) 
       

class Enquete_lounge(db.Model):
     id = db.Column(db.Integer, primary_key=True)
     question_1 = db.Column(db.String(100), nullable=False)
     question_2 = db.Column(db.String(100), nullable=False)
     question_3 = db.Column(db.String(100), nullable=False)
     question_4 = db.Column(db.String(100), nullable=False)
     question_5 = db.Column(db.String(100), nullable=False)
     question_6 = db.Column(db.String(100), nullable=False)
     question_7 = db.Column(db.String(100), nullable=False)
     question_8 = db.Column(db.String(100), nullable=False)
     question_9 = db.Column(db.String(100), nullable=False)
     question_10 = db.Column(db.String(100), nullable=False)
     question_11 = db.Column(db.String(100), nullable=False)
     question_12 = db.Column(db.String(100), nullable=False)

     def __repr__(self):
          return f'Response {self.name}'
     
     @app.route("/submit_lounge", methods=["POST"])
     def submit_lounge():
       
        question_1 = request.form['question_1']
        question_2 = request.form['question_2']
        question_3 = request.form['question_3']
        question_4 = request.form['question_4']
        question_5 = request.form['question_5']
        question_6 = request.form['question_6']
        question_7 = request.form['question_7']
        question_8 = request.form['question_8']
        question_9 = request.form['question_9']
        question_10 = request.form['question_10']
        question_11 = request.form['question_11']
        question_12 = request.form['question_12']
    
      

        enquete_lounge = Enquete_lounge(question_1=question_1, question_2=question_2, question_3=question_3, question_4=question_4, question_5=question_5, 
                                        question_6=question_6, question_7=question_7, question_8=question_8, question_9=question_9, question_10=question_10,
                                          question_11=question_11, question_12=question_12)

        db.session.add(enquete_lounge)
        db.session.commit()

        flash('Bedankt voor uw medewerking')

        return redirect(url_for('enquete_lounge')) 



     
          

class Enquete(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        vraag_1 = db.Column(db.String(100), nullable=False)
        vraag_2 = db.Column(db.String(100), nullable=False)
        vraag_3 = db.Column(db.String(100), nullable=False)
        vraag_4 = db.Column(db.String(100), nullable=False)
        vraag_5 = db.Column(db.String(100), nullable=False)
        vraag_6 = db.Column(db.String(100), nullable=False)
        vraag_7 = db.Column(db.String(100), nullable=False)
        vraag_8 = db.Column(db.String(100), nullable=False)
        vraag_9 = db.Column(db.String(100), nullable=False)
        vraag_10 = db.Column(db.String(100), nullable=False)
        vraag_11 = db.Column(db.String(100), nullable=False)
        vraag_12 = db.Column(db.String(100), nullable=False)
        vraag_13 = db.Column(db.String(100), nullable=False)
        vraag_14 = db.Column(db.String(100), nullable=False)
        vraag_15 = db.Column(db.String(100), nullable=False)
        vraag_16 = db.Column(db.String(100), nullable=False)
        vraag_17 = db.Column(db.String(100), nullable=False)
        vraag_18 = db.Column(db.String(100), nullable=False)
        vraag_19 = db.Column(db.String(100), nullable=False)
        vraag_20 = db.Column(db.String(100), nullable=False)

        def __repr__(self):
            return f'Response {self.name}'
    
@app.route("/submit", methods=["POST"])
def submit():
       
        vraag_1 = request.form['vraag_1']
        vraag_2 = request.form['vraag_2']
        vraag_3 = request.form['vraag_3']
        vraag_4 = request.form['vraag_4']
        vraag_5 = request.form['vraag_5']
        vraag_6 = request.form['vraag_6']
        vraag_7 = request.form['vraag_7']
        vraag_8 = request.form['vraag_8']
        vraag_9 = request.form['vraag_9']
        vraag_10 = request.form['vraag_10']
        vraag_11 = request.form['vraag_11']
        vraag_12 = request.form['vraag_12']
        vraag_13 = request.form['vraag_13']
        vraag_14 = request.form['vraag_14']
        vraag_15 = request.form['vraag_15']
        vraag_16 = request.form['vraag_16']
        vraag_17 = request.form['vraag_17']
        vraag_18 = request.form['vraag_18']
        vraag_19 = request.form['vraag_19']
        vraag_20 = request.form['vraag_20']
      

        enquete = Enquete(vraag_1=vraag_1, vraag_2=vraag_2, vraag_3=vraag_3, vraag_4=vraag_4, vraag_5=vraag_5, 
                          vraag_6=vraag_6, vraag_7=vraag_7, vraag_8=vraag_8, vraag_9=vraag_9, vraag_10=vraag_10, 
                          vraag_11=vraag_11, vraag_12=vraag_12, vraag_13=vraag_13, vraag_14=vraag_14, vraag_15=vraag_15, 
                          vraag_16=vraag_16, vraag_17=vraag_17, vraag_18=vraag_18, vraag_19=vraag_19, vraag_20=vraag_20)

        db.session.add(enquete)
        db.session.commit()

        flash('Bedankt voor uw medewerking')

        return redirect(url_for('enquete')) 

    
app.config['UPLOAD_FOLDER'] = 'static/image' 

class Dishes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    taal = db.Column(db.String(255), nullable=False)
    vega = db.Column(db.String(255), nullable=False)
    name = db.Column(db.String(255), nullable=False)
    price = db.Column(db.String(255), nullable=False)
    plant_based = db.Column(db.String(120), nullable=False)
    description = db.Column(db.String(255))
    category = db.Column(db.String(120), nullable=False)
    allergies = db.Column(db.String(100), nullable=False)
    image_filename = db.Column(db.String(250))
    
    def __init__(self,taal, name, vega, price, plant_based, description, category, allergies, image_filename=None):
        self.taal = taal
        self.vega = vega
        self.name = name
        self.price = price
        self.plant_based = plant_based
        self.description = description
        self.category = category
        self.allergies = allergies 
        self.image_filename = image_filename
    
    def __repr__(self):
        return f'Dishes({self.name}, {self.category})'

@app.route('/add_dishes', methods=['GET', 'POST'])
@login_required
def add_dishes():
    if request.method == 'POST':
        taal = request.form['taal']
        name = request.form['name']
        price = float(request.form['price']) 
        description = request.form['description']
        category = request.form['category']

        
        values_vega = request.form.getlist('vega')
        values_plant_based = request.form.getlist('plant_based')
        values_allergies = request.form.getlist('allergies')
        

        # lijst van geselecteerde waarden naar lijst
        vega = ' '.join(values_vega)
        plant_based = ' '.join(values_plant_based)
        allergies = ' '.join(values_allergies)

        if 'image' in request.files:
            image = request.files['image']
            if image:
                filename = image.filename
                image.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            else:
                filename = None
        else:
            filename = None

        dishes = Dishes(taal=taal, name=name, vega=vega, price=price, plant_based=plant_based, description=description, category=category, allergies=allergies, image_filename=filename)
        db.session.add(dishes)
        db.session.commit()

        flash('U gerecht is toegevoegd')


        return redirect(url_for('add_dishes'))

    return render_template('add_dish.html')





@app.route('/dishes')
def dishes():
    taal = request.args.get('taal', 'nl')

    voorgerechten = Dishes.query.filter_by(category='voorgerecht', taal=taal) .all()
    hoofdgerechten = Dishes.query.filter_by(category='hoofdgerecht', taal=taal).all()
    nagerechten = Dishes.query.filter_by(category='nagerecht',  taal=taal).all()
    
    return render_template('dish.html',voorgerechten=voorgerechten, hoofdgerechten=hoofdgerechten, nagerechten=nagerechten)

     

@app.route('/dishes_english')
def dishes_english():
    taal = request.args.get('taal', 'eng')

    voorgerechten = Dishes.query.filter_by(category='voorgerecht', taal=taal) .all()
    hoofdgerechten = Dishes.query.filter_by(category='hoofdgerecht', taal=taal).all()
    nagerechten = Dishes.query.filter_by(category='nagerecht',  taal=taal).all()
    
    return render_template('dish_english.html',voorgerechten=voorgerechten, hoofdgerechten=hoofdgerechten, nagerechten=nagerechten)

     




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




# Gebruikte bronnen (alle bronnen bevatte uitleg):
# - digital oceaan (authentication)