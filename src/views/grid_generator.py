import os
from txt_gui_parts import TXT_GRID_ART as ART
from collections import namedtuple
# from box import Box


Line = namedtuple("Line", ["begin", "hline", "sep", "end"])

DataRow = namedtuple("DataRow", ["begin", "hfill", "sep", "end"])

TableFormat = namedtuple(
    "TableFormat",
    [
        "lineabove",
        "linebelowheader",
        "linebetweenrow",
        "headerrow",
        "datarow",
        "linebelow",
        "padding"
    ]
)

tf = TableFormat(
    lineabove=Line("┏", "━", "┳", "┓"),
    linebelowheader=Line("┏", "━", "╋", "┫"),
    linebetweenrow=Line("┣", "━", "╋", "┫"),
    headerrow=DataRow("┃", "", "┃", "┃"),
    datarow=DataRow("┃", "", "┃", "┃"),
    linebelow=Line("┗", "━", "┻", "┛"),
    padding=1,
)


def get_maxstr_length(inputlist: list[str]) -> int:
    res = max(inputlist, key=len)
    return len(res)


def get_minstr_length(inputlist: list[str]) -> int:
    res = min(inputlist, key=len)
    return len(res)


def generate_header_row(cols: list[str] = ["123", "123456789", "12345"]):
    colwidth = 1+(2*tf.padding)
    maxstr = get_maxstr_length(cols)
    minstr = get_minstr_length(cols)
    headerwidth = maxstr+3
    lines = []

    # for y in range(maxstr+2+(tf.padding*2)):
    for y in range(maxstr+1+(tf.padding*2)):

        if y == 0:

            # top border
            line = tf.lineabove
            inside = line[1]*((tf.padding*2)+1)

        elif y == 1 or y == (maxstr+(tf.padding*2)):
        # elif y == 1 or y == (maxstr+(tf.padding*2))-1:

            # top and bottom padding line
            line = tf.datarow
            inside = " "*((tf.padding*2)+1)

        elif y == (maxstr+1+(tf.padding*2)):

            # bottom border
            line = tf.linebelow
            inside = line[1]*((tf.padding*2)+1)

        else:
            # DATAROW
            # Get correct char of nounname
            line = tf.datarow
            inside = f"{' '*(tf.padding)}{' '}{' '*(tf.padding)}"

        # add top border
        topline = []

        # spacing nounnames column
        topline.append(" "*headerwidth)

        # add begin line
        topline.append(line[0])

        # add colwidth and sep for each col except last
        for x in range(len(cols)):

            if x == len(cols)-1:
                endchar = line[3]
            else:
                endchar = line[2]

            # stringpos_range = range(2, maxstr+(tblFormat.padding*2))

            strlength = len(cols[x])

            if y > 1 and y < strlength+2:
                topline.append(f" {cols[x][y-2]} ")
            else:
                topline.append(inside)


            topline.append(endchar)
            topline_str = "".join(topline)

            # inside = f"{' '*(tblFormat.padding)}{' '}{' '*(tblFormat.padding)}"

        print(topline_str)

    lines.append(topline_str)

    return lines


def generate_rows(rows: list[str] = ["123", "123456789", "12345"]):
    rowheight = 1+(2*tf.padding)
    maxstr = get_maxstr_length(rows)
    minstr = get_minstr_length(rows)
    rowlist = []
    

    # VOOR IEDERE GRID RIJ
    # for y in range(maxstr+2+(tf.padding*2)):
    for y in range(len(rows)):
        
        row = []

        tflines = {}
        
        if y == 0:
            tflines["sepline"] = tf.linebelowheader
        else:
            tflines["sepline"] = tf.linebetweenrow
        
        tflines["dataline"] = tf.datarow
        
        # ADD END LINE TO LAST ROW
        if y == (len(rows)-1):
            tflines["endline"] = tf.linebelow

        # VOOR IEDERE CONSOLE-REGEL
        # for i,tfline in enumerate(tflines.values()):
        for key,tfline in tflines.items():
                rowline = []
                
                # APPEND first corner / edge to consoleline
                rowline.append(tfline[0])

                # VOOR IEDERE CEL
                for x in range(len(rows)+1):
                    endchar = tfline[3]
                    content = ""

                    # ALS LAATSTE CELL
                    if x <= len(rows)-1:
                        endchar=tfline[2]            
                    
                    #ALS SEPLINE OR ENDLINE
                    # if i == 0:
                    if key != 'dataline':
                        if x == 0:
                            content = tfline[1]*(maxstr+(2*tf.padding))
                        else:
                            content = tfline[1]*((tf.padding*2)+1)
                    # ALS DATALINE
                    else:
                        if x == 0:
                            # GET NOUN
                            noun = rows[y]
                            
                            # Calculate padding space for non-longest nouns
                            diff = maxstr - len(noun)
                            contentlist = [" "*tf.padding, noun, " "*diff, " "*tf.padding ]
                            content = "".join(contentlist)
                        else:
                            content = " "*((tf.padding*2)+1)
                                        
                    rowline.append(content)
                    rowline.append(endchar)
                
                row.append(rowline)

        rowlist.append(row)
    
    for r1 in rowlist:
        for r2 in r1:
            print("".join(r2))
                
   
def create_sub_grid(nouns_per_type:int=4, padding:int=1):
    chars = nouns_per_type+(nouns_per_type-1)
    grid = []

    for y in range(chars):
        
        row=[]

        for x in range(chars):
            if y % 2 == 0:
                if x % 2 == 0:
                    char = "".join([" ", " "*(padding*2)])
                else:
                    char = ART.LINE.Y
            else:   
                if x % 2 == 0:
                    char = ART.LINE.X*((padding*2)+1)
                else:
                    char = ART.CROSS.X.XY
           
            row.append(char)
        
        grid.append(row)
        print("".join(row))

    return grid            

            

if __name__ == '__main__':

    nounTypes = ["Jeroen van der Hel", "Lianne", "Sabrina", "Arthur"]

    os.system('cls')
    
    # result = generate_header_row()
    # result = generate_header_row(cols=nounTypes)
    
    # result = generate_rows()
    # result = generate_rows(rows=nounTypes)

    result = create_sub_grid(nouns_per_type=7)

    print("\n\n")

   