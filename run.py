import datetime
import telebot
import os

from modulos.CharacterAIClient import ChatAI
from telebot import types
from datetime import datetime


from dotenv import load_dotenv


# Cargar las variables del archivo .env
load_dotenv()

# Configuración de Tokens
TOKEN_TELEGRAM = os.getenv('TOKEN_TELEGRAM')
bot = telebot.TeleBot(TOKEN_TELEGRAM)
TOKEN = os.getenv('TOKEN_CHARAI')
CHAR_ID = os.getenv('TOKEN_CHAT')
ID_TG_USER = os.getenv('ID_TG_USER')

# Crear una instancias
bot_ai = ChatAI(TOKEN, CHAR_ID)

# Lista de usuarios permitidos por su ID
usuarios_permitidos = [ID_TG_USER]  # IDs de los usuarios permitidos

# Función para manejar el comando /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    user_id = str(message.from_user.id)  # ID del usuario que envió el mensaje
    if user_id in usuarios_permitidos:
        saludo_inicial = bot_ai.start_chat_ai()
        bot.reply_to(message, saludo_inicial)
    else:
        # Responder si el usuario no está autorizado
        bot.reply_to(message, "No estás autorizado para usar este bot.")

# Control de mensajes por orden de relevancia----------------------------------------------
        
# Captura cualquier mensaje del usuario, pero solo si está autorizado
@bot.message_handler(func=lambda message: True)
def responder_mensaje(message):
    user_id = str(message.from_user.id)  # ID del usuario que envió el mensaje
    
    # Verificar si el usuario está autorizado
    if user_id in usuarios_permitidos:
        
        texto_usuario = f"$ {message.text}"
        bot.send_chat_action(message.chat.id, 'typing')
        respuesta = bot_ai.chat_with_ai(texto_usuario)
        bot.reply_to(message, respuesta)
    else:
        # Responder si el usuario no está autorizado
        bot.reply_to(message, "No estás autorizado para usar este bot.")

# Iniciar el bot de Telegram
if __name__ == "__main__":
    bot.polling(none_stop=True)

