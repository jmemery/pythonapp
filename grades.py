import random

def grade(scores):
    print "Scores and Grades"
    for x in range(0, scores):
        score = random.randint(60, 101)
        if score >= 60 and score <= 69:
            print "Score: ", score,"; Your grade is a D"
        elif score >= 70 and score <= 79:
            print "Score: ", score, "; Your grade is a C"
        elif score >= 80 and score <= 89:
            print "Score: ", score, "; Your grade is a B"
        elif score >= 90 and score <= 100:
            print "Score: ", score, "; Your grade is an A"
        else:
            print "You failed"
    print "End of the program.  Bye!"

grade(10)
