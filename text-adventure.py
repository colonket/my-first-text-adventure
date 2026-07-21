'''
Eric's Simple Text Adventure Engine

Edit the 'story' dictionary below to create your own adventure.

To run:
python text-adventure.py
'''

def main():
    '''
    Show the first scene, then proceed from there...
    '''
    first_scene = story['start']
    show(first_scene)

def show(scene):
    '''
    This is how each scene is shown
    '''
    print('='*30)
    print(scene['title'])
    print('-'*30)
    print(scene['desc'])
    print()
    choice_nums = {}
    for i, c in enumerate(scene['choices'],1):
        print(f'[{i}] {c['text']}')
        choice_nums[str(i)] = c

    while True:
        print()
        print("Enter the number of your choice, or enter 'QUIT' to quit:")
        user_input = input('> ')

        if user_input == 'QUIT':
            print("Goodbye.")
            exit()

        try:
            print(choice_nums[user_input]['goto'])
        except:
            print()
            print(f"Invalid choice. Please pick a number between 1 and {len(scene['choices'])}.")
            continue

# Edit the 'story' dictionary below to create your own text adventure!
story = {
    'start': {
        'title': 'The Beginning',
        'desc': '''
    You find yourself a room.
        ''',
        'choices': [
            {'text':'Enter the bathroom',
             'goto':'branch_a'},
            {'text':'Sit on the couch',
             'goto':'branch_b'},
            {'text':'Do a silly dance',
             'goto':'branch_c'},
        ],
    },
    'branch_a': {
        'title': '',
        'desc': '''

        ''',
        'choices': [
            {'text':'',
             'goto':''},
            {'text':'',
             'goto':''},
            {'text':'',
             'goto':''},
        ],
    },
    'branch_b': {
        'title': '',
        'desc': '''

        ''',
        'choices': [
            {'text':'',
             'goto':''},
            {'text':'',
             'goto':''},
            {'text':'',
             'goto':''},
        ],
    },
    'branch_c': {
        'title': '',
        'desc': '''

        ''',
        'choices': [
            {'text':'',
             'goto':''},
            {'text':'',
             'goto':''},
            {'text':'',
             'goto':''},
        ],
    },
}

if __name__ == '__main__':
    main()
