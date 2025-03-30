import genanki
import pdfplumber

#file = open("test.rtf")
#content = file.read()
#print(content)


#def ExtractQuestionAnswer():
#    with pdfplumber.open('test.pdf') as pdf:
#        for page in range(0, len(pdf.pages)):
#            text = pdf.pages[page]
#            question_text = text.filter(lambda obj: obj["object_type"] == "char" and "Bold" in obj["fontname"])
#            answer_text = 
#            print(question_text.extract_text())
my_deck = genanki.Deck(
        2059400110,
        'Test Deck ahHAH')


#ExtractQuestionAnswer()

def MakeQuestions(question, answer):
    model = genanki.Model(
    1607392319,
    'Test Model',
    fields=[
        {'name': 'testQuestion'},
        {'name': 'testAnswer'},
    ],
    templates=[
    {
      'name': 'Card 1',
      'qfmt': '{{testQuestion}}',
      'afmt': '{{FrontSide}}<hr id="answer">{{testAnswer}}',
    },
  ])

    my_note = genanki.Note(
        model=model,
        fields=[question, answer])

    # my_deck = genanki.Deck(
    #     2059400110,
    #     'Test Deck ahHAH')

    my_deck.add_note(my_note)

def ExtractQuestionAnswer():
    questions = []
    answers = []
    
    with pdfplumber.open("test.pdf") as pdf:
        for page in pdf.pages:
            question = ""
            answer = ""
            in_question = False  # Track whether we're in a question
            
            for obj in page.extract_words(extra_attrs=["fontname"]):
                if "Bold" in obj["fontname"]:  # Identifying bold text
                    if in_question:  # If already in a question, append
                        question += " " + obj["text"]
                    else:
                        if question and answer:  # Store previous Q&A
                            questions.append(question.strip())
                            answers.append(answer.strip())
                        question = obj["text"]  # Start new question
                        answer = ""
                        in_question = True
                else:
                    answer += " " + obj["text"]
                    in_question = False
            
            # Store last question-answer pair
            if question and answer:
                questions.append(question.strip())
                answers.append(answer.strip())

    for q, a in zip(questions, answers):
        MakeQuestions(q, a)

    genanki.Package(my_deck).write_to_file('output.apkg')

ExtractQuestionAnswer()