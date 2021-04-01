import json

# def checkForFunc(inputText):
# 	if inputText == 'quit()':
# 		print('quitted')
# 		return continue
# 	elif inputText == 'retry()':
# 		print('retried')
		

def main():

	hasIdeas = True

	while hasIdeas:
		ideaDict = {}
		ideaType = input('What is your idea type?: ')
		# checkForFunc(ideaType)
		if ideaType == 'workshop':
			ideaDict['type'] = ideaType


			code = input("What is the workshop code?: ")
			# checkForFunc(code)
			if code == 'quit()':
				break
			elif code == 'retry()':
				continue
			else:	
				ideaDict['code'] = code

		elif ideaType == 'comp':
			ideaDict['type'] = ideaType

		elif ideaType == 'quit()':
			break
		else:

			print('Invalid Type. Try Again.')
			continue

		description = input('Describe the idea: ')
		# checkForFunc(description)
		
		ideaDict['description'] = description
		f = open('../resources/ideas.json', 'r')
		ideas = json.load(f)
		f.close()
		ideas.append(ideaDict)
		
		with open('../resources/ideas.json', 'w') as f:
			json.dump(ideas, f)
			print('Idea Stored!')









if __name__ == "__main__":
	main()