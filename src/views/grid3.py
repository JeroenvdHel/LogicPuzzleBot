

# size = len(headers) - 1

def create_grid(data):
	grid = {}

	# determine longest header for outlining first col
	nounlist = parse_datadict_to_flat_list(data)
	maxstr = get_maxstr_length(nounlist)

	
	# create row headers
	row_headers = [headers[1]] + [headers[i] for i in range(len(headers)-1, 1, -1)]
	
	# print the headers
	print(" ".join(col_headers))
	
	for idx,i in enumerate(row_headers):
		rev = list(reversed(range(len(row_headers)+1)))
		row = ['.'] * rev[idx]
		row.insert(0, i)
		print(" ".join(row))


# SUB FUNCTIONS
def create_columnheaders(colheaders:list[str], maxstr:int) -> list[str]:
	# create col headers
	col_headers = [headers[0]] + [headers[i] for i in range(2, len(headers))]
	col_headers.insert(0, " ")


def create_rowheaders(rowheaders:list[str]) -> list[str]:
	pass






# HELPER FUNCTIONS

def parse_datadict_to_flat_list(datadict:dict(list)) -> list[str]:
    return sorted({x for v in datadict.values() for x in v})


def get_maxstr_length(inputlist: list[str]) -> int:
    res = max(inputlist, key=len)
    return len(res)


def get_minstr_length(inputlist: list[str]) -> int:
    res = min(inputlist, key=len)
    return len(res)
						
if __name__ == '__main__':
	# data = ['1', '2', '3', '4', '5', '6', '7']
	data = {'1': ['1.1', '1.2', '1.3', '1.4'],
			'2': ['2.1', '2.2', '2.3', '2.4'],
			'3': ['3.1', '3.2', '3.3', '3.4'],
			'4': ['4.1', '4.2', '4.3', '4.4']}