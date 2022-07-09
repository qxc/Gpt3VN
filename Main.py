import subprocess

initialPrompt = "Your name is Mark. You are a 20 year old business major at University of Columbia in New York. You are at a party at a bar called the Drunken Tab where you met Julie. You have known her for only a few hours but already you think you could spend your whole life with her."
dateFollowup = "What are two places you could take her on a date?"
questionFollowup = "What are two questions you could ask her?"
doFollowup = "What are two activities you could do next with her?"

cmdFile = "gpt3 -e davinci -t .5 -f 1 -p 1 '{} {}' 30 > testing.txt".format(initialPrompt, dateFollowup)
print(cmdFile)

t=subprocess.run(["C:\Program Files\Git\git-bash.exe", '-c', cmdFile], capture_output=True, text=True)
