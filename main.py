# Generate a quiz.txt file and add the quiz question to it, and the answer

with open("quiz.txt","w") as q:
    q.write("What is the capital of France?\n")
    q.write("Paris.\n")
    q.write("\n")
    q.write("What does vocabulary means?\n")
    q.write("It is the total number of words you know in a particular language. \n")
    q.write("\n")
    q.close()

# to read
with open("quiz.txt","r") as r:
    content = r.read()
    print(content)
    r.close()

# a is used to append a new text to the file
with open("quiz.txt","a") as q:
    q.write("How many legs does a turtle have?\n")
    q.write("4\n")
    q.close()


#  write a function which takes a list of question in parameter and is in the file

def add_question(question):
    with open("question.txt","a") as p:
        for i in question:
            p.write(i + "\n")
    return question

question = ["What is a phone?","a tool for communication."]

print(add_question(question))

def read_question(file_name):
    with open(file_name,"r") as r:
        content = r.read().splitlines()
        print(content)
        r.close()

read_question("question.txt")

