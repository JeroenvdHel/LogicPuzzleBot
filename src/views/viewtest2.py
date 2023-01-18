from pprint import pprint
from box import Box
from txt_gui_parts import TXT_GRID_ART as ART

def grid_factory(noun_types:list[str], nouns:int, isNounTypeSubGrid=False):
    if isNounTypeSubGrid:
        return create_nounType_subgrid(nouns)
    else:
        return create_grid_data(nounTypes)

def create_nounType_subgrid(nouns):
    grid = {}
    for rows in range(nouns):
        row = []
        for cells in range(nouns):
            cell = []
            row.append(cell)
        grid[f"_{rows+1}"] = row

    return grid

def create_grid_data(nountypes):
    orders = create_xy_order(nounTypes)
    x_order = orders['x']
    y_order = orders['y']
    grid = {}
    ycount = 0

    while ycount < len(nounTypes)-1:
        xcount = 0
        #create row
        grid[ycount+1] = {}

        #create cells for current rowconstructor
        while xcount < (len(nounTypes)-ycount-1):
            # cell = f"{x_order[xcount]}<->{y_order[ycount]}"
            cell = {"x": f"{x_order[xcount]}", "y":f"{y_order[ycount]}"}
            grid[ycount+1][chr(65+xcount)] = cell
            xcount += 1

        ycount += 1

    return grid

def create_xy_order(nountypes:list[str]) -> dict:
    result = []
    y_order= []
    x_order = []
    amount = len(nountypes)

    # x_order
    for i,nt in enumerate(nountypes, start=1):
        # Skip second item
        if i != 2:
            x_order.append(nt)

    # y_order
    y_order.append(nountypes[1])
    for i,nt in reversed(list(enumerate(nountypes, start=1))):
        if i > 2:
            y_order.append(nt)

    return Box({"x": x_order, "y": y_order})

def get_dict_keys(mydict):
    result = []
    for d in mydict.keys():
        result.append(d)
    return result

    return [k for k in keys]


def create_grid_txt(data:Box) -> None:
    nounTypes = get_dict_keys(data)
    nounsPerType = len(data[next(iter(data))])
    nt_data = create_grid_data(nounTypes)

    grid_size = grid_x_size = grid_y_size = len(nounTypes)-1

    

    grid = []
    for i in range(grid_size):
        gridrow = []
        rowheight = 8
        for row_subline_index in range(rowheight):
            

            row_sublines = []
            # If NounTypeRow index is 0
            if i == 0:
                for j in range(grid_size):
                    cellrow = []
                    if row_subline_index == 0:
                        h_line = ART.LINE.X2
                        v_line = ""
                        left_sep = ART.CORNER.NW.X2Y2
                        right_sep = ART.CORNER.NE.X2Y2
                        center_sep = ART.CROSS.T.TOP.X2Y2
                    elif row_subline_index == rowheight-1:
                        #bottomborder
                        h_line = ART.LINE.X2
                        v_line = ""
                        left_sep = ART.CORNER.SW.X2Y2
                        right_sep = ART.CORNER.SE.X2Y2
                        center_sep = ART.CROSS.X.X2Y2
                    else:
                        # default cell
                        h_line = ""
                        v_line = ART.LINE.Y2
                        left_sep = ART.CROSS.T.LEFT.X2Y2
                        right_sep = ART.CROSS.T.RIGHT.X2Y2
                        center_sep = ART.CROSS.X.X2Y2
                        
                        cellsubrow = ""
                        
                                        
                    if j == 0:
                        continue
                    
                    if j == 1:
                        cellrow.append(left_sep)
                        
                        for n in range(nounsPerType-1):
                            cellrow.append(h_line*3)
                            cellrow.append(center_sep)
                        
                        cellrow.append(h_line*3)
                        cellrow.append(right_sep)
                        

                    row_sublines.append("".join(cellrow))
                    print(f"cellrow {j}: {cellrow}")
            gridrow.append("".join(row_sublines))   
            print(f"row_sublines {row_subline_index}: {row_sublines}")     
        grid.append("".join(gridrow))      
        print(f"gridrow {i}: {gridrow}")     
        print(grid)  

if __name__ == '__main__':
    
    data = Box({
        "Wife": [
            "Alyssa",
            "Tracy",
            "Alice",
            "Jodie",
            "Suzy"
        ],
        "Husband": [
            "Peter Brennen",
            "Jack Baker",
            "Mark Hartford",
            "Allen Smother",
            "Alex Frost",
        ],
        "Activity": [
            "Horseback",
            "Fort",
            "Sight Seeing",
            "Kayaking",
            "Bicycling"
        ],
        "Souvenir": [
            "Fudge",
            "Lighthouse",
            "Model Ship",
            "Postcards",
            "Maple Syrup"
        ]
    })
    
    nounTypes = get_dict_keys(data)
    nounsPerType = len(data[next(iter(data))])
    

    # orders = create_xy_order(nounTypes)
    # print()
    # print(f"          {' | '.join(orders['x'])}")
    # for y in orders['y']:
    #     print(y)



    # grid = grid_factory(noun_types=nounTypes, nouns=nounsPerType, isNounTypeSubGrid=True)
    grid = create_grid_data(nounTypes)
    # pprint(grid, width=150)

    create_grid_txt(data)



