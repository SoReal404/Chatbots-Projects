# ChatBot :sparkles:

![Demo](https://raw.githubusercontent.com/SoReal404/Chatbots-Projects/main/ChatBot%20API%20Based/Screenshot%202026-06-13%20040832.png)
*Gemini-powered AI chatbot with a neon cyberpunk UI*

## 📂 Projects

| Project | Description |
|---------|-------------|
| **ChatBot API Based** | AI chatbot powered by Google Gemini API (this project) |
| ChatBot Choices based Type | JSON-driven menu chatbot |
| ChatBot Choices based on web file | Web-scraped data chatbot |

---

## 🤖 ChatBot API Based

An AI chatbot with a floating neon widget, AJAX-based messaging, and Google Gemini integration.

### 🚀 Features
- **Google Gemini 2.5 Flash** — intelligent, context-aware responses
- **AJAX chat** — no page reloads, instant messaging
- **Typing indicator** — animated dots while AI responds
- **Chat history** — persisted in localStorage across sessions
- **Markdown rendering** — code blocks, lists, links, and formatting
- **XSS protection** — DOMPurify sanitization on all bot output
- **Floating widget** — toggle button with slide-up panel
- **Mobile responsive** — full-screen on small devices
- **Keyboard shortcuts** — Enter to send, Shift+Enter for newline
- **Security headers** — X-Content-Type-Options, X-Frame-Options, X-XSS-Protection
- **Production-ready** — config via environment variables

### 📸 Screenshots & Demo

| Chat Widget Open | Mobile View |
|------------------|-------------|
| ![Screenshot](https://raw.githubusercontent.com/SoReal404/Chatbots-Projects/main/ChatBot%20API%20Based/Screenshot%202026-06-13%20040832.png) | *Responsive design adapts to any screen* |

▶️ [Watch demo recording](https://raw.githubusercontent.com/SoReal404/Chatbots-Projects/main/ChatBot%20API%20Based/Recording%202026-06-13%20041124.mp4)

### ⚙️ Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/SoReal404/Chatbots-Projects.git
   cd "Chatbots-Projects/ChatBot API Based"
   ```

2. **Install dependencies:**
   ```bash
   pip install flask python-dotenv google-genai markdown
   ```

3. **Set up your API key:**
   Create a `.env` file (or edit the existing one):
   ```env
   GEMINI_API_KEY=your_google_gemini_api_key_here
   ```
   Get a free key at [aistudio.google.com](https://aistudio.google.com/apikey)

4. **Run the application:**
   ```bash
   python chatbot.py
   ```

5. **Open in browser:**
   ```
   http://localhost:5000
   ```

### 🔧 Configuration

All config is done via environment variables in `.env`:

| Variable | Default | Description |
|----------|---------|-------------|
| `GEMINI_API_KEY` | — | Google Gemini API key (required) |
| `FLASK_DEBUG` | `0` | Set to `1` for debug mode |
| `SECRET_KEY` | Auto-generated | Flask session secret |

### 🎨 Customize UI

Edit `templates/index.html` CSS variables:

```css
:root {
    --primary: #00f3ff;     /* Neon blue accent */
    --accent: #bc13fe;      /* Neon purple accent */
    --bg: #0a0e17;          /* Dark background */
}
```

### 📚 Project Structure

```
ChatBot API Based/
├── chatbot.py              # Flask app + Gemini API integration
├── .env                    # Environment variables (API key)
├── templates/
│   └── index.html          # Chat UI (AJAX, animations, responsive)
├── Screenshot*.png         # Preview images
└── Recording*.mp4          # Demo video
```

### 🛡️ Security

- API key stored in `.env`, never hardcoded
- Bot output sanitized with DOMPurify (XSS prevention)
- Security headers set on all responses
- Input validated and length-limited on server
- Chat history stored locally (never sent to server)

---

## 🤝 Contributing

1. Fork the project
2. Create your feature branch:
   ```bash
   git checkout -b feature/AmazingFeature
   ```
3. Commit your changes:
   ```bash
   git commit -m 'Add some AmazingFeature'
   ```
4. Push to the branch:
   ```bash
   git push origin feature/AmazingFeature
   ```
5. Open a Pull Request

## ✉️ Contact

**Marwan Mostafa**  
[LinkedIn](https://www.linkedin.com/in/marwan-mostafa-712192212/)  
marwan.d.2008@gmail.com

Project Link: [https://github.com/SoReal404/Chatbots-Projects](https://github.com/SoReal404/Chatbots-Projects)
