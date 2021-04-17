felix = open('Final_list.txt', 'r')
txtfile = []
lst = [line.split('\n') for line in felix.readlines()]
for i in range(len(lst)):
    for j in range(len(lst[i])):
        if not lst[i][j].strip():
            continue
        txtfile.append(lst[i][j])

print(len(txtfile))
with open('New Text Document.txt', 'w') as f:
    [f.write('"%s ",' % item) for item in txtfile]
for i in txtfile:
    print(i)




