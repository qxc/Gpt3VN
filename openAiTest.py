import openai
import apikey
import os

os.system("python apikey.py")
openai.api_key = apikey.api_key

_model = "text-davinci-002"
_echo=False
_temperature=.7
_presence_penalty = 1.5
_frequency_penalty = .5
_max_tokens = 100
_prompt=""
_n=1
_best_of = 2

name = "John"

datePronoun = "her"

locationPrompt = "What are two places you could go to together?"
questionPrompt = "What are two questions you could ask?"
activityPrompt = "What are two activties you could do together?"

questionPromptFollowup = f"{name}: "
continuePrompt = "What happens next?"

sampleDialogue = ""

#These initial questions don't seem to affect the subsequent dialogue much. Probably needs to be more involved.

# Seed GPT with some initial text about you. 
def selfSetupQuestions():
    return "You are, " + input("Please enter some adjectives to describe yourself. ") + "."

# Seed GPT with some initial text about your date.
def dateSetupQuestions():
    return "\n Julie is " + input("Please enter some adjectives to describe your date. ") + "."


def setup():
    #name = input("What is your name? ")
    global _prompt
    _prompt = f"""Your name is {name}. You are a 20 year old business major at University of Columbia New York.
        You are at a party at a bar called the Drunken Tab where you just started talking to a beautiful woman named Julie."""
    dateName = "Julie"
    sampleDialogue = f"{name}: Hi, my name is {name}. What is your name?\n{dateName}: My name is {dateName}. Nice to meet you."
    _prompt = selfSetupQuestions() + dateSetupQuestions() + " " + _prompt + '\n' + sampleDialogue + setFollowUp()
    print(_prompt)
    return _prompt

def setFollowUp():
    return '\n' + questionPrompt

def preparePrompt(text):
    text = text.strip()
    splitText = text.partition('\n')

    choice = input("What would you like to ask? (1 or 2) ")
    if choice == '1':
        newText = questionPromptFollowup + splitText[0].split(' ', 1)[-1]
    else:
        newText = questionPromptFollowup + splitText[2].split(' ', 1)[-1]
    return newText

def callGpt(text):
    completion = openai.Completion.create(
        model=_model,
        echo = _echo,
        temperature = _temperature,
        presence_penalty = _presence_penalty,
        frequency_penalty = _frequency_penalty,
        max_tokens = _max_tokens,
        prompt = text,
        n = _n,
        best_of = _best_of)
    text = completion.choices[0].text
    print(text)
    return text

def main():
    global _prompt
    #Initial formatting of prompt for information & formatting
    _prompt = setup()
    
    while True:
        # Call GPT on the prompt
        completion = callGpt(_prompt)
        
        # Ask the user which follow-up question they would like to ask
        qPromptFollowup = preparePrompt(completion)
        print(qPromptFollowup)
        _prompt = '\n' + qPromptFollowup
        
        # Feed GPT follow-up question
        completion = callGpt(_prompt)
        _prompt = _prompt + completion + setFollowUp()

def test():
    txt = "What is your favorite food?"
    print(txt)
    print(callGpt(txt))

#test()
main()
