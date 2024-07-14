def grashof(L1,L2,L3,L4):
        links = [L1,L2,L3,L4]
        links.sort()
        s, l, p, q = links[0], links[3], links[1], links[2]
        if (s+l) <= (p+q):
            if L1 == L2 and L3 == L4:
                link_type = "Parallel-crank mechanism"
            elif L1 == links[0]:
                link_type = "Drag-link mechanism"
            elif L3 == links[0] or L4 == links[0]:
                link_type = "Crank-rocker mechanism"
            elif (s+l) > (p+q):
                link_type = "Double-rocker mechanism"
        else:
            link_type = "Rocker-crank mechanism"
        return link_type

selikem=grashof(50,200,150,205)
print(type(selikem))