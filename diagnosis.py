import sys

def input_to_dict(filename):
    dict = {}
    with open(filename) as f:
        line_num = 0
        disease_name = ""
        for line in f:
            if line_num % 2 == 0:
                disease_name = line
            else:
                symptoms = set(line.split(", "))
                dict.update({disease_name:symptoms})
    return dict

def ask_for_symptoms(filename):
    symptoms = []
    with open(filename) as f:
        for line in f:
            answer = input("Are you experiencing %s? (Y/N)" % line)
            valid_answer = False
            while(valid_answer):
                if answer.lower() == "y":
                    valid_answer = True
                    symptoms.append(answer)
                elif answer.lower() == "n":
                    valid_answer = True
                else:
                    answer = input("Invalid input. Please answer 'y' or 'n' to the above question.")
    return symptoms

def match_to_diseases(symptoms_experienced, dd):
    diseases = []
    for dis in dd:
        count = 0
        disease_symptoms  = dd[dis] #set
        for symp in symptoms_experienced:
            if symp in disease_symptoms:
                count += 1
        if count > 3:
            diseases.append(dis)
    return diseases

disease_dict = input_to_dict("input.txt")
symptoms = ask_for_symptoms("symptoms.txt")
possible_diagnoses = match_to_diseases(symptoms, disease_dict)
print("You could be experiencing one of the following diseases:")
for disease in possible_diagnoses:
    print(disease)