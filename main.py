from pyrogram import *
from pyrogram.types import *
import os
from requests import get as Get

def get_url(url):
	result = Get(url).json()
	return result

ph_url = "https://apig.herokuapp.com/get?text={}"

text_url = "https://api.dlyar-dev.tk/open-ai.json?key=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&text={}"

token = os.environ.get("TOKEN")

app = Client("bd",12643300,"73c1a336adc28a59661ff7761ff02672",bot_token=token)

@app.on_message(filters.command("start"))
async def start(c:Client,m:Message):
	
	await m.reply("""**
- Welcom 🔥 .
- A bot that solves software and research issues ، chetGPT .

- مرحبا 🔥 .
- بوت يقوم بحل مسائل البرمجية وعمل البحوث عن طريق chatGPT .
- تحدث مع الذكاء الاصطناعي .
𝙱𝚈 › @Team_Doss .
**""",
reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Dev >_",url="EP_EU.t.me"),InlineKeyboardButton("Channel",url="https://t.me/Team_Doss")]]))
	
@app.on_message(filters.text)
async def bot(c:Client,m:Message):
	
	order = m.text
	
	c = await m.reply("جارى الرد...")
	
	ph = get_url(ph_url.format(order))
	ph3 = ph["data"][0]["url"]
	
	tx = get_url(text_url.format(order))
	tx3 = tx["choices"][0]["text"]
	
	await m.reply_photo(photo=ph3,caption=tx3,reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Dev >_",url="EP_EU.t.me"),InlineKeyboardButton("Channel",url="https://t.me/Team_Doss")]]))
	
	await c.delete()
	
app.run()
