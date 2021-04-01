import json



if __name__ == "__main__":
	with open('../resources/ideas.json', 'r') as f:
		ideas = json.load(f)
		print(ideas)