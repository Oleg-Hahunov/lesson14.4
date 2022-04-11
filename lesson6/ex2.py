def draw_carpet(w, h):

    line = ''
    for i in range(h):
        if i == 0 or i == (h - 1):
            for j in range(w):
                if j == 0 or j == (w - 1):
                    line += '▓'
                else:
                    line += '░'
            print(line)
            line = ''
        else:
            for k in range(w):
                if k == 0 or k == (w - 1):
                    line += '▓'
                elif k == 1 or k == (w - 2):
                    line += '░'
                else:
                    line += '▒'
            print(line)
            line = ''
