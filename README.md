[voice-assistant-claude.md](https://github.com/user-attachments/files/32288861/voice-assistant-claude.md)
# voice-assistant-claude
Voice assistant claude on linux

<p align="right">
  <a href="#english">🇬🇧 English</a> | <a href="#português">🇧🇷 Português</a>
</p>

<a name="english"></a>
# Voice Assistant with Claude (Linux)

A terminal-based voice assistant for Linux that listens to the microphone, transcribes speech, sends it to the Claude API, and speaks the response back — with conversation history kept in memory for context across turns.

## 📋 Overview

- **Language:** Python 3
- **Interface:** Terminal (command-line)
- **Model:** Claude (Anthropic API)
- **Platform:** Linux

## ✨ Features

- Continuous voice listening with ambient noise adjustment
- Speech-to-text in Portuguese (pt-BR)
- Text-to-speech responses via a local speech engine
- Conversation history maintained across turns, so the assistant keeps context
- Voice commands to exit ("sair", "parar", "encerrar", "tchau")

## 🛠️ Tech stack

| Library | Purpose |
|---|---|
| [`anthropic`](https://pypi.org/project/anthropic/) | Claude API client |
| [`SpeechRecognition`](https://pypi.org/project/SpeechRecognition/) | Microphone capture and speech-to-text (via Google's recognizer) |
| [`pyttsx3`](https://pypi.org/project/pyttsx3/) | Offline text-to-speech engine |
| [`PyAudio`](https://pypi.org/project/PyAudio/) | Microphone audio stream backend |

## 📦 Installation

```bash
pip install anthropic SpeechRecognition pyttsx3 pyaudio --break-system-packages
```

On Ubuntu/Debian, PyAudio may also require system packages:

```bash
sudo apt install portaudio19-dev python3-pyaudio espeak
```

Set your Anthropic API key as an environment variable before running:

```bash
export ANTHROPIC_API_KEY="your-key-here"
```

## ▶️ Usage

```bash
python3 assistente_voz.py
```

The assistant announces it's ready, then continuously listens for speech. Speak your question, wait for the spoken response, and repeat. Say "sair", "parar", "encerrar" or "tchau" to end the session.

## 🔄 How it works

1. **Listen** — captures audio from the microphone, adjusting for ambient noise before each listen
2. **Transcribe** — sends the audio to a speech recognition service, returning Portuguese (pt-BR) text
3. **Ask Claude** — appends the transcribed text to the conversation history and sends it to the Claude API
4. **Speak** — converts Claude's text response to speech and plays it back
5. Loop back to step 1, keeping full conversation history for context

## ⚠️ Known limitations

- Continuous/automated use was paused after initial testing, pending a better understanding of the API's usage costs
- Speech recognition depends on an external service (Google's recognizer via `SpeechRecognition`), so it requires an internet connection
- Currently a single-script, terminal-only tool — no wake word, GUI, or background service mode

## 🙏 Credits

This project was built with significant guidance from **Claude** (Anthropic) throughout development — including architecture decisions, dependency choices, and troubleshooting. The resulting script was tested and run successfully via terminal on Linux.

---

<a name="português"></a>
# Assistente de Voz com Claude (Linux)

Um assistente de voz via terminal para Linux que escuta o microfone, transcreve a fala, envia o texto para a API do Claude e fala a resposta de volta — mantendo o histórico da conversa em memória para dar contexto entre as falas.

## 📋 Visão geral

- **Linguagem:** Python 3
- **Interface:** Terminal (linha de comando)
- **Modelo:** Claude (API da Anthropic)
- **Plataforma:** Linux

## ✨ Funcionalidades

- Escuta contínua por voz com ajuste automático de ruído ambiente
- Reconhecimento de fala em português (pt-BR)
- Respostas faladas via motor de síntese de voz local
- Histórico de conversa mantido entre falas, dando contexto ao assistente
- Comandos de voz para encerrar ("sair", "parar", "encerrar", "tchau")

## 🛠️ Tecnologias utilizadas

| Biblioteca | Função |
|---|---|
| [`anthropic`](https://pypi.org/project/anthropic/) | Cliente da API do Claude |
| [`SpeechRecognition`](https://pypi.org/project/SpeechRecognition/) | Captura de microfone e reconhecimento de fala (via serviço do Google) |
| [`pyttsx3`](https://pypi.org/project/pyttsx3/) | Motor de texto-para-fala offline |
| [`PyAudio`](https://pypi.org/project/PyAudio/) | Backend de stream de áudio do microfone |

## 📦 Instalação

```bash
pip install anthropic SpeechRecognition pyttsx3 pyaudio --break-system-packages
```

No Ubuntu/Debian, o PyAudio também pode exigir pacotes do sistema:

```bash
sudo apt install portaudio19-dev python3-pyaudio espeak
```

Defina sua chave de API da Anthropic como variável de ambiente antes de rodar:

```bash
export ANTHROPIC_API_KEY="sua-chave-aqui"
```

## ▶️ Uso

```bash
python3 assistente_voz.py
```

O assistente avisa que está pronto e passa a escutar continuamente. Fale sua pergunta, espere a resposta falada, e repita. Diga "sair", "parar", "encerrar" ou "tchau" para encerrar a sessão.

## 🔄 Como funciona

1. **Escutar** — captura o áudio do microfone, ajustando o ruído ambiente antes de cada escuta
2. **Transcrever** — envia o áudio para um serviço de reconhecimento de fala, retornando o texto em português (pt-BR)
3. **Perguntar ao Claude** — adiciona o texto transcrito ao histórico da conversa e envia para a API do Claude
4. **Falar** — converte a resposta em texto do Claude em fala e reproduz o áudio
5. Volta ao passo 1, mantendo o histórico completo da conversa para dar contexto

## ⚠️ Limitações conhecidas

- O uso contínuo/automatizado foi pausado após os testes iniciais, até um melhor entendimento dos custos de uso da API
- O reconhecimento de fala depende de um serviço externo (reconhecedor do Google via `SpeechRecognition`), exigindo conexão com a internet
- Atualmente é um script único, apenas via terminal — sem wake word, interface gráfica ou modo de serviço em segundo plano

## 🙏 Créditos

Este projeto foi desenvolvido com assistência significativa do **Claude** (Anthropic) ao longo do processo — incluindo decisões de arquitetura, escolha de dependências e troubleshooting. O script resultante foi testado e executado com sucesso via terminal no Linux.
