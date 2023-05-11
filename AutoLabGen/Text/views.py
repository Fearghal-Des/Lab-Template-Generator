from django.shortcuts import render
from django.http import JsonResponse
import os
import openai
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv('OPENAI_API_KEY', None)

def chat_bot(request):
    chat_bot_response = None
    if api_key is not None and request.method == 'POST':
        openai.api_key = api_key
        user_input = request.POST.get('user_input')
        if user_input == '':
            return render(request, 'index.html', {})
        prompt = f'Provide a template for an experiment with the following title: {user_input}. I do not want you to fill in information under the various headings. Only add useful comments for the discussion. Include a line break between each different section. Include the following sections: Introduction, Diagram, Table of Results, Results, Precautions, Discussion and Conclusion. Once again, do not fill in those sections. Only add useful comments under the Discussion section.'
        response = openai.Completion.create(
            engine = 'davinci-instruct-beta',
            prompt = prompt,
            max_tokens = 250,
            # stop='.',
            temperature = 0.6,            
        )
        chat_bot_response = response['choices'][0]['text']
        print(response)
    return render(request, 'index.html', {'response': chat_bot_response})
# Create your views here.

def chat_json_response(request):
    chat_response = None
    if api_key is not None and request.method == 'POST':
        openai.api_key = api_key
        user_input = request.POST.get('user_input')
        prompt = f'Provide a template for an experiment with the following title: {user_input}. Sample template: Supoose the question was: Determine the Boiling Point of Milk. \n Then a good template would be:\n Title: To Determine the boiling point of milk. \n Introduction: \n Diagram: \n Table of Results: \n Analysis of Results: \n Precautions: \n Discussion: \n What are the sources of error? \n How could this method be applied to different materials? \n Why would measuring boiling points have useful applications in industry? \n Conclusion: \n Come up with a similar template for the experiment {user_input}. Tailor the helpful comments in the discussion to the specific experiment. Do not mention the sample template specifically in the response.'
        response = openai.Completion.create(
            engine = 'davinci-instruct-beta',
            prompt = prompt,
            max_tokens = 250,
            temperature = 0.6,
        )
        chat_bot_response = response['choices'][0]['text']
        print(response)
    return JsonResponse({'chat_bot_response': chat_bot_response})