from modulos.characterAIClient import ChatAI

# Define tu token y char_id. Asegúrate de tener estos valores antes de probar.
token = '760259b09e5a42f9dd96f55f4b4871a8580a998f'  # Reemplázalo con tu token real
char_id = '9WXvvno9me4K7Xalpe632CwfKbU9Yhu1aO1ZQ2e0aKY'  # Reemplázalo con el ID del personaje

def test_chat_ai():
    try:
        # Inicializa el objeto ChatAI
        chat_ai = ChatAI(token, char_id)

        # Inicia la conversación
        print("Iniciando el chat...")
        start_message = chat_ai.start_chat_ai()
        print(start_message)

        # Enviar un mensaje
        user_message = "Hola, ¿cómo estás?"
        print(f"\nEnviando mensaje: '{user_message}'")
        bot_response = chat_ai.chat_with_ai(user_message)
        print(f"Respuesta del bot: {bot_response}")

        # Cerrar la conversación
        print("\nCerrando el chat...")
        chat_ai.close_chat()

    except Exception as e:
        print(f"Error en el test: {e}")

# Llamamos a la función de test
if __name__ == "__main__":
    test_chat_ai()
