#class question
class Question():
    def __init__(self,text,choises,answer):
        self.text=text
        self.choises=choises
        self.answer=answer
    def checkAnswer(self,answer):
        return self.answer == answer
#class quiz
class Quiz():
    
    def __init__(self,questions):
        self.questions=questions
        self.score=0
        self.questionsIndex=0
    
    def getQuestion(self):
        return self.questions[self.questionsIndex]            

    def displayQuestion(self):
        question = self.getQuestion()
        print(f"Soru {self.questionsIndex + 1}: {question.text}")
        
        for q in question.choises:
            print("-" + q)
        
        cevap=input("Cevap:")
        print(question.checkAnswer(cevap))
        self.guess(cevap)
        self.loadQuestion()
    
    def guess(self,answer):
        question = self.getQuestion()
        if question.checkAnswer(answer):
            self.score +=1
        self.questionsIndex +=1
        

    def loadQuestion(self):
        if len(self.questions) == self.questionsIndex:
            self.showScore()
        else:
            self.displayProgress()
            self.displayQuestion()

    def showScore(self):
        print("Score:",self.score)

    def displayProgress(self):
        totalQuestion = len (self.questions)
        questionNumber = self.questionsIndex + 1
        
        if questionNumber > totalQuestion:
            print("Quiz Bitti")
        else:
            print(f"Soru {questionNumber} , {totalQuestion} soru icinden")

#main
q1=Question("Arda Turanin Ispanyada Oynadigi ilk takim",["Barcelona","Real Madrid","Villa Real","Atletico Madrid"],"Atletico Madrid")
q2=Question("Arda Guler Hangi Altyapida Oynadi",["Genclerbirligi","Ankaragucu","Kocaeli","Sakaryaspor"],"Genclerbirligi")
q3=Question("Icardi Hangi takimda oynamamistir",["Galatasaray","PSG","Barcelona","Inter","Chelsea"],"Chelsea")

question = [q1,q2,q3]

quiz=Quiz(question)
quiz.loadQuestion()