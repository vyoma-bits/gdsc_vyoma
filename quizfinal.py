
class Operation:
    
    def __init__(self, questions):
        self.questions = questions
        self.marks =0

    
    def start(self):
        for question in self.questions:
            question.Display()
           
            answer = input("Enter your answer (True/False): ")
            if self.check_answer(question, answer):
                
                
                self.marks += 2
                print("correct",self.check_answer(question, answer))
                
                
            else:
                
                self.marks-=1
                
            print()
       
        print("You marksd " + str(self.marks) + " out of " + str(len(self.questions)*2))

   
    def check_answer(self, question, answer):
        
        correct_answer = question.text[0:4:]
        if correct_answer=="Fals":
            correct_answer="False"
        return answer==correct_answer
class Question_set:
   
    def __init__(self, text, choice_1, choice_2):
        self.text = text[::]
        self.choice_1 = choice_1
        self.choice_2 = choice_2
        
   
    def Display(self):
        print(self.text[5::])
        print("A. " + self.choice_1)
        print("B. " + self.choice_2)
        
     
        
question_data =[
{"text": "A slug's blood is green.", "answer": "True"},
{"text": "The loudest animal is the African Elephant.", "answer": "False"},
{"text": "Approximately one quarter of human bones are in the feet.", "answer": "True"},
{"text": "The total surface area of a human lungs is the size of a football pitch.", "answer": "True"},
{"text": "In West Virginia, USA, if you accidentally hit an animal with your car, you are free to take it home to eat.", "answer": "True"},
{"text": "In London, UK, if you happen to die in the House of Parliament, you are entitled to a state funeral.", "answer": "False"},
{"text": "It is illegal to pee in the Ocean in Portugal.", "answer": "True"},
{"text": "You can lead a cow down stairs but not up stairs.", "answer": "False"},
{"text": "Google was originally called 'Backrub'.", "answer": "True"},
{"text": "Buzz Aldrin's mother's maiden name was 'Moon'.", "answer": "True"},
{"text": "No piece of square dry paper can be folded in half more than 7 times.", "answer": "False"},
{"text": "A few ounces of chocolate can to kill a small dog.", "answer": "True"}
]
l=[]
for i in range(12):
    l.append(question_data[i]["answer"]+" "+question_data[i]["text"])
    
question_1 = Question_set(l[0],  "True", "False")
question_2 = Question_set(l[1], "True", "False")
question_3 = Question_set(l[2],  "True", "False")
question_4 = Question_set(l[3], "True", "False")
question_5 = Question_set(l[4],  "True", "False")
question_6 = Question_set(l[5],  "True", "False")
question_7 = Question_set(l[6],  "True", "False")
question_8 = Question_set(l[7],  "True", "False")
question_9 = Question_set(l[8],  "True", "False")
question_10 = Question_set(l[9], "True", "False")
question_11= Question_set(l[10],  "True", "False")
question_12= Question_set(l[11],  "True", "False")

questions = [question_1,question_2,question_3,question_4,question_5,question_6,question_7,question_8,question_9,question_10,question_11,question_12]


quiz = Operation(questions)

print("welcome to the quiz +2 for correct ,-1 for negative be careful with the uppercase and lowercase")
quiz.start()
