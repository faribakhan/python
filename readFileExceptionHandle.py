lines = ["THis is first line","This is second line","I am a great programmer"]

with open("text.txt","w", encoding="utf-8") as fp:
    for line in lines:
        fp.write(line+"\n")
import io


filename = "file.txt"
mode = "r"
try:
    with open(filename,mode) as fp:
        content = fp.read()
        print(content)
except FileNotFoundError:
    print(filename +" not found. Please check the file name.")
except io.UnsupportedOperation:
    print("Are you sure ",filename," is readable?")