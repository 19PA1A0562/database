from flask import Flask,render_template,flash, redirect,url_for,session,logging,request
from flask_sqlalchemy import SQLAlchemy


"""from chatterbot import ChatBot 
from chatterbot.trainers import ChatterBotCorpusTrainer,ListTrainer
english_bot = ChatBot('corona bot')
english_bot = ChatBot(
              'Buddy',
              storage_adapter='chatterbot.storage.SQLStorageAdapter',
              database_uri='sqlite:///database.sqlite3'
             
)

trainer =  ListTrainer(english_bot)
trainer.train(['helo',
                'How can I help you?',
                'I want to write a quiz',
                'oh Great,type quiz and get ready for quiz',
                'How are you?',
                'I am fine, How can I help you?',
                'May i know your name?',
                'My name is Quizbot .I am there to conduct quizes',
                'Thankyou',
                'Not a problem visit our bot again',
                'bye',
                'bye have a good day .see u again.'])

trainer = ChatterBotCorpusTrainer(english_bot)
trainer.train("chatterbot.corpus.english")


@app.route("/get")
def get_bot_response():
    usertext = request.args.get('msg')
    return str(english_bot.get_response(usertext))






"""



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/Ramanaidu/Documents/DB/example.db'
db = SQLAlchemy(app)


class user(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    email = db.Column(db.String(120))
    password = db.Column(db.String(80))

@app.route("/")
def index():
    return render_template("homepage.html")



@app.route("/login",methods=["GET", "POST"])
def login():
    if request.method == "POST":
        uname = request.form["uname"]
        passw = request.form["passw"]
        
        login = user.query.filter_by(username=uname, password=passw).first()
        if login is not None:
            return redirect(url_for("base"))
        return render_template("loginwrong.html")
    return render_template("login.html")


@app.route("/loginwrong")
def loginpage():
    return render_template("loginwrong.html")



@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        uname = request.form['uname']
        mail = request.form['mail']
        passw = request.form['passw']

        register = user(username = uname, email = mail, password = passw)
        register1= user.query.filter_by(username=uname, email =mail, password=passw).first()
        if register1 is not None:
            return render_template("registercompleted.html")
        db.session.add(register)
        db.session.commit()
        return redirect(url_for("login"))
    return render_template("register.html")
@app.route("/base")
def base():
    return render_template("base.html")



if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)
