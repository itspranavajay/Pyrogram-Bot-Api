import os
import json

from pyrogram import Client

from fastapi import FastAPI, Request


app = FastAPI()

API_ID = os.environ.get("API_ID", None) 
API_HASH = os.environ.get("API_HASH", None)

async def clientbot(token):
    bot = Client(
        ':memory:',
        api_id=API_ID,
        api_hash=API_HASH,
        bot_token=token
    )
    await bot.start()
    return bot

@app.get('/sendmessage')
async def send_message(token, log, msg):
    bot = await clientbot(token)
    try:
        await bot.send_message(chat_id=int(log), text=f"{msg}")
        return {'message': "Done 👍"}
    except Exception as e:
        return {'error': f"{e}"}
