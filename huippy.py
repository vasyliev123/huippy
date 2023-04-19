import requests
from bs4 import BeautifulSoup
from telegram.ext import CommandHandler, MessageHandler, filters, ApplicationBuilder
import random 

TOKEN = ""
class huippy():
    
    def __init__(self) -> None:
        self.app = ApplicationBuilder().token(TOKEN).build()
        self.app.add_handler(MessageHandler(filters.TEXT, self.get_huippy))
        
    async def get_huippy(self, update, context):
        print(update.message.text)
        probability = random.randint(0, 100)
        
        if probability < 100:
            text = update.message.text
            text = text.split(" ")
            word = random.choice(text)
            definition = self.get_definition(word)
            if definition == "No definition found":
                return
            await update.message.reply_text(f"📎 It looks like you're trying to talk about \"{word}\". Urban Dictionary defines it as \"{definition}\""+"\n\n🤖 Huippy Bot by @vasyliev123")
            return
        else:
            return
    def get_definition(self, word):
        url = f"https://www.urbandictionary.com/define.php?term={self.clean_word(word)}"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        definition = soup.find("div", {"class": "meaning"})
        if definition == None:
            return "No definition found"
        definition = definition.text
        if len(definition) > 200:
            definition = definition[:200] + "..."   
        return definition
    def clean_word(self, word):
        return word.replace(" ", "-").replace("?", "").replace("!", "").replace(".", "").replace(",", "").replace(":", "").replace(";", "").replace("(", "").replace(")", "").replace("[", "").replace("]", "").replace("{", "").replace("}", "").replace("'", "").replace('"', "").replace("/", "").replace("\\", "").replace("_", "").replace("-", "").replace("=", "").replace("+", "").replace("*", "").replace("&", "").replace("^", "").replace("%", "").replace("$", "").replace("#", "").replace("@", "").replace("!", "").replace("`", "").replace("~", "").replace("<", "").replace(">", "").replace("?", "").replace("1", "").replace("2", "").replace("3", "").replace("4", "").replace("5", "").replace("6", "").replace("7", "").replace("8", "").replace("9", "").replace("0", "").lower()
    def run(self):
        
        self.app.run_polling()

if __name__ == "__main__":
    bot = huippy()
    bot.run()