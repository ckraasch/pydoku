print("Hello world!")

filename="sudoku_001.txt"
with open(filename) as f:
	content = f.readlines()
content = [x.strip() for x in content] 
print(content)

print("Bye world!")

