from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import uvicorn
from mainlib.qabot import return_answer

app = FastAPI()

@app.get("/")
async def root():
    return HTMLResponse("""<h1>Welcome to the Q&A bot!</h1><br> 
    Please use the <code>/question</code> endpoint to randomly pull a question from the White Forum Post.
    <br>Alternatively, you can also ask your own question by using the <code>/question/{your question}</code> 
    endpoint and inputting your question in the <code>your question</code> parameter.""")

@app.get("/add/{num1}/{num2}")
async def add(num1: int, num2: int):
    """Add two numbers together"""

    total = num1 + num2
    return {"total": total}

@app.get("/question") 
async def ask():  
    """Ask a question"""

    question, answer = return_answer() 
    return {"Question": question + "?", "Answer": answer}

@app.get("/question/{question}") 
async def ask_own_question(question: str): 
    """Ask a question"""

    question, answer = return_answer(question)
    return {"Question": question + "?", "Answer": answer}


if __name__ == '__main__':
    uvicorn.run(app, port=8080, host='0.0.0.0')