from fastapi import FastAPI, WebSocket, Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
import ollama
from typing import Annotated
import asyncio

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# response = ollama.chat(
#     "llama3",
#     messages=[
#         {"role": "user", "content": "why is the sky blue?"},
#         {
#             "role": "user",
#             "content": "how to implement a component in Vue.js composition API",
#         },
#     ],
#     stream=True,
# )

# response = ollama.generate(
#     model="llama3",
#     prompt="how to implement a component in Vue.js composition API",
#     stream=True,
# )

# print(response["message"]["content"])
# for chunk in response:
#     print(chunk["response"], end="", flush=True)


@app.get("/ws")
async def connect():
    return {"message": "ok"}


@app.websocket("/ws")
async def chat(
    websocket: WebSocket,
):
    await websocket.accept()

    while True:
        # Receive prompt
        data = await websocket.receive_text()
        print("received prompt", data)

        # Send your own message into client
        # await websocket.send_text(f"You: {data}")

        # Send all chunks of stream from model response
        stream = ollama.generate(model="llama3", prompt=data, stream=True)
        for chunk in stream:
            # print("Sending chunk: ", chunk["response"], flush=True)
            await websocket.send_text(chunk["response"])
            # print("Chunk was sent")
            await asyncio.sleep(0.001)


@app.websocket("/wscounter")
async def counter(
    websocket: WebSocket,
):
    await websocket.accept()

    # Send all chunks of stream from model response
    for i in range(50):
        await websocket.send_text(str(i))
        await asyncio.sleep(0.5)

    await websocket.close()
