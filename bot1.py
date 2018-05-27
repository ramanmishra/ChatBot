import os

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

bot = ChatBot('Bot')
bot.set_trainer(ListTrainer)

for files in os.listdir('C:/Users/Parth - Pc/Desktop/ChatBot/data'):
             data = open('C:/Users/Parth - Pc/Desktop/ChatBot/data/'+ files,'r').readlines()
             bot.train(data)

while True:
        message=input('You:')
		
        if message.strip()!='Bye':
            reply = bot.get_response(message)
            print('Chatbot:',reply)
			
        if message.strip().lower() =='bye':
            print('Chatbot:Bye')
            break
