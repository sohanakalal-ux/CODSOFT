
# chatbot project

from datetime import datetime

print("Hi! I am a simple chatbot - my_chatbot.py:6")
print("you can talk to me :) - my_chatbot.py:7")
print("type help to see what i can do - my_chatbot.py:8")
print("type bye to exit - my_chatbot.py:9")
print("")

while True:

    msg = input("You: ")
    msg = msg.lower()

    # say hello
    if msg == "hi" or msg == "hello":
        print("SohanaBot: hey! how are you doing? - my_chatbot.py:19")

    # say bye and stop
    elif msg == "bye":
        print("SohanaBot: bye bye! have a great day :) - my_chatbot.py:23")
        break

    # tell the date
    elif msg == "date":
        today = datetime.now()
        print("SohanaBot: todays date is - my_chatbot.py:29" + today.strftime("%d %B %Y"))

    # tell the time
    elif msg == "time":
        now = datetime.now()
        print("SohanaBot: the time right now is - my_chatbot.py:34" + now.strftime("%I:%M %p"))

    # what is python
    elif msg == "what is python":
        print("SohanaBot: python is a popular programming language its easy to learn and good for beginners - my_chatbot.py:38")

    # what is ai
    elif msg == "what is ai":
        print("SohanaBot: ai means artificial intelligence it is when computers do smart things like humans - my_chatbot.py:42")

    # what is a chatbot
    elif msg == "what is a chatbot":
        print("SohanaBot: a chatbot is a program that talks to you like i am doing right now lol - my_chatbot.py:46")

    # what is nlp
    elif msg == "what is nlp":
        print("SohanaBot: nlp stands for natural language processing it helps computers understand human language - my_chatbot.py:50")

    # who created python
    elif msg == "who created python":
        print("SohanaBot: python was created by guido van rossum and first released in 1991 - my_chatbot.py:54")

    # how are you
    elif msg == "how are you":
        print("SohanaBot: i am doing great thanks for asking :) - my_chatbot.py:58")

    # help command
    elif msg == "help":
        print("SohanaBot: here is what you can type: - my_chatbot.py:62")
        print("hi or hello - my_chatbot.py:63")
        print("bye - my_chatbot.py:64")
        print("date - my_chatbot.py:65")
        print("time - my_chatbot.py:66")
        print("what is python - my_chatbot.py:67")
        print("what is ai - my_chatbot.py:68")
        print("what is a chatbot - my_chatbot.py:69")
        print("what is nlp - my_chatbot.py:70")
        print("who created python - my_chatbot.py:71")
        print("how are you - my_chatbot.py:72")

    # if i dont understand
    else:
        print("SohanaBot: hmm i dont know that yet sorry - my_chatbot.py:76")
        print("SohanaBot: try typing help to see what i can do - my_chatbot.py:77")

