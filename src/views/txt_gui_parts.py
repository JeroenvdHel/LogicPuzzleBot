from box import Box


TXT_GRID_ART = Box({
    "LINE":{
        "X": "─",
        "Y": "│",
        "X2": "═",
        "Y2": "║", 
    },
    "CORNER": {
        "NW": {
            "XY": "┌",
            "X2Y": "╒",
            "XY2": "╓",
            "X2Y2": "╔",
        },
        "NE":{
            "XY": "┐",
            "X2Y": "╕",
            "XY2": "╖",
            "X2Y2": "╗",
        },
        "SE": {
            "XY": "┘",
            "X2Y": "╛",
            "XY2": "╜",
            "X2Y2": "╝",
        },
        "SW": {
            "XY": "└",
            "X2Y": "╘",
            "XY2": "╙",
            "X2Y2": "╚"
        }
    },
    "CROSS": {
        "X":{
            "XY":"┼",
            "X2Y":"╪",
            "XY2":"╫",
            "X2Y2":"╬"
        },
        "T": {
            "TOP": {
                "XY":"┬",
                "X2Y":"╤",
                "XY2":"╥",
                "X2Y2":"╦"
            },
            "LEFT": {
                "XY":"├",
                "X2Y":"╞",
                "XY2":"╟",
                "X2Y2":"╠"
            },
            "RIGHT": {
                "XY":"┤",
                "X2Y":"╡",
                "XY2":"╢",
                "X2Y2":"╣"
            },
            "BOTTOM": {
                "XY":"┴",
                "X2Y":"╧",
                "XY2":"╨",
                "X2Y2":"╩"
            }
        }
    }
})
  
def create_txt_grid(nouns_per_type:int=5):
    # Create rows
    # For each row
    pass
    

def create_row(nouns_per_type, last_row=False) -> str:
    pass





if __name__ == '__main__':
    
    GRIDART = TXT_GRID_ART
    print(GRIDART.LINE)
    # print(GRIDART.LINE.X)
    # print(GRIDART.CORNER)
    # print(GRIDART.CORNER.NW)
    # print(GRIDART.CORNER.NW.XY)

