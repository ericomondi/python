class Perfomance:
    def __init__(self,math, eng, kis, sci, sos ):
        self.math = math
        self.eng = eng
        self.kis = kis
        self.sci = sci
        self.sos = sos
        
    def find_total_marks(self,math, eng, kis, sci, sos):
        total = self.math + self.eng + self.kis + self.sci + self.sos
        print(f'The total is {total}')
    def find_avg_marks(total):
        avg = total / 5
        print(f'The avarage marks is {avg}')
    def find_grade(avg_marks):
        if avg_marks > 79:
            grade = "A"
        elif avg_marks >= 60 and avg_marks <= 79:
            grade = "B"
        elif avg_marks > 49 and avg_marks <= 59:
            grade = "C"
        elif avg_marks >= 40 and avg_marks <= 49:
            grade = "D"
        else:
            grade = "E"
        print(f'The grade is {grade}')
    


s1 = Perfomance(50,50,50,50,50)


s1.find_total_marks()

