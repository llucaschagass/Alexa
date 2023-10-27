import speech_recognition as sr
import os

# Função para ouvir e reconhecer a fala
def ouvir_microfone():
    # Habilita o microfone do usuário
    microfone = sr.Recognizer()
    
    # Usando o microfone
    with sr.Microphone() as source:
        
        # Chama um algoritmo de redução de ruídos no som
        microfone.adjust_for_ambient_noise(source)
        
        ouvindo = False  # Inicialmente não estamos ouvindo

        while True:
            try:
                # Captura a fala contínua
                audio = microfone.listen(source)
                
                # Tenta reconhecer a fala
                frase = microfone.recognize_google(audio, language='pt-BR')

                if "Alexa" in frase:
                    print("Estou ouvindo, pode falar.")

                # Exibe a frase pronunciada
                print("Você disse: " + frase)

            except sr.UnknownValueError:
                pass
            except sr.RequestError:
                print("Ocorreu um erro na solicitação. Verifique sua conexão com a Internet.")

ouvir_microfone()
