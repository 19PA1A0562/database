from flask import Flask, render_template,request

#from chatterbot import ChatBot 
#from chatterbot.trainers import ChatterBotCorpusTrainer,ListTrainer
#english_bot = ChatBot('corona bot')
#english_bot = ChatBot(
 #             'Buddy',
  #            storage_adapter='chatterbot.storage.SQLStorageAdapter',
   #           database_uri='sqlite:///database.sqlite3'
             
#)

#trainer =  ListTrainer(english_bot)
#trainer.train(['helo',
 #               'How can I help you?',
  #              'I want to write a quiz',
   #             'oh Great,type quiz and get ready for quiz',
    #            'How are you?',
     #           'I am fine, How can I help you?',
      #          'May i know your name?',
       #         'My name is Quizbot .I am there to conduct quizes',
        #        'Thankyou',
         #       'Not a problem visit our bot again',
          #      'bye',
           #     'bye have a good day .see u again.'])

#trainer = ChatterBotCorpusTrainer(english_bot)
#trainer.train("chatterbot.corpus.english")

app=Flask(__name__)
@app.route("/")
def home():
    return render_template("base.html")

#@app.route("/get")
#def get_bot_response():
 #   usertext = request.args.get('msg')
    #return str(english_bot.get_response(usertext))
 
 
if __name__ == "__main__":
    app.run()
