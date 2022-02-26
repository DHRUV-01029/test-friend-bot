from telethon import TelegramClient, events

bot = TelegramClient('bot', 2496118, '8e49bf44e7eeadf25e6f019d244771b5').start(bot_token='5164656985:AAF4cYyQiF-bqmjo11iRgIVheCV2PfO9QJs')
@bot.on(events.NewMessage(pattern='/start'))
async def send_welcome(event):
	await event.reply('Howdy, how are you doing?')


@bot.on(events.NewMessage)
async def echo_all(event):
	print(event.message.message)


bot.run_until_disconnected()