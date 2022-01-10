with open("sites\\N.txt", "r") as f:
    newssites = f.readlines()
        
with open("U.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        if "comment" in line:
            with open("C.txt", "w") as f:
                f.write(line)
        else:
            for newssite in newssites:
                if newssite in line:
                    with open("N.txt", "a") as f:
                        f.write(line)
