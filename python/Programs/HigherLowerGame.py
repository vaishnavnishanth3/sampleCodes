from random import randint
import os
score = 0

quiz = {
    'Bruna Marquezine': {
                    'Job': 'Artist',
                    'Country': 'Brazil',
                    'Followers': 45100000
                },
    'Zendaya': {
                    'Job': 'Artist and Model',
                    'Country' : 'USA',
                    'Followers': 184000000
                },
    'Naomi Watts':{
                    'Job': 'Artist and Producer',
                    'Country': 'England',
                    'Followers': 1900000
                },
    'Sadie Sink':{
                    'Job': 'Artist',
                    'Country': 'USA',
                    'Followers': 26000000 
                },
    'Heilee Steinfield':{
                    'Job': 'Artist, Singer and Video Creator',
                    'Country': 'USA',
                    'Followers': 20800000
                },
    'Madison Beer':{
                    'Job': 'Artist, Singer and Producer',
                    'Country': 'USA',
                    'Followers': 37800000
                },
    'Emilia Clarke':{
                    'Job': 'Artist',
                    'Country': 'England',
                    'Followers': 28200000
                },
    'Gwyneth Paltrow':{
                    'Job': 'Artist and Writer',
                    'Country':'USA',
                    'Followers': 8300000
                },
    'Millie Bobby Brown':{
                    'Job':'Artist and Model',
                    'Country': 'England',
                    'Followers': 62900000
                },
    'Jennifer Aniston':{
                    'Job': 'Artist, Producer and Director',
                    'Country': 'USA',
                    'Followers' : 45300000
                }
}

celebName = ['Bruna Marquezine','Zendaya','Naomi Watts','Sadie Sink','Heilee Steinfield','Madison Beer','Emilia Clarke','Gwyneth Paltrow','Millie Bobby Brown','Jennifer Aniston']

def playGame(score):
    print(f"\nScore = {score}")
    randomNumber1 = randint(0,9)
    randomNumber2 = randint(0,9)

    while randomNumber2 == randomNumber1:
        randomNumber2 = randint(0,10)

    chosenCelebrity1 = celebName[randomNumber1]
    chosenCelebrity2 = celebName[randomNumber2]
    print(f"\n[Higher / Lower]\nCompare Followers of \n\nA: {chosenCelebrity1}, an {quiz.get(chosenCelebrity1).get('Job')} from {quiz.get(chosenCelebrity1).get('Country')}\n\n           VS\n\nB: {chosenCelebrity2}, an {quiz.get(chosenCelebrity2).get('Job')} from {quiz.get(chosenCelebrity2).get('Country')}")
    
    match(quiz.get(chosenCelebrity2).get('Followers') > quiz.get(chosenCelebrity1).get('Followers')):
        case True:
            answer = "Higher"
        case False:
            answer = "Lower"
    
    option = input("\nHigher / Lower? type 'Higher' or 'Lower': ")
    os.system('cls')
    
    match(option.capitalize() == answer):
        case True:
            score += 1
            playGame(score)
        case False:
            print(f"You Lost and Your Score is {score}")   

playGame(score)
