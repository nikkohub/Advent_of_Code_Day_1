with open("data.txt") as data:
    rdata = data.read()
    ldata = rdata.rsplit("\n")


num = 0

dic = {}
mux = 0
sack = 0
for kcal in ldata:
    if kcal == '':
        mux = 0
        num += 1
        p = f"alv:{num}"

    else:
        kcal = int(kcal)
        mux += kcal
        dic[p] = mux
max_value = max(dic.values())

print(max_value)
print(dic)
