from constraint import Problem, AllDifferentConstraint
from pathlib import Path
from txt_reader import parse_txt


def solve_problem(p:Problem, data:list, clues:list):
	groups = len(data[0][1])
	domains = len(data)
	criteria_items = []
	for i in data:
		criteria_items += i[1]

	p.addVariables(criteria_items, list(range(1, groups + 1)))
	for row in data:
		# p.addConstraint(AllDifferentConstraint(), cat)
		p.addConstraint(AllDifferentConstraint(), row[1])
		
	for clue in clues:
		if clue[2] == '1':
			p.addConstraint(match, (clue[0], clue[1]))
		else:
			p.addConstraint(no_match, (clue[0], clue[1]))

	solutions = p.getSolutions()
	solution = solutions[0]
	print(len(solution))

	for i in range(1, len(data[0][1]) + 1):
		r = []
		print("--------------------")
		for x in solution:
			if solution[x] == i:
				r.append(x)
		print(f"{i}: {r}")

def no_match(a, b):
	return a != b

def match(a, b):
	return a == b



# sorteddict = {}
# for d in range(domains):
# 	# globals()[f"d{d+1}"] = []
# 	sorteddict[f"d{d+1}"] = []

# for i in range(1, domains + 1):
# 	r = []

# 	print("--------------------")
# 	for x in solution:
# 		if solution[x] == i:
# 			y = [x, solution[x], i]
# 			domain = ''
# 			for idx, d in enumerate(data, start=1):
# 				if x in d[1]:
# 					domain = idx
# 					break
# 			r.append([x, solution[x], domain])

# 	r.sort(key=lambda x: x[2])
# 	# print(r)
# 	sorted = [x[0] for x in r]
# 	print(sorted)
# 	# for c in range(domains):
# 	# 	r.append(sorteddict[f"d{c+1}"][i-1])
# 	# print(f"{i}: {r}")

# 	# for x in solution:
# 	# 	if solution[x] == i:
# 	# 		r.append(x)
# 	# print(f"{i}: {r}")


if __name__ == '__main__':
	p = Problem()
	data_folder = Path(__file__).parents[1] / "puzzles"
	datafile = data_folder / "einstein" / "medium" / "7.txt"

	data, clues = parse_txt(datafile)
	solve_problem(p, data, clues)
	