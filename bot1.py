import os

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

bot = ChatBot('Bot')
bot.set_trainer(ListTrainer)

for files in os.listdir('C:\makathon\data'):
             data = open('C:\makathon\data\\'+files,'r').readlines()
             bot.train(data)

while True:
        message=input('You:')
        if message.strip()!='Bye':
            reply = bot.get_response(message)
            print('Chatbot:',reply)
        if message.strip()=='Bye':
            print('Chatbot:Bye')
            break
