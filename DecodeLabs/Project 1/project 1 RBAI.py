
from datetime import datetime
import re

bot="RBAI"
def sanitize(text):
  text=re.sub(r"[^\w\s]","",text.lower())
  return " ".join(text.split())


def hello():
  print(f"{bot}: Hi!!.How can i help you today..")
def bye():
  print(f"{bot}: Bye..!")
def unknown():
  print(f"{bot}: I can't understand your message!!")
def how_are_you():
  print(f"{bot}: i'm doing great!!What about you?")
def name():
    print(f"{bot}: My name is AK.I'm your AI Assistant")
def capability():
  print(f"{bot}: I can greet you,answer simple questions, and help you with basic information.")
def show_help():
  print(f"{bot}: You can ask me following questions")
  print("--> Hello")
  print("--> How are you")
  print("--> What is your name")
  print("--> What can you do")
  print("--> Bye")
def thanks():
  print(f"{bot}: You're welcome!!")
def curr_time():
  current_time=datetime.now().strftime("%I:%M %p")
  print(f"{bot}: The current time is {current_time}")
def curr_date():
  current_date=datetime.now().strftime("%d-%m-%Y")
  print(f"{bot}: The current date is {current_date}")
def joke():
  print(f"{bot}: Why don't scientists trust atoms?")
  print(f"{bot}: Because they make up everything!")


intents={
hello:["hi","hello","hey"],
bye:["exit","bye","quit"],
how_are_you:["how are you","how is it going","how are you doing"],
name:["what is your name","who are you","whats your name","your name","name of yours"],
capability:["what can you do","what are your capabilities","what can you help me with","how can you help me"],
show_help:["show commands","help","what can i ask you","what are the things i can ask you"],
thanks:["thanks","thank you","thank you very much","thank you so much"],
curr_time:["whats the time now","current time","tell me current time","tell me the time now"],
curr_date:["whats todays date","tell me today date","what is the date today"],
joke:["tell me a joke","tell me a funny joke","joke","make me laugh"],
}


response={phrase:handler for handler, phrases in intents.items() for phrase in phrases}
exit_phrase=set(intents[bye])

fallback="I can't understand your message!!Type 'help' to see the list of commands you can ask me."

def main():
  print("-----------RBAI BOT-----------")
  while True:
    try:
      inp=sanitize(input("You: "))
    except (KeyboardInterrupt, EOFError):
      print()
      bye()
      break

    handler=response.get(inp)
    if handler:
      handler()
    else:
      print(f"{bot}: {fallback}")

    if inp in exit_phrase:
      break


if __name__=="__main__":
  main()    