from chatterbot import ChatBot
from flask import Flask

app = Flask(__name__)

@app.route('/abc/<string:question>', methods=['GET'])
def get_answer(question):
    reply = ''
    bot = ChatBot('Bot',read_only=True,
                  logic_adapters=[
                      {
                          'import_path': 'chatterbot.logic.BestMatch'
                      },
                      {
                          'import_path': 'chatterbot.logic.LowConfidenceAdapter',
                          'threshold': 0.65,
                          'default_response': 'I am sorry, but I do not understand.'
                      }
                  ],
                  trainer='chatterbot.trainers.ListTrainer')
    print('you asked: '+ question)
    message = question

    if message.strip() != 'Bye':
        reply = bot.get_response(message)
        reply = 'Chatbot:'+ str(reply)

    if message.strip().lower() == 'bye':
        reply = 'Chatbot:Bye'

    return reply

app.run(debug=True)

