This is finally the time to upload my 100% local ai discord chatbot.

This is truly a big project for me, maybe not for you, but this whole itself took me 2 years, from 0 in ai and programmation.
---
# Base core

To make this chatbot here's how my script basically works and need:

- ollama installed and running
- a custom model with proper system prompt (for persona)
- And that's mostly all:
Based on the given model, my script will fetch its capabilities:
- If the raw model have vision, all the image will directly be given to its context. If not, they'll be described by another smaller vision model and provide its description.
- If the raw model have tool_calls, it'll be able to do some cool function
- Each file attached to a message or a replied message are 'analysed', allowing the model to read(raw, description or transcript): .pdf .pptx .docx .txt .md .mp3 .ogg .wav (upcoming a day: video and gifs)

Also, the model use a custom made model to judge incomming message and tell if the bot should reply or not (instead of always replying to each message).
Better solution can be found, as its trained locally on small datasets, not really good.
You can downloaded it here: [neoluigi/Importance_Regressor](https://huggingface.co/neoluigi/Importance_Regressor/tree/main)

---
# Tool Calls!

The chatbot can do those:
- Run integrated python script:
 - to do complex maths with accuracy
 - provide graph using matplot
- Browse online:
 - Browse the web
 - Browse Youtube
 - Browse gifs (its discord after all)
- Use RAG:
 - Look for past memory
 - Write memory
---
# Some Experiments!

Probably still not included, but at some point of developpement my model was able of those:
- Generate image
- Reply using tts (gpt-so-vit)

Why it got removed?
- My computer isn't enough powerfull to allow *quick* llm inference while offering tools, and all the current function, if I have one of those.

---
# Setup

Sadly, the project is more of a prototype / proof of concept...

However, if you really want to setup your own one, just dm me on discord `neo_luigi` and I'll give you hint on how to run it yourself!
If you want to see a live version with my own chatbot, hmu on discord too!

---
# Contributor

If you're a great dev and want to help the project, then you can! The project isn't moving as fast as I want (because of studies and personnal life), but like I said, its still 2 years of project ongoing!
(explaining why its *not getting lots of update*, which actually I may forgot to push every modification lol, just ask me on discord and I'll tell you everything ^^)

---
 # My personnal Current Setup

 Wondering if it could work on your personnal computer? Well, for my side, with some optimisation (mostly automated with Ollama already), I can run the bot on my machine:
 - Ryzen 5 6-core
 - RTX 3050 8gb
 - Ram 32gb
(not that crazy but still not thaaaat baaad)

If you have more then this, you can run it without any trouble!
