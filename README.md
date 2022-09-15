[![Python application test with Github Actions using devcontainers](https://github.com/nogibjj/Project-1-Elisa-Chen/actions/workflows/main.yml/badge.svg)](https://github.com/nogibjj/Project-1-Elisa-Chen/actions/workflows/main.yml)

# Project-1: Answering Burning Questions From AskReddit Thread Posts on Reddit (2011 - 2020) Using a Chat Bot
This repository contains the source code, config files and a short video walkthrough of my project. Please see below for more details.

![Project 1 - Flowchart - Page 1](https://user-images.githubusercontent.com/25168588/190188245-e4652052-7c01-4271-9af5-046cc9a83aed.png)

## Key Objectives & Project Description
The goal of my project is to answer questions from AskReddit Forum website using a Chat Bot. The data for all posts shared on AskReddit Forum can be found [here](https://www.kaggle.com/datasets/rodmcn/askreddit-questions-and-answers?select=reddit_questions.csv). The bot was built using OpenAI's "chat" [API](https://beta.openai.com/examples/default-chat). By default, the program will randomly select a question asked in AskReddit Forum and generate an answer using the chat bot. Alternatively, the user can also input their own custom question to be answered by the bot. The questions and answers will be displayed on a web app, after the user runs the command `python qabot-app.py`. Most questions are still quite foreign / unseen by the bot, so don't be surprised if the bot doesn't have an answer to the question.

## Demo Video
<a href="https://www.loom.com/share/0c2ef6edf2e64009a15410e36fab8622">
    <p>Project 1 - Elisa Chen - AskReddit Chat Bot - Watch Video</p>
    <img style="max-width:300px;" src="https://cdn.loom.com/sessions/thumbnails/0c2ef6edf2e64009a15410e36fab8622-with-play.gif">
  </a>

## Methodology
1. The data was downloaded to my GitHub codespaces using the Kaggle API. 
2. The data was then ingested, cleaned and pre-processed using Dask:
    - Posts without questions were filtered out
    - Only the portions containing questions were used as inputs for the bot. (As an example, for a post like "I'm really hungry. Are you hungry?" only "Are you hungry?" would be extracted and used.)
3. The bot was created using OpenAI's Chat API
4. The Web App was created using FastAPI and uvicorn

## Relevant Files & User Instructions
### Data Files
Data Files are located in the `raw_data` directory. Below is a preview of the data content:

ID | text | votes | timestamp | datetime 
--- | --- | --- | --- |--- 
izdtr | What's the purpose of life? | 28 | 1601075611.0 | Fri Sep 25 23:13:31 2020 UTC

`ID` is the unique id identifying the question. We primarily use `text` field to extract the questions from. `Votes` is the number of upvotes received by the post. `timestamp` is the unix timestamp at time of posting. `datetime` is the human readable timestamp.


### Helper Functions
All the functions needed to preprocess and run the program are in the `mainlib/qabot.py` file. 

### CLI
Code needed to run the CLI are in the `main.py` file. NOTE: CLI not shown in the diagram above. 
To run the CLI, type in `./main.py answer` in the terminal, and a prompt should pop up. Afterwards, either
1. Do nothing and press enter again to randomly select a question from AskReddit Forum and generate a response with the bot
2. Type in your own question in the prompt and press enter to generate a response to your own question with the bot

### Web-App
Code needed to run the web app using FastAPI are in `qabot-app.py` file. 
To run the web app, type in `python qabot-app.py` in your terminal and open up the web app on a new tab on your browser. This should bring you to the home page that says "Welcome to the Q&A bot!". After that you can either
1.  type in `/question` to the end of the URL to randomly pull a question from the AskReddit Forum Post and have it answered by the bot OR
2.  use the `/question/{your question}` endpoint to have the bot answer your own question (to clarify, you should be replacing the parameter `{your question}` with your own question).

### Other
This directory also contains `.devcontainer`, `requirements.txt`, `Makefile`, `.yml` files for configuration and setup / testing purposes. 
