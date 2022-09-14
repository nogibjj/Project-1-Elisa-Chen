#!/usr/bin/env python3

# Importing necessary libraries
import click
from mainlib.qabot import return_answer

#build a click group
@click.group()
def cli():
    """A command line interface for the Q&A bot"""
    
#build a click command
@cli.command()
@click.option("--question", default = '' ,prompt="Ask a question. If you input nothing, the bot will randomly select a question asked in White Power Forum... so please do ask a question.", help="The question you want to ask")
def answer(question):
    """Ask a question and receive an answer. By default it will select a random question from the White Power Forum posts."""
    return_answer(question)

#run the command line interface
if __name__ == "__main__":
    cli()