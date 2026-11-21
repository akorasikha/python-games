Favorite_Players = {"Soccer":"Lionel Messi",
                   "Basketball": "Shaquille O' Neil",
                   "Cricket": "Sanju Samsung TV",
                   "Football":"Xavier Worthy"}

for key in Favorite_Players:
    print(key, ":", Favorite_Players[key])

Favorite_Players.update({"Baseball":"Albert Puljos"})

for key in Favorite_Players:
    print(key, ":", Favorite_Players[key])

del Favorite_Players["Baseball"]

for key in Favorite_Players:
    print(key, ":", Favorite_Players[key])