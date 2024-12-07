class Score():
    def __init__(self,score1,score2,score3,score4,score5,score6,score7,score8,score9,score10):
        self.score1=score1
        self.score2=score2
        self.score3=score3
        self.score4=score4
        self.score5=score5
        self.score6=score6
        self.score7=score7
        self.score8=score8
        self.score9=score9
        self.score10=score10
        self.average()

    def average(self):
        avg=(score1+score2+score3+score4+score5+score6+score7+score8+score9+score10)/10
        print("your memory score was : ",avg,"out of 100")

score1=int(input("enter your score of 1st standard"))
score2=int(input("enter your score of 2st standard"))
score3=int(input("enter your score of 3st standard"))
score4=int(input("enter your score of 4st standard"))
score5=int(input("enter your score of 5st standard"))
score6=int(input("enter your score of 6st standard"))
score7=int(input("enter your score of 7st standard"))
score8=int(input("enter your score of 8st standard"))
score9=int(input("enter your score of 9st standard"))
score10=int(input("enter your score of 10st standard"))

Score(score1,score2,score3,score4,score5,score6,score7,score8,score9,score10)