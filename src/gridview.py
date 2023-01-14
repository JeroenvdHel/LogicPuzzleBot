from __future__ import annotations
from dataclasses import dataclass

@dataclass(frozen=True)
class Item:
    name: str
    domain: Domain
    group: Group
    row: int = 0
    col: int = 0

@dataclass(frozen=True)
class Group:
    name: str
    xpos: int = 0
    ypos: int = 0

@dataclass(frozen=True)
class Domain(Group):
    isDomain: bool = True


if __name__ == '__main__':
    groups = []
    catlist = ["Name,0,1","Surname,1,0","Position,2,3","Cake,3,2"]

    for cat in catlist:
        c = cat.split(",")
        g = Group(c[0], c[1], c[2])
        # print(g)
        groups.append(g)
    
    print("-"*20)
    print("x (Horizontal)")
    xsorted = sorted(groups, key=lambda g: g.xpos)
    print([xs.name for xs in xsorted if xs.xpos != 0])
    print("-"*20)
    print("y (Vertical)")
    ysorted = sorted(groups, key=lambda g: g.ypos)
    print([ys.name for ys in ysorted if ys.ypos != 0])
