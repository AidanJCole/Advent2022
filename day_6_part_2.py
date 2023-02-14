with open("day_6.txt", 'r') as f:
    txt = f.read()
    end = 14
    for i in range(len(txt)-end):
        if len(set(txt[i:i+end]))==end:
            print(i+end)