import genanki
import pdfplumber

#file = open("test.rtf")
#content = file.read()
#print(content)

deckName = ""

#def ExtractQuestionAnswer():
#    with pdfplumber.open('test.pdf') as pdf:
#        for page in range(0, len(pdf.pages)):
#            text = pdf.pages[page]
#            question_text = text.filter(lambda obj: obj["object_type"] == "char" and "Bold" in obj["fontname"])
#            answer_text = 
#            print(question_text.extract_text())

def GenerateCards(pathToFile, choosenDeckName):
    deckName = choosenDeckName
    ExtractQuestionAnswer(pathToFile)



my_deck = genanki.Deck(
        2059400110,
        deckName)


#ExtractQuestionAnswer()

def MakeQuestions(question, answer):
    model = genanki.Model(
    1607392319,
    'Model',
    fields=[
        {'name': 'Question'},
        {'name': 'Answer'},
    ],
    templates=[
    {
      'name': 'Quiz Question',
      'qfmt': '{{Question}}',
      'afmt': '{{FrontSide}}<hr id="answer">{{Answer}}',
    },
  ])

    my_note = genanki.Note(
        model=model,
        fields=[question, answer])

    # my_deck = genanki.Deck(
    #     2059400110,
    #     'Test Deck ahHAH')

    my_deck.add_note(my_note)

def ExtractQuestionAnswer(pathToFile):
    questions = []
    answers = []
    
    with pdfplumber.open(pathToFile) as pdf:
        for page in pdf.pages:
            question = ""
            answer = ""
            in_question = False 
            
            for obj in page.extract_words(extra_attrs=["fontname"]):
                if "Bold" in obj["fontname"]:  
                    if in_question:  
                        question += " " + obj["text"]
                    else:
                        if question and answer:  
                            questions.append(question.strip())
                            answers.append(answer.strip())
                        question = obj["text"]  
                        answer = ""
                        in_question = True
                else:
                    answer += " " + obj["text"]
                    in_question = False
            
            
            if question and answer:
                questions.append(question.strip())
                answers.append(answer.strip())

    for q, a in zip(questions, answers):
        MakeQuestions(q, a)

    genanki.Package(my_deck).write_to_file('output.apkg')

#ExtractQuestionAnswer()