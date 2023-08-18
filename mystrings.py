first_name = "   Joh.n"
last_name = "   Do,e"

fst = first_name.strip()
lst = last_name.strip()
x = slice(0,3)
x2 = slice(4,0)
y= slice(2)

print(fst[x]+fst[x2] + " "+ lst[y])

