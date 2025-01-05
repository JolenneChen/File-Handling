'''
Create a function that takes the file content in the form of list, then iterate to the data using a for loop with a step or two, because every pair of elements have a question and it's corresponding answer
'''
qna = ["What's a apple?","A fruit.","How many legs do horse have?","4",]

def add_question(qna):
    with open("quiz.txt","w") as p:
         for i in qna:
              p.write(i + "\n")
    return qna

'''
Next for its iteration, give prompt user with the question, take the input for the answer and compare it with the correct answer. If the user answer matches the correct answer the program increment the score and prints correct otherwise it'll print incorrect
'''

def read_question(file_name,answer):
    score = 0
    with open(file_name,"r") as r:
        content = r.readlines()
        for i in range(0,len(content),2):
            question = content[i]
            print(question)
            real_answer = content[i+1]
            print(real_answer)
            answer = input("Whats the answer? : ")
            if answer == real_answer.strip():
                print("Correct")
            else:
                print(f"Wrong, The correct answer is :  {real_answer}")
    
        
            
read_question("quiz.txt", "answer")
