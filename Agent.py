from mineflayer import Mineflayer
from config.config import Config
from scripts.movement import setup_movement

# Initialize the bot using the configuration
bot = Mineflayer(Config.HOST, Config.PORT, Config.USERNAME)

@bot.event
def on_spawn():
    print("lee-mon has spawned in the game.")
    setup_movement(bot)
#gg good going
@bot.event
def on_chat(username, message):
    if username != Config.USERNAME:
        bot.chat(f"Hello, {username}! You said: {message}")
        if message == ":quit":
            bot.quit()
        elif message == ":join":
            if not bot.is_connected():
                bot.connect()

if __name__ == '__main__':
    bot.run()
