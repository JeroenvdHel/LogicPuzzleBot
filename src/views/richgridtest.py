from rich import print
from rich.table import Table, Column, Row


if __name__ == '__main__':
    col1 = Column()
    col2 = Column()
    col3 = Column()
    # row1 = "A1", "B1", "C1"
    # row2 = Row("A2", "B2", "C2")
    # row3 = Row("A3", "B3", "C3")

    grid = Table.grid()
    grid.add_column(col1)
    grid.add_column(col2)
    grid.add_column(col3)
    grid.add_row("A1", "B1", "C1")
    grid.add_row("A2", "B2", "C2")
    grid.add_section()
    grid.add_row("A3", "B3", "C3")


    print(grid)