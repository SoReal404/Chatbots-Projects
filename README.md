# ChatBot ✨

![Demo](https://raw.githubusercontent.com/MarwanRTX/Chatbots-Projects/main/chatbotgif.gif)

## 📂 Projects

| Project | Description |
|---------|-------------|
| **ChatBot Choices based Type** | JSON-driven menu chatbot with neon UI |
| **ChatBot API Based** | AI chatbot powered by Google Gemini |
| **ChatBot Choices based on web file** | Web-scraped data chatbot |

---

## 🤖 ChatBot Choices based Type

A dynamic chatbot interface for modern businesses with a neon cyberpunk UI.

### 🚀 Features
- **Neon Cyberpunk UI** with animated elements
- **JSON-powered menu system** for easy updates
- Real-time conversation interface
- Multi-type response handling (lists, key-value, text)
- Floating chat widget with smooth animations
- Mobile-responsive design
- Easy integration with external APIs

### 📸 Screenshots
| Menu Interface | Response Display |
|----------------|------------------|
| ![Menu](https://raw.githubusercontent.com/MarwanRTX/Chatbots-Projects/main/chat.png) | ![Response](https://raw.githubusercontent.com/MarwanRTX/Chatbots-Projects/main/chat3.png) |

### ⚙️ Installation
```bash
git clone https://github.com/SoReal404/Chatbots-Projects.git
cd "Chatbot Choices based Type"
pip install -r requirements.txt
python app.py
```

### 🔧 Configuration
Edit `app.py` to modify the JSON data source:
```python
url = "https://your-json-data-source.json"
```

### 📋 Usage
- Click the floating neon button 💬
- **Fruits Menu**: Displays available fruits and prices
- **Available Places**: Shows store locations
- **Special Offers**: Lists current promotions
- **Contact Info**: Provides contact details

---

## ⚡ ChatBot API Based

AI chatbot powered by **Google Gemini 2.5 Flash** — AJAX-based, no page reloads.

![Screenshot](https://raw.githubusercontent.com/SoReal404/Chatbots-Projects/main/ChatBot%20API%20Based/Screenshot%202026-06-13%20040832.png)

![Demo](https://raw.githubusercontent.com/SoReal404/Chatbots-Projects/main/ChatBot%20API%20Based/vid.gif)

### 🚀 Features
- Google Gemini AI with markdown responses
- AJAX chat — no page reloads
- Typing indicator while AI responds
- Chat history saved in localStorage
- XSS protection via DOMPurify
- Floating widget with slide-up panel
- Mobile responsive
- Enter to send, Shift+Enter for newline
- Security headers on all responses

### ⚙️ Installation
```bash
cd "ChatBot API Based"
pip install flask python-dotenv google-genai markdown
```

Create `.env` with your API key:
```env
GEMINI_API_KEY=your_key_here
```
Get one at [aistudio.google.com](https://aistudio.google.com/apikey)

```bash
python chatbot.py
```

Open `http://localhost:5000`

### 🔧 Config
| Variable | Description |
|----------|-------------|
| `GEMINI_API_KEY` | Google Gemini API key (required) |
| `FLASK_DEBUG` | Set to `1` for debug mode |

---

## 🤝 Contributing
1. Fork the project
2. Create a feature branch: `git checkout -b feature/AmazingFeature`
3. Commit: `git commit -m 'Add feature'`
4. Push: `git push origin feature/AmazingFeature`
5. Open a Pull Request

## ✉️ Contact
**Marwan Mostafa** — [LinkedIn](https://www.linkedin.com/in/marwan-mostafa-712192212/) — marwan.d.2008@gmail.com

Project Link: [https://github.com/SoReal404/Chatbots-Projects](https://github.com/SoReal404/Chatbots-Projects)
