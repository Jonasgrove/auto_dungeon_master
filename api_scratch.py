#!/usr/bin/env python

from openai import OpenAI


client = OpenAI()

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a Dungeons and Dragnons Dungeon Master."},
    {"role": "user", "content": "Please tell me the base weapons and dammage scores of an orc of level 2 attacking you."}
  ]
)




print(completion.choices[0].message.content)

