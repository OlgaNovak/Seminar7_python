
def loger1(v):
    with open('file1.txt','a') as data:
        rasparse="\n".join(map(str,v))
        rasparse=rasparse+"\n"
        data.write(str(rasparse)+"\n")

def loger2(v):
    with open('file2.txt','a') as data:
        rasparse=", ".join(map(str,v))
        rasparse=rasparse+"\n"
        data.write(str(rasparse))