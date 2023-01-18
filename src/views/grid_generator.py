from txt_gui_parts import TXT_GRID_ART as ART
from collections import namedtuple
# from box import Box

Line = namedtuple("Line", ["begin","hline","sep","end"])
DataRow = namedtuple("DataRow", ["begin", "sep", "end"])
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

tblFormat = TableFormat(
    lineabove=Line("┏", "━", "┳", "┓"),
    linebelowheader=Line("┣", "━", "╋", "┫"),
    linebetweenrow=Line("┣", "━", "╋", "┫"),
    headerrow=DataRow("┃", "┃", "┃"),
    datarow=DataRow("┃", "┃", "┃"),
    linebelow=Line("┗", "━", "┻", "┛"),
    padding=1,
)

def get_longest_value_length(inputlist:list[str]) -> int:
    res = max(inputlist, key=len)
    return len(res)

def generate_header_row(
    cols:list[str]=["NT1", "NTtttttt2", "NTte3"]
    ):
    colwidth = 1+(2*tblFormat.padding)
    maxstr = get_longest_value_length(cols)
    headerwidth = maxstr+7
    
    lines=[]
    
    for y in range(maxstr+2+(tblFormat.padding*2)):
        
        if y == 0:                                                      # top border
            line = tblFormat.lineabove
            inside = line[1]*((tblFormat.padding*2)+1)
        elif y == 1 or y == (maxstr+2+(tblFormat.padding*2))-1:         # top and bottom padding line
            line = tblFormat.datarow
            inside = f"{' '*(tblFormat.padding*2)+1}"
        elif y == (maxstr+2+(tblFormat.padding*2)):                     # bottom border
            line = tblFormat.linebelowheader
            inside=line[1]*((tblFormat.padding*2)+1)
        else:
            # Get right char of nounname
            line = tblFormat.datarow
            inside = f"{' '*(tblFormat.padding)}{' '}{' '*(tblFormat.padding)}"

        #add top border
        topline = []
        #spacing nounnames column
        topline.append(" "*headerwidth)
        # add begin line
        topline.append(line[0])
        # add colwidth and sep for each col except last
        for x in range(len(cols)-1):
            topline.append(inside)
            topline.append(line[2])
        #add last col
        topline.append(inside)
        topline.append(line[3])
        topline_str = "".join(topline)
        print(topline_str)
    lines.append(topline_str)

    return lines


if __name__ == '__main__':
    result = generate_header_row()
    print(result)
# rownum = [1,2,3]
# colnum = [1,2,3]
# colwidth = 3

# max_noun_len = 9

# """
# --- lineabove ---------
#     headerrow
# --- linebelowheader ---
# 	datarow
# --- linebetweenrows ---
# ... (more datarows) ...
# --- linebetweenrows ---
# 	last datarow ------
# --- linebelow ---------
# """







#cells_to_generate = len(colnum)




# # VOOR IEDERE REGEL
# # +2 for NounType titles and NounNames
# for ri in range(len(rownum)):

#     for ci in range(cells_to_generate):
#         print(chr(65+ci),ri+1)
#         #....
#     cells_to_generate -= 1