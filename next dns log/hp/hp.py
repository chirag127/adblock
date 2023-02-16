with open("host\\hp\\raw.txt","r") as f:
    lines = f.readlines()
    for line in lines:
        with open("host\\hp\\hp.txt","a") as f1:
            f1.write(f"0.0.0.0 {line}")
            f1.write("\n")

