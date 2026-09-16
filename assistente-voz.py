#!/usr/bin/env python3
"""
Assistente de voz com Claude - Linux
======================================

Fluxo: escuta o microfone -> transcreve fala -> envia para o Claude -> fala a resposta

DEPENDÊNCIAS (instale antes de rodar):
    pip install anthropic SpeechRecognition pyttsx3 pyaudio --break-system-packages

    No Ubuntu/Debian, o pyaudio pode precisar de:
        sudo apt install portaudio19-dev python3-pyaudio espeak

CONFIGURAÇÃO:
    Defina sua chave de API como variável de ambiente antes de rodar:
        export ANTHROPIC_API_KEY="sua-chave-aqui"
"""

import os
import speech_recognition as sr
import pyttsx3
from anthropic import Anthropic

# --- Configuração ---
client = Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))
MODEL = "claude-sonnet-4-6"

recognizer = sr.Recognizer()
mic = sr.Microphone()

engine = pyttsx3.init()
engine.setProperty("rate", 175)  # velocidade da fala
# Para escolher voz em português, veja engine.getProperty("voices")

# Histórico simples de conversa (mantém contexto entre falas)
historico = []


def falar(texto: str):
    print(f"Claude: {texto}")
    engine.say(texto)
    engine.runAndWait()


def ouvir() -> str | None:
    with mic as source:
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        print("\n🎤 Escutando... (fale agora)")
        try:
            audio = recognizer.listen(source, timeout=6, phrase_time_limit=15)
        except sr.WaitTimeoutError:
            return None

    try:
        texto = recognizer.recognize_google(audio, language="pt-BR")
        print(f"Você: {texto}")
        return texto
    except sr.UnknownValueError:
        print("(não entendi o áudio)")
        return None
    except sr.RequestError as e:
        print(f"Erro no serviço de reconhecimento: {e}")
        return None


def perguntar_claude(pergunta: str) -> str:
    historico.append({"role": "user", "content": pergunta})
    resposta = client.messages.create(
        model=MODEL,
        max_tokens=500,
        messages=historico,
    )
    texto_resposta = resposta.content[0].text
    historico.append({"role": "assistant", "content": texto_resposta})
    return texto_resposta


def main():
    falar("Assistente pronto. Pode falar.")
    while True:
        pergunta = ouvir()
        if not pergunta:
            continue
        if pergunta.lower().strip() in ("sair", "parar", "encerrar", "tchau"):
            falar("Até mais!")
            break
        resposta = perguntar_claude(pergunta)
        falar(resposta)


if __name__ == "__main__":
    main()
