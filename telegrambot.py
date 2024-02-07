from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Define a function to handle the /start command
def start(update, context):
    update.message.reply_text('Hello! I am your Telegram bot.')

# Define a function to handle the /echo command
def echo(update, context):
    update.message.reply_text(update.message.text)

# Define a function to handle regular messages
def reply(update, context):
    update.message.reply_text('I can only echo your messages. Send /start to begin.')

def main():
    # Initialize the updater with your bot's token
    updater = Updater("YOUR_BOT_TOKEN_HERE", use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # Register command handlers
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", start))  # Redirect /help to /start
    dp.add_handler(CommandHandler("echo", echo))

    # Register a message handler for all other messages
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, reply))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C
    updater.idle()

if __name__ == '__main__':
    main()
