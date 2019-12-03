# mr Miyagi trainee ##projct

# Ask for user input and depending on the response, mr Miyagi will respond.
#
# prompt user for input
# Evaluate each input and print the appropriate responses
# Follow these rules:
#
# every time you ask a question --> Mr. Miyagi responde with
    # --> 'questions are wise, but for now. Wax on, and Wax off!'
# every statement/question must start with Sensei, otherwise:
    # --> 'You are smart, but not wise - address me as Sensei please'
# every time you mention 'block' or 'blocking' --> Mr. Miyagi responde with
    # --> 'Remeber, best block, not to be there..'
# anything else you say:
    # --> 'do not lose focus. Wax on. Wax off.'


# Make it so you keep playing until we say: 'Sensei, I am at peace'
    # --> 'Sometimes, what heart know, head forget'
def mizaki_game():
    print("Welcome to Mr.Miyagi's class!")
    your_response = input('(MR.Miyagi)... -.-')
    number_tries = list(range(0,9,1))
    for i in number_tries:
        if 'Sensei' not  in your_response:
            print('You are smart, but not wise - address me as Sensei please')
            your_response = input('(MR.Miyagi)... -.-')
            continue
        elif '?' in your_response:
            print('questions are wise, but for now. Wax on, and Wax off!')
            your_response = input('(MR.Miyagi)... -.-')
            continue
        elif 'block' in your_response or 'blocking' in your_response:
            print('Remember, best block, not to be there..')
            your_response = input('(MR.Miyagi)... -.-')
            continue
        elif 'Sensei,peace' in your_response:
            print('You have finished training !')
            break
        else:
            print('do not lose focus. Wax on. Wax off.')
            your_response = input('(MR.Miyagi)... -.-')
            continue