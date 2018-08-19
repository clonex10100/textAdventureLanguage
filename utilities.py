def parse(f):
    results={}
    f = open(f)
    lines=[i[:-1] for i in f if i[:-1] != ""]
    index = 0
    while index < len(lines):
        currentLine = lines[index].split(" ")
        if currentLine[0][0] == "~":
            field = currentLine[0][1:-1]
            end = lines.index("~end"+field+"~")
            results[field] = "\n".join(lines[index+1:end])
            index=end+1
        else:
            results[currentLine[0]] = currentLine[1]
            index+=1
    f.close()
    return results
            

