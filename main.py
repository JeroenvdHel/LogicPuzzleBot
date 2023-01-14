from src import solver
from pathlib import Path
from src import txt_reader


if __name__ == '__main__':
    data_folder = Path(__file__).parent / "puzzles"
    datafile = data_folder / "einstein" / "medium" / "7.txt"
    datafile = str(datafile)
    data, clues = txt_reader.parse_txt(str(datafile))
    solver.solve_problem(data, clues)
