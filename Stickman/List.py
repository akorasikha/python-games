List = ["run", "walk", "move", "dance"]

for item in List:
    print(item)

List.append("talk")

for item in List:
    print(item)

del(List[4])

for item in List:
    print(item)