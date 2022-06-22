with open("sites\\N.txt", "r") as f:
    news_sites = f.readlines()
        
with open("U.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        if "comment" in line:
            with open("C.txt", "a") as f:
                f.write(line)
        else:
            for news_site in news_sites:
                if news_site in line:
                    with open("N.txt", "a") as f:
                        f.write(line)
