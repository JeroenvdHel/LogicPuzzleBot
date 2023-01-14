import os
from pathlib import Path

def parse_txt(txtfile):
	with open(txtfile, "r", encoding="utf8") as f:
		lines = f.readlines()
		datatype = ""
		counter = 1
		data = []
		clues = []

		for line in lines:
			line = line.strip()
			if "CLUES" in line:
				datatype = "clues"
				continue
			if "DATA" in line:
				datatype = "data"
				continue

			if datatype == "clues":
				# print(f"Clue: [{line}]")
				parsed_line = parse_clueline(line) 
				clues.append(parsed_line)
			elif datatype == "data":
				# print(f"Data: [{line}]")
				parsed_line = parse_dataline(line)
				data.append([str(counter), parsed_line])
				counter += 1
			else:
				print("No clue or data")
	
	return (data,clues)


def parse_clueline(line):
	type = ""
	if line[0] == "-":
		type = "0"
	if line[0] == "+":
		type = "1"

	ll = line[1:].split(',')
	ll.append(type)

	return ll


def parse_dataline(line):
	return line.split(',')

if __name__ == '__main__':
	data_folder = Path(__file__).parents[1] / "puzzles"
	
	f = data_folder / "einstein" / "medium" / "7.txt"
	data, clues = parse_txt(f)
	print(data)
	print(clues)