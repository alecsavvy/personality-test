# a short Myers Briggs Test

import random

# create a master questions list of question objects
questionsList = []

# creating question class to contain question data


class Question:
    def __init__(self, question, group):
        self.question = question[0]
        self.direction = question[1]
        self.group = group
        self.A = True
        self.B = False
        self.scores = None

    def ask(self):
        """
        uses a while loop to ask user a question
        their answer determines the score which is returned

        returns answer value
        """
        while True:
            print(self.question)
            answer = input("yes or no: ")
            if answer.lower() == "yes" or answer.lower() == "no":
                answer = answer.lower()
                if answer == "yes":
                    answer = True
                    break
                else:
                    answer = False
                    break
            else:
                print("not a valid answer")
                continue
        if self.direction:
            if answer:  # answer was yes
                self.scores = questionScores(self.A, self.group)
                return None
            else:
                self.scores = questionScores(self.B, self.group)
                return None

        else:  # question answer is reversed
            if answer:
                self.scores = questionScores(self.B, self.group)
                return None
            else:
                self.scores = questionScores(self.A, self.group)
                return None

    def getQuestion(self):
        return self.question

    def getDirection(self):
        return self.direction

    def getScores(self):
        return self.scores


# creating questions, true value means they score fowards, false means they score reversed
opennessItems = [["i have excellent ideas", True],
                 ["i am quick to understand things", True],
                 ["i use difficult words", True],
                 ["i am full of ideas", True],
                 ["i am not interested in abstractions", False],
                 ["i do not have a good imagination", False],
                 ["i have difficulty understanding abstract ideas", False]
                 ]

conscientiousnessItems = [["i am always prepared", True],
                          ["i pay attention to detail", True],
                          ["i get chores done right away", True],
                          ["i like order", True],
                          ["i follow a schedule", True],
                          ["i am exacting in my work", True],
                          ["i leave my belongings around", False],
                          ["i make a mess of things", False],
                          ["i often forget to put things back in their proper place", False],
                          ["i shirk my duties", False]
                          ]

extroversionItems = [["i am the life of the party", True],
                     ["i don't mind being the center of attention", True],
                     ["i feel comfortable around people", True],
                     ["i start conversations", True],
                     ["i talk to a lot of different people at parties", True],
                     ["i don't talk a lot", False],
                     ["i think a lot before i speak or act", False],
                     ["i don't like to draw attention to myself", False],
                     ["i am quiet around strangers", False],
                     ["i have no intention of talking in large crowds", False]
                     ]

agreeablenessItems = [["i am interested in people", True],
                      ["i sympathize with others' feelings", True],
                      ["i have a soft heart", True],
                      ["i take time out for others", True],
                      ["i feel others' emotions", True],
                      ["i make people feel at ease", True],
                      ["i am not really interested in others", False],
                      ["i insult people", False],
                      ["i am not interested in other people's problems", False],
                      ["i feel little concern for others", False]
                      ]

neuroticismItems = [["i get irritated easily", True],
                    ["i get stressed out easily", True],
                    ["i get upset easily", True],
                    ["i have frequent mood swings", True],
                    ["i worry about things", True],
                    ["i am much more anxious than most people", True],
                    ["i am relaxed most of the time", False],
                    ["i seldom feel blue", False]
                    ]

# function that creates question objects for each of the values in their respective lists


def createQuestions():

    print()
    print("loading...")
    print()

    # creates openness questions
    print("creating openness questions...")
    for statement in opennessItems:
        question = Question(statement, "O")
        questionsList.append(question)

    print("creating conscientiousness questions...")
    for statement in conscientiousnessItems:
        question = Question(statement, "C")
        questionsList.append(question)

    print("creating extroversion questions...")
    for statement in extroversionItems:
        question = Question(statement, "E")
        questionsList.append(question)

    print("creating agreeableness questions...")
    for statement in agreeablenessItems:
        question = Question(statement, "A")
        questionsList.append(question)

    print("creating neuroticism questions...")
    for statement in neuroticismItems:
        question = Question(statement, "N")
        questionsList.append(question)

    print()
    print()
    print("Welcome to my personality test!")
    print()

    return None


# function that returns a list of answer values based on return value from ask() method in Question


