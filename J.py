import math

scores=[]

def get_group_score(scores):
	total = 0
	for i in range(len(scores)):
		total += scores[i] * (4/5)**i
	return total / 5

for i in range(int(input())):
	scores.append(int(input()))

print(get_group_score(scores))

print(sum(
	get_group_score(scores[:i] + scores[i+1:])
		for i in range(len(scores))) / len(scores))