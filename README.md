[![Python application test with Github Actions using devcontainers](https://github.com/nogibjj/Project-1-Elisa-Chen/actions/workflows/main.yml/badge.svg)](https://github.com/nogibjj/Project-1-Elisa-Chen/actions/workflows/main.yml)

# Project-1: Answering Burning Questions From The White Power Forum Posts (2001 - 2020) Using a Chat Bot
This repository contains the source code, config files and a short video walkthrough of my project. Please see below for more details.

![Project 1 - Flowchart - Page 1](https://user-images.githubusercontent.com/25168588/190188245-e4652052-7c01-4271-9af5-046cc9a83aed.png)

## Key Objectives & Project Description
The goal of my project is to answer questions from the White Power Forum <<<LINK>>>> website using a Chat Bot. The data for all posts shared on White Power Forum between 2001 - 2020 can be found here <<<LINK>>>. The bot was built using OpenAI's "chat" API <<<LINK>>>. By default, the program will randomly select a question asked in the White Power Forum and generate an answer using the chat bot. Alternatively, the user can also input their own custom question to be answered by the bot. The questions and answers will be displayed on a web app, after the user runs the command `python qabot-app.py`. Most questions are still quite foreign / unseen by the bot, so don't be surprised if the bot doesn't have an answer to the question.

## Demo Video
Link or Embed a demo video

## Methodology
1. The data was downloaded to my GitHub codespaces using the Kaggle API. 
2. The data was then ingested, cleaned and pre-processed using Dask <<<LINK>>>:
    - Posts without questions were filtered out
    - Only the portions containing questions were used as inputs for the bot. (As an example, for a post like "I'm really hungry. Are you hungry?" only "Are you hungry?" would be extracted and used.)
3. The bot was created using OpenAI's Chat API <<<LINK>>>
4. The Web App was created using FastAPI and uvicorn

## Relevant Files & User Instructions
### Data Files
Data Files are located in the `raw_data` directory. <<<SEE IF YOU WANT TO EXPAND. EXPAND IF YOU CAN UPLOAD THE DATA>>>

### Helper Functions
All the functions needed to preprocess and run the program are in the `mainlib/qabot.py` file. 

### CLI
Code needed to run the CLI are in the `main.py` file. NOTE: CLI not shown in the diagram above. 
To run the CLI, type in `./main.py answer` in the terminal, and a prompt should pop up. Afterwards, either
1. Do nothing and press enter again to randomly select a question from the White Power Forum and generate a response with the bot
2. Type in your own question in the prompt and press enter to generate a response to your own question with the bot

### Web-App
Code needed to run the web app using FastAPI are in `qabot-app.py` file. 
To run the web app, type in `python qabot-app.py` in your terminal and open up the web app on a new tab on your browser. This should bring you to the home page that says "Welcome to the Q&A bot!". After that you can either
1.  type in `/question` to the end of the URL to randomly pull a question from the White Forum Post and have it answered by the bot OR
2.  use the `/question/{your question}` endpoint to have the bot answer your own question (to clarify, you should be replacing the parameter `{your question}` with your own question).

### Other
This directory also contains `.devcontainer`, `requirements.txt`, `Makefile`, `.yml` files for configuration and setup / testing purposes. 
