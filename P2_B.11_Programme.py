import random as rand
def build_questionnaire(filename):
     """
         Construit le QCM avec les questions contenue dans le fichier donné.
         :type filename: Un string représentant le nom du fichier a charger.
 
         :return: Une liste de questions
     """
     questions = []
     wording = None
     choices = []
     with open(filename, encoding='utf-8') as file:
         for line in file.readlines():
             if '|' not in line:
                 if wording or choices:
                     questions.append([wording, choices])
                 wording = None
                 choices = []
             else:
                 parts = line.strip().split('|')
                 if 1 < len(parts) < 5:
                     if parts[0] == 'Q':
                         if not wording and not choices:
                             wording = parts[1]
                             choices = []
                         else:
                             questions.append([wording, choices])
                             wording = None
                             choices = []
                     elif parts[0] == 'A':
                         if parts[2] not in ('V', 'X'):
                             print("Error when loading line:\n\t{}".format(line))
                         else:
                             choices.append([parts[1], parts[2] == 'V', parts[3] if len(parts) > 3 else ''])
                     else:
                         print("Error when loading line:\n\t{}".format(line))
                 else:
                     print("Error when loading line:\n\t{}".format(line))
 
                 if line.startswith('Q'):
                     wording = parts[1]
 
     if wording or choices:
         questions.append([wording, choices])
     return questions

 
"""
     Exemple d'utilisation de la librairie de lecture de fichiers QCM
1
"""
 
def questionaire(liste):
    reponses = []
    for i in range(len(liste)):
        print(liste[i][0])
        cmt = 0
        for j in range(len(liste[i][1])):
            print(j+1 , liste[i][1][j][0])
            if liste[i][1][j][1] == True:
                cmt = cmt + 1
        sRep = []
        if cmt <= 1:
            reponses.append([[int(input())],liste[i][1]])
        else:
            print("il y a plusieurs choix possible à cette réponse \n veillez encoder vos données une par une puis terminer par un 'f' ")
            while(True):
                x = input()
                if x == 'f':
                    break
                sRep.append(int(x) - 1)
            reponses.append([sRep,liste[i][1]])
    return reponses

def correctionSimple(reponses):
    score = 0
    for i in range(len(reponses)):
        if((len(reponses[i][0])) == 1):
            if reponses[i][1][reponses[i][0][0]]:
                score += 1
        else:
            acc = 0
            scoreTemp = 0
            for j in range(len(reponses[i][0])):
                if reponses[i][1][j][1]:
                    scoreTemp += 1
            for j in range(len(reponses[i][1])):
                if reponses[i][i][j][1]:
                    acc += 1
            score += scoreTemp / acc
    return score
        

if __name__ == '__main__':
     filename = "QCM.txt"
 
     # Chargement du questionnaire
     questions = build_questionnaire(filename)
     x = questionaire(questions)
     print("score : " , correctionSimple(x))
     
     
     print("Le questionnaire est une liste de questions.")
     for q in range(len(questions)):
         print("\tQuestion " + str(q+1) + ": \"" + questions[q][0] + "\"")
         ver = []
         for v in range(len(questions[q][1])):
             ver.append(False)
         for r in range(len(questions[q][1])+1):
             rep = rand.randint(0,len(questions)-1)
             if ver[rep-1] == False:
                 ver[rep-1] = True 
                 print("\t\tReponses " + str(rep) + ":")
                 print("\t\t\tMessage: \"" + questions[q][1][rep][0] + "\"")
                 print("\t\t\tCorrect: " + str(questions[q][1][rep][1]))
                 print("\t\t\tFeedback: \"" + questions[q][1][rep][2] + "\"")