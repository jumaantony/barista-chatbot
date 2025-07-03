from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from agent.agent import chat
from models.models import ChatRequest, ChatResponse

app = FastAPI(
    title="Coffee Bot API",
    description="A simple API for coffee bot functionality with comprehensive documentation",
    version="1.0.0",
    contact={
        "name": "API Support",
        "email": "support@coffeebot.com",
    },
    license_info={
        "name": "MIT",
        "url": "https://opensource.org/licenses/MIT",
    },
)

@app.exception_handler(Exception)
async def global_exception_handler(request, exc):
    """Global exception handler for all unhandled errors"""
    return JSONResponse(
        status_code=500,
        content={"error": "Internal server error", "detail": str(exc)}
    )

@app.post("/chat", tags=["chat"])
def chat_with_bot(request: ChatRequest):
    """Chat with the coffee bot to place orders"""
    try:
        response = chat.send_message(request.message)
        return ChatResponse(response=response.text)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Chat error: {str(e)}")
