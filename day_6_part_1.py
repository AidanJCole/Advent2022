with open("day_6.txt", 'r') as f:
    txt = f.read()
    end = 4
    for i in range(len(txt)-end):
        if len(set(txt[i:i+end]))==4:
            print(i+end)