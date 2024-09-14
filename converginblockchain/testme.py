# Untested!

class Disease:
     def __init__(self, name, symptoms):
         self.name = name
         self.symptoms = symptoms


known_diseases = [
   Disease('cold', set("sore throat|runny nose|congestion|cough|aches".split("|"))),
   Disease('flu', set("fever|headache|muscle aches|returning fever".split("|"))),
   Disease('ebola', set("tiredness|death|bruising over 90% of body|black blood".split("|"))),
   Disease('spondylosis', set("Tingling|numbness|weakness|Abnormal reflexes|muscle spasms".split("|"))),
   Disease('alcohol misuse', set("antisocial behaviour|impulsivity|self-harm|loneliness".split("|"))),
   Disease('stroke', set("Numbness|arm|Confusion|Difficulty speaking|difficulty walking|slurred speech".split("|"))),
   Disease('Lower respiratory infections', set("phlegm|fever|difficulty breathing|a blue tint to the skin|chest pain|wheezing".split("|"))),
   Disease('pulmonary', set("dyspnea|Fatigue|fainting spells|Chest pressure|Swelling".split("|"))),
   Disease('bronchus', set("Cough with blood|Wheezing|Shortness of breath|Chest pain|Flushing".split("|"))),
   Disease('Diabetes', set("thirst and hunger|urination|Weight loss or gain|Fatigue|Nausea|Blurred vision".split("|"))),
   Disease('Alzheimer', set("Memory loss|Vision loss|Misplacing items|Difficulty making decisions|meaningless repetition ".split("|"))),
   Disease('Dehydration', set("vomiting|sweating|Individuals |dry mouth|lethargy|dizziness".split("|"))),
   Disease('Tuberculosis', set("Coughing|Chest pain|weight loss|Fatigue|Fever|Night sweats|Chills".split("|"))),
   Disease('Cirrhosis', set("jaundice|Weakness|Loss of appetite|Itching|Easy bruising|dark urine".split("|"))),
   Disease('Plague', set("diarrhoea|nausea|nausea|malaise|delirium|shortness of breath|tender lymph node".split("|"))),
   
   ]


# note: for Python 2, use "raw_input" instead of input
symptoms = input("Please enter symptoms separated by commas: ")
symptoms = symptoms.lower()
symptoms = symptoms.split(",")

possible = []
for symptom in symptoms:
     for disease in known_diseases:
         if symptom in disease.symptoms:
             possible.append(disease.name)

if possible:
     print("You may have these diseases:")
     print(*possible)
else:
     print("Good news! You're going to have a disease named after you!")

