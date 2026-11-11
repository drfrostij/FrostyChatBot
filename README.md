# FrostAI

**FrostAI** is a Python-based AI chatbot designed to provide an interactive AI experience through a custom graphical user interface. The project aims to recreate the core functionality of modern AI chat applications, including conversation management, persistent memory, voice interaction and web searching.

## Features

### User Management
- **Login System** — User authentication using Python and SQLite.
- **User Accounts** — Separate data and conversations for each user.

### Conversation Management
- **Channels** — Create separate conversations for different topics.
- **Create Channels** — Start new AI conversations.
- **Delete Channels** — Remove existing conversations and their stored data.
- **Auto Save** — Automatically save conversations.
- **Channel Storage** — Store each conversation in an individual `.txt` file.

### AI Functionality
- **AI Chatbot** — Communicate with an AI model through an API.
- **Saved Memory** — Persistent AI memory across conversations.
- **Personalised AI** — Customise the AI's behaviour using saved system prompts.
- **Web Searching** — Allow the AI to search the internet for additional information.

### Voice Interaction
- **Quick Speech** — Convert spoken input into text.
- **Speak Responses** — Convert AI-generated responses into speech.

## Technologies

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| CustomTkinter | Graphical user interface |
| SQLite | User accounts and database management |
| Text Files | Conversation storage |
| AI API | AI-generated responses |
| Speech Recognition | Voice input |
| Text-to-Speech | Spoken AI responses |
| Web Search API | Internet searching |

## Project Structure

```text
FrostAI/
│
├── main.py
├── requirements.txt
│
├── interface/
│   ├── login.py
│   ├── mainGUI.py
│   ├── channels.py
│   └── settings.py
│
├── ai/
│   ├── chatbot.py
│   ├── memory.py
│   ├── prompts.py
│   └── websearch.py
│
├── speech/
│   ├── speech_to_text.py
│   └── text_to_speech.py
│
├── database/
│   ├── database.py
│   └── accounts.py
│
└── data/
    ├── users/
    └── channels/
```

## Data Storage

Each user will have their own directory containing their saved memory and individual conversations.

Example:

```text
data/
│
└── users/
    │
    └── frost/
        │
        ├── memory.txt
        │
        └── channels/
            ├── channel_001.txt
            ├── channel_002.txt
            └── channel_003.txt
```

### Example Channel File

Each channel stores its conversation history and its own system prompt.

```text
CHANNEL: Python Development

SYSTEM PROMPT:
You are a Python programming assistant.

USER:
How do I create a function?

AI:
You can create a function using def...

USER:
What about parameters?

AI:
Parameters allow you to pass information...
```

## Development Roadmap

- [ ] Create the main CustomTkinter interface.
- [ ] Implement the login and registration system.
- [ ] Implement channel creation and deletion.
- [ ] Implement individual channel storage.
- [ ] Implement automatic conversation saving.
- [ ] Integrate an AI model API.
- [ ] Implement custom system prompts.
- [ ] Implement persistent AI memory.
- [ ] Implement web searching.
- [ ] Implement speech recognition.
- [ ] Implement text-to-speech.
- [ ] Improve the graphical interface.
- [ ] Prepare the application for future web deployment.

## Future Development

FrostAI will initially be developed as a Python desktop application using CustomTkinter.

The long-term goal is to separate the AI backend from the graphical interface, allowing the same Python AI engine to eventually power a browser-based version using HTML, CSS and JavaScript.

---

**Project:** FrostAI  
**Language:** Python  
**Interface:** CustomTkinter  
**Status:** In Development



<img width="1152" height="648" alt="FrozenSoulAI" src="https://github.com/user-attachments/assets/d01ac5dc-867e-4144-82cc-daee4b18fb43" />




