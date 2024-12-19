from characterai import pycai
import time

class ChatAI:
    def __init__(self, token, char_id):
        self.client = pycai.Client(token)
        self.char_id = char_id
        self.chat = None
        self.new_chat = None
        self.user_token = token

    def start_chat_ai(self):
        """Inicia la sesión del chat con el bot de Character AI."""
        try:
            # Intentamos obtener la información del usuario
            me = self.client.get_me()
            
            # Intentamos establecer la conexión
            self.chat = self.client.connect()
            chat_actual = self.client.get_chat(self.char_id, token=self.user_token)

            if chat_actual:
                self.new_chat = chat_actual
                return "Conversación reanudada..."
            else:
                # Si no existe la conversación, la creamos
                self.new_chat, answer = self.chat.new_chat(self.char_id, me.id)
                return f'{answer.name}: {answer.text}'  # Devuelve la primera respuesta al iniciar el chat.
        except Exception as e:
            return f"Error al iniciar el chat: {e}"

    def chat_with_ai(self, aMessage): 
        """Envía un mensaje al bot y devuelve la respuesta."""
        if self.chat and self.new_chat:
            try:
                # Intentamos enviar el mensaje al bot
                message = self.chat.send_message(self.char_id, self.new_chat.chat_id, aMessage)
                return f'{message.text}'
            except Exception as e:
                # Si hay error al enviar el mensaje, intentamos reconectar
                print("Error al enviar mensaje. Intentando reconectar...")
                error_message = self.reconnect_and_retry(aMessage)
                return error_message
        else:
            raise Exception("El chat no ha sido iniciado. Llama a start_chat_ai primero.")

    def reconnect_and_retry(self, aMessage):
        """Reconecta y vuelve a intentar enviar el mensaje."""
        retries = 3  # Intentamos hasta 3 veces
        for attempt in range(retries):
            print(f"Intento {attempt + 1} de {retries}...")
            time.sleep(2)  # Esperamos un momento antes de intentar de nuevo
            try:
                # Volver a intentar iniciar el chat
                self.start_chat_ai()
                message = self.chat.send_message(self.char_id, self.new_chat.chat_id, aMessage)
                return f'{message.text}'  # Devuelve la respuesta del bot.
            except Exception as e:
                print(f"Error al reconectar: {e}")
                if attempt == retries - 1:
                    return "No se pudo enviar el mensaje después de varios intentos. Intenta más tarde."
        return "Error al intentar enviar el mensaje."

    def close_chat(self):
        """Cierra la conexión del chat."""
        if self.chat:
            try:
                self.chat.__exit__(None, None, None)
                self.chat = None
                print("Chat cerrado correctamente.")
            except Exception as e:
                print(f"Error al cerrar el chat: {e}")

