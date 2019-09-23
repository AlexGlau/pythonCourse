answers = {
    'How are you?': 'Good',
    'What are you doing?': 'I am coding',
    'Do you want to eat?': 'No, thanks!',
    'Do you know where is your wife now?': 'What?!!'
}

def ask_user():
    while True:
        try:
            user_say = input('Enter your message:\n')
            if user_say in answers:
                program_answer = answers[user_say]
                print(f'- Program: {program_answer}')
            elif (user_say == 'Thanks, that`s all!'):
                print('Finally!')
                break
            else:
                print('Incorrect message.')
        except KeyboardInterrupt:
            print("Interrupted by keyboard.")
            break

ask_user()
