

import pandas as pd
from pptx import Presentation
from pptx.util import Inches
from collections import defaultdict

from api_settings import safety_settings
from openai import OpenAI
import google.generativeai as genai

from dotenv import load_dotenv
from pathlib import Path
import os

dotenv_path = Path('generative_ai_keys.env')
load_dotenv(dotenv_path=dotenv_path)

from openai import OpenAI
chat_gpt_key = os.getenv('chat_gpt_key')
gemini_key = os.getenv('gemini_key')

client = OpenAI(api_key=chat_gpt_key)
genai.configure(api_key=gemini_key)

topic="Weather Safety"

#Ais can either be chatgpt or gemini
ais=[]
ais.append("chatgpt")
#ais.append("gemini")

questions_to_generate=10

def get_answer_from_chatgpt():
    system_prompt=f"""
    You are a soft skills teaching assistant."""

    user_prompt=f"""Create {questions_to_generate} questions on {topic} that students can write about.
    Questions should be simple and not have multiple parts.
    Put each question on a new line without any numbers."
    """

    completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt}
    ],
    )

    #print(completion.usage,end="\n\n")
    #print(completion.choices[0].message.content)
    response=completion.choices[0].message.content
    return response

def get_answer_from_gemini():
    system_prompt=f"""
    You are a soft skills teaching assistant."""

    user_prompt=f"""Create {questions_to_generate} questions on {topic} that students can write about. 
    Questions should be simple and not have multiple parts.
    Put each question on a new line without any numbers."
    """

    model = genai.GenerativeModel('gemini-1.5-flash',safety_settings=safety_settings)
    chat = model.start_chat(history=[])

    response = chat.send_message(system_prompt,safety_settings=safety_settings)
    
    response = chat.send_message(user_prompt,safety_settings=safety_settings)

    return response.text

def blank():
    return ""

def main():
    for ai in ais:
        print(ai)
        if ai=="chatgpt":
            questions=get_answer_from_chatgpt()
            print(questions)
        else:
            break
            questions=get_answer_from_gemini()
            print(questions)


if __name__=="__main__":
    main()