# Question
class Question:
    def __init__(self,text,choices,answer):
        self.text = text
        self.choices = choices
        self.answer = answer
    
    def checkAnswer(self, answer):
        return self.answer == answer

# Quiz
class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0
        self.questionIndex = 0

    def getQuestion(self):
        return self.questions[self.questionIndex]

    def displayQuestion(self):
        question = self.getQuestion()
        print(f'Soru {self.questionIndex + 1}: {question.text}')

        for q in question.choices:
            print('-'+ q)
        
        answer = input('cevap: ')
        self.guess(answer)
        self.loadQuestion()

    def guess(self, answer):
        question = self.getQuestion()

        if question.checkAnswer(answer):
            self.score += 1
        self.questionIndex += 1

    def loadQuestion(self):
        if len(self.questions) == self.questionIndex:
            self.showScore()
        else:         
            self.displayProgress()  
            self.displayQuestion()

    def showScore(self):
        print('score: ', self.score)
        print(f'Alınan puan : {self.score * 20}')

    def displayProgress(self):
        totalQuestion = len(self.questions)
        questionNumber = self.questionIndex + 1

        if questionNumber > totalQuestion:
            print('Quiz bitti.')
        else:
            print(f'Question {questionNumber} of {totalQuestion}'.center(100,'*'))

q1 = Question('Türkiyenin Başkenti ?', ['Antalya','Ankara','Adana','İstanbul','İzmir'], 'Ankara')
q2 = Question('Bir yıl kaç hafta ?', ['51','52','53','53','55'], '54')
q3 = Question('Türkiyede Kaç tane şehir vardır ?', ['78','79','80','81','82'], '81')
q4 = Question('Alfabenin 5.harfi nedir ?', ['E','F','G','Ğ','H'], 'E')
q5 = Question('Bir sayının yarısın 3 katı 60 ise sayı kaçtır?', ['50','45','44','42','40'], '40')

questions = [q1,q2,q3,q4,q5]

quiz = Quiz(questions)

quiz.loadQuestion()