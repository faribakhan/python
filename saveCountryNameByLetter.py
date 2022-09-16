letter = input("Enter the first letter of your desired countries: ")
data = []
new_file = letter+".txt"
with open("name.txt","r") as fp:
    for line in fp:
        if line[0]== letter.upper():

            data.append(line.replace("\t","").replace("\n",""))
with open(new_file,"w") as f:
    f.write(str(data))
