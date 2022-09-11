#!/home/vscode/.venv/bin/python python3

#Importing necessary libraries
import os
import random
import pandas as pd
import openai
import click

#Using dask to load and manipulate the data
from dask import dataframe as dd
from dask.distributed import Client

#Setting up the API key
#openai.api_key = os.environ["OPENAI_API_KEY"] --> ASK HOW SHOULD I SET THIS UP IF SOMEONE WANTS TO CLONE THIS REPO?

#Loading the data
def load_data():
    #Setting up the client
    client = Client()
    pd_df = pd.read_csv("./raw_data/cleanposts.csv", nrows=100000) #REMEMBER TO CHANGE NROWS
    ddf = dd.from_pandas(pd_df, npartitions=10)
    return ddf

#A Function To Find All Messages With Question Marks
def find_question_mark(df):
    df['question_mark'] = df['cleanmessage'].str.contains('\?')
    df = df[df['question_mark'] == True]
    return df

#A Function to extract the question from the message
def extract_question(df):
    df['question'] = df['cleanmessage'].str.extract(r'\b([A-Z][^.!]*[?])')[0]
    return df

#Function to generate the answer to any question using OpenAI GPT-3 API
def ask(question):
  openai.api_key = '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'

  start_sequence = "\nAI:"

  response = openai.Completion.create(
      engine="text-davinci-002",
      prompt=question + start_sequence,
      temperature=0.9,
      max_tokens=150,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0.6,
      stop=["\n", " Human:", " AI:"]
    )
  return response["choices"][0]["text"].strip(" \n")

#Function to randomly pick a question from the dataset and provide a response via OpenAI GPT-3 API
def answer(ddf):
    index = random.randint(1, len(ddf))
    question = ddf['question'].compute().tolist()[index]
    print("Question: " + question)
    print("Answer: " + ask(question))

#Function to run the program
#@click.command()
#@click.argument()
def main():
    """Randomly select a question from the White Power Forum posts and provide an answer using OpenAI GPT-3 API"""
    ddf = load_data()
    ddf = ddf.map_partitions(find_question_mark)
    ddf = ddf.map_partitions(extract_question)
    ddf = ddf.dropna(subset=['question'])  
    answer(ddf)

if __name__ == "__main__":
    # pylint: disable=no-value-for-parameter
    main()