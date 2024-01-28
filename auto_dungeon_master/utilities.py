#!/usr/bin/env python

from openai import OpenAI


def make_api_request(context: str, prompt: str) -> str:
    """
    Make an api call to the llm with the context and the 
    prompt
    Args:
    """
    client = OpenAI()
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": context},
            {"role": "user", "content": prompt}
        ]
    )

    response_txt = completion.choices[0].message.content

    return response_txt

def prompt_for_player_input(prompt: str) -> str:
    """
    Use python input function to retrieve a response from the indeicated prompt.
    """
    player_input = input(prompt)

    return player_input