def questionScores(answer, group):
    # scores goes in E, I, S, N, T, F, J, P
    scores = []
    if answer:
        if group == "N":
            scores.append(-0.18)  # E
            scores.append(0.14)  # I
            scores.append(-0.16)  # S
            scores.append(0.21)  # N
            scores.append(-0.29)  # T
            scores.append(0.36)  # F
            scores.append(-0.25)  # J
            scores.append(0.30)  # P
            return scores

        elif group == "E":
            scores.append(0.58)  # E
            scores.append(-0.58)  # I
            scores.append(-0.08)  # S
            scores.append(0.02)  # N
            scores.append(0.02)  # T
            scores.append(0.05)  # F
            scores.append(-0.06)  # J
            scores.append(0.03)  # P
            return scores

        elif group == "O":
            scores.append(-0.30)  # E
            scores.append(0.30)  # I
            scores.append(-0.60)  # S
            scores.append(0.71)  # N
            scores.append(-0.34)  # T
            scores.append(0.35)  # F
            scores.append(-0.07)  # J
            scores.append(0.03)  # P
            return scores

        elif group == "A":
            scores.append(-0.08)  # E
            scores.append(-0.01)  # I
            scores.append(-0.11)  # S
            scores.append(0.29)  # N
            scores.append(0.52)  # T
            scores.append(0.52)  # F
            scores.append(0.00)  # J
            scores.append(0.00)  # P
            return scores

        elif group == "C":
            scores.append(-0.11)  # E
            scores.append(0.01)  # I
            scores.append(0.03)  # S
            scores.append(0.03)  # N
            scores.append(0.02)  # T
            scores.append(0.02)  # F
            scores.append(0.56)  # J
            scores.append(0.62)  # P
            return scores

        else:
            return None

    else:
        if group == "N":
            scores.append(-0.24)  # E
            scores.append(0.26)  # I
            scores.append(-0.02)  # S
            scores.append(0.03)  # N
            scores.append(-0.16)  # T
            scores.append(0.18)  # F
            scores.append(0.01)  # J
            scores.append(0.00)  # P
            return scores

        elif group == "E":
            scores.append(-0.69)  # E
            scores.append(0.46)  # I
            scores.append(-0.18)  # S
            scores.append(0.16)  # N
            scores.append(0.09)  # T
            scores.append(0.05)  # F
            scores.append(-0.03)  # J
            scores.append(0.02)  # P
            return scores

        elif group == "O":
            scores.append(0.21)  # E
            scores.append(0.22)  # I
            scores.append(0.52)  # S
            scores.append(0.49)  # N
            scores.append(0.22)  # T
            scores.append(0.22)  # F
            scores.append(-0.24)  # J
            scores.append(0.24)  # P
            return scores

        elif group == "A":
            scores.append(0.12)  # E
            scores.append(-0.01)  # I
            scores.append(0.03)  # S
            scores.append(0.03)  # N
            scores.append(0.40)  # T
            scores.append(0.40)  # F
            scores.append(0.06)  # J
            scores.append(0.00)  # P
            return scores

        elif group == "C":
            scores.append(0.03)  # E
            scores.append(0.06)  # I
            scores.append(0.20)  # S
            scores.append(0.24)  # N
            scores.append(-0.28)  # T
            scores.append(-0.28)  # F
            scores.append(0.50)  # J
            scores.append(-0.41)  # P
            return scores

        else:
            return None


# function used to add all the scores together for the classification


def applyScores():
    global extroversion
    extroversion = 0
    global introversion
    introversion = 0
    global sensation
    sensation = 0
    global intuition
    intuition = 0
    global thinking
    thinking = 0
    global feeling
    feeling = 0
    global judging
    judging = 0
    global perceiving
    perceiving = 0

    for question in questionsList:
        scores = question.getScores()
        extroversion += scores[0]
        introversion += scores[1]
        sensation += scores[2]
        intuition += scores[3]
        thinking += scores[4]
        feeling += scores[5]
        judging += scores[6]
        perceiving += scores[7]
    return None

# function to ask all the questions once they are made


def askQuestions():
    for question in questionsList:
        question.ask()

    return None


# function to present the score of the test


def shareScore():
    score = ""
    print()
    print("loading...")
    if extroversion >= introversion:
        score += "E"
    else:
        score += "I"

    if sensation >= intuition:
        score += "S"
    else:
        score += "N"

    if thinking >= feeling:
        score += "T"
    else:
        score += "F"

    if judging >= perceiving:
        score += "J"
    else:
        score += "P"

    print()
    print("your type is: ", score)
    print()

    print("individual results: ")
    print("extroversion: ", str(extroversion))
    print("introversion: ", str(introversion))
    print("sensation: ", str(sensation))
    print("intuition: ", str(intuition))
    print("thinking: ", str(thinking))
    print("feeling: ", str(feeling))
    print("judging: ", str(judging))
    print("perceiving: ", str(perceiving))

    print()
    print()
    print("thank you for taking this test")
    print()
    print("created by Alec Savvy")
    print("inspired by the official Myers Briggs personality test")


def main():
    createQuestions()
    askQuestions()
    applyScores()
    shareScore()
    return None

main()


