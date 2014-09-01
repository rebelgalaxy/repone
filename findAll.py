# date 2014-09-01
# created by rebelgalaxy
# "Don't believe anything you read on the net. Except this. Well, including this, I suppose." Douglas Adams

# find and return all consecutive indices of characters / substrings in string as a list
def findAll(string, character):
  indices = []
	ctemp = 0
	while True:
		index = string.find(character, ctemp)
		if (index != -1):
			ctemp = index+1
			indices.append(index)
		else:
			break
	return indices
	
# test cases
s = "blablabla"
r = findAll(s, 'b')   # 0, 3, 6
print r

s = "that's all folks."
r = findAll(s, 'a')   # 2, 7
print r
