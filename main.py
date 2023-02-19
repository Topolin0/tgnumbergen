import random
import string
import pyrogram
import tgcrypto

from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram import enums

api_id = <id> # u can find it on https://my.telegram.org/ (remove the <id>, just put the id)
api_hash = "" # u can find it on https://my.telegram.org/
bot_token = "" # obv ur bot token

app = Client(
    "my_bot",
    api_id=api_id, api_hash=api_hash,
    bot_token=bot_token
)


@app.on_message(filters.command("start"))
async def start(_, message: Message):
    await message.reply_text("**Hi** " + message.from_user.mention + " 👋" + "\n**I can generate a random number in a range you choose, you just need to write /random min_value max_value. Example: /random 1 10**" + "\n<i>You can find my source code on https://github.com/Topolin0</i>")

@app.on_message(filters.command(["random"]))
def random_number(client, message):
    try:
        min_value, max_value = map(int, message.text.split()[1:3])
        random_num = random.randint(min_value, max_value)
        message.reply_text(f"Your random number is {random_num}")
    except:
        message.reply_text("Invalid input. Please use: /random min max")

app.run()