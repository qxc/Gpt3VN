import openai
openai.api_key = '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'

_model = "text-davinci-002"
_echo=False
_temperature=.7
_presence_penalty = 1
_frequency_penalty = 1
_max_tokens = 100
_prompt=""
_n=1
_best_of = 2

datePronoun = "her"

locationPrompt = "What are two places you could go to together?"
questionPrompt = "What are two questions you could ask?"
activityPrompt = "What are two activties you could do together?"

questionPromptFollowup = "You ask "
continuePrompt = "What happens next?"

sampleDialogue = ""

def setup():
    #name = input("What is your name? ")
    name = "Kevin"
    global _prompt
    _prompt = f"""Your name is {name}. You are a 20 year old business major at University of Columbia New York.
        You are at a party at a bar called the Drunken Tab where you just walked up to a beautiful woman."""
    dateName = "Julie"
    sampleDialogue = f"{name}: Hi, my name is {name}. What is your name?\n{dateName}: My name is {dateName}. Nice to meet you."
    #sampleQuestion = "What are two questions you could ask? \n 1. What do you like to do for fun? \n 2. What is your favorite band? \n You ask, What do you like to do for fun?"
    _prompt = _prompt + '\n' + sampleDialogue + '\n' + '\n' + questionPrompt
    print(_prompt)

def preparePrompt(text):
    text = text.strip()
    splitText = text.partition('\n')
    print(splitText[0])
    print(splitText[2])

    choice = input("What would you like to ask? (1 or 2) ")
    if choice == '1':
        newText = questionPromptFollowup + splitText[0]
    else:
        newText = questionPromptFollowup + splitText[2]
    print(newText)
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
    return completion.choices[0].text

def main():
    global _prompt
    setup()
    while True:
        completion = callGpt(_prompt)
        _prompt = _prompt + completion + '\n' + preparePrompt(completion)
        print ('---------------------------')
        #print(_prompt)
        print(callGpt(_prompt))

def test():
    txt = "What is your favorite food?"
    print(txt)
    print(callGpt(txt))

#test()
main()
