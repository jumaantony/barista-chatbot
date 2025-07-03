# ☕ Coffee Chatbot

A conversational AI-powered coffee ordering system built with FastAPI, Google Gemini AI, and Streamlit. This chatbot helps customers place coffee orders by understanding natural language requests and managing the ordering process through an intuitive chat interface.

## 🚀 Features

- **Natural Language Processing**: Uses Google Gemini AI to understand customer orders in natural language
- **Menu Management**: Comprehensive coffee and tea menu with customizable modifiers
- **Order Management**: Add, remove, and modify items in real-time
- **Order Confirmation**: Built-in confirmation flow before placing orders
- **Web Interface**: Beautiful Streamlit UI for seamless user experience
- **RESTful API**: FastAPI backend for easy integration and scalability

## 🛠️ Tech Stack

- **Backend**: FastAPI (Python)
- **AI/LLM**: Google Gemini 2.5 Flash
- **Frontend**: Streamlit
- **Language**: Python 3.8+
- **Dependencies**: Poetry for package management

## 📋 Prerequisites

- Python 3.8 or higher
- Google AI API key
- Poetry (recommended) or pip

## 🚀 Quick Start

### 1. Clone the Repository
```bash
git clone <repository-url>
cd chatbot
```

### 2. Install Dependencies
```bash
# Using Poetry (recommended)
poetry install

# Or using pip
pip install -r requirements.txt
```

### 3. Environment Setup
Create a `.env` file in the root directory:
```env
GOOGLE_API_KEY=your_google_ai_api_key_here
API_URL=http://localhost:8000/chat
```

### 4. Start the Backend
```bash
fastapi dev main.py
```
The API will be available at `http://localhost:8000`

### 5. Start the Frontend
```bash
streamlit run app.py
```
The UI will be available at `http://localhost:8501`

## 📖 Usage

### Web Interface
1. Open your browser and navigate to `http://localhost:8501`
2. Start chatting with the bot using natural language
3. Example interactions:
   - "I'd like a latte with oat milk"
   - "Can I get an americano with extra hot?"
   - "What's on your menu?"

### API Endpoints

#### POST `/chat`
Send a message to the chatbot.

**Request:**
```json
{
  "message": "I'd like a latte"
}
```

**Response:**
```json
{
  "response": "Got it! One latte. Is there anything else?",
  "order": []
}
```

## 🗂️ Project Structure

```
chatbot/
├── main.py                 # FastAPI backend server
├── app.py                  # Streamlit frontend
├── agent/
│   ├── agent.py           # Google Gemini AI agent setup
│   └── prompt.txt         # System prompt for the chatbot
├── service/
│   └── barista.py         # Order management service
├── models/
│   └── models.py          # Pydantic models for API
├── tests/                 # Test files
├── README.md              # This file
├── pyproject.toml         # Poetry configuration
└── .env                   # Environment variables
```

## 🧠 AI Agent Features

The chatbot uses Google Gemini AI with the following capabilities:

- **Menu Understanding**: Recognizes all drinks and modifiers from the menu
- **Order Management**: Can add, remove, and modify items
- **Confirmation Flow**: Ensures orders are confirmed before placement
- **Natural Language**: Understands various ways customers might phrase requests

### Available Tools
- `add_to_order`: Add drinks with modifiers
- `get_order`: View current order
- `remove_item`: Remove specific items
- `clear_order`: Reset the entire order
- `confirm_order`: Get order summary for confirmation
- `place_order`: Submit order to kitchen

## 🍽️ Menu

### Coffee Drinks
- Espresso, Americano, Cold Brew

### Coffee Drinks with Milk
- Latte, Cappuccino, Cortado, Macchiato, Mocha, Flat White

### Tea Drinks
- English Breakfast Tea, Green Tea, Earl Grey

### Tea Drinks with Milk
- Chai Latte, Matcha Latte, London Fog

### Other Drinks
- Steamer, Hot Chocolate

### Modifiers
- **Milk**: Whole, 2%, Oat, Almond, 2% Lactose Free
- **Espresso Shots**: Single, Double, Triple, Quadruple
- **Caffeine**: Decaf, Regular
- **Temperature**: Hot, Iced
- **Sweeteners**: Vanilla, Hazelnut, Caramel, Chocolate, Sugar-free Vanilla
- **Special Requests**: Extra hot, one pump, half caff, extra foam, etc.

## 🔧 Configuration

### Environment Variables
- `GOOGLE_API_KEY`: Your Google AI API key
- `API_URL`: Backend API URL (default: http://localhost:8000/chat)

### Customization
- Modify `agent/prompt.txt` to change the bot's behavior
- Update the menu in the prompt file
- Customize the UI styling in `app.py`

## 🧪 Testing

Run tests using:
```bash
pytest tests/
```

## 📝 API Documentation

Once the backend is running, visit:
- **Swagger UI**: `http://localhost:8000/docs`
- **ReDoc**: `http://localhost:8000/redoc`

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🆘 Support

If you encounter any issues:
1. Check that all dependencies are installed
2. Verify your Google AI API key is valid
3. Ensure both backend and frontend are running
4. Check the console for error messages

## 🔮 Future Enhancements

- [ ] Payment integration
- [ ] Order history
- [ ] User accounts
- [ ] Mobile app
- [ ] Voice interface
- [ ] Multi-language support
