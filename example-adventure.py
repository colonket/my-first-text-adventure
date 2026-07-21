'''
Eric's Example Adventure

This is an example that shows one way the text adventure engine
can be used.

In this example, we use the 'title' field to show each scene's location.
We point to the same 'answer_phone' scene through different branches.
We use a single choice '...' as a way to pace the player through connecting
scenes without branches.

To run:
python example-adventure.py
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
            #print(choice_nums[user_input]['goto'])
            show(story[choice_nums[user_input]['goto']])
        except ValueError:
            print()
            print(f"Invalid choice. Please pick a number between 1 and {len(scene['choices'])}.")
            continue
        except KeyError as e:
            print(f"[ERROR] Scene {e} not found.")
            continue

# Edit the 'story' dictionary below to create your own text adventure!
story = {
    'start': {
        'title': 'Office',
        'desc': '''
    You are sitting in a office, when suddenly, the phone rings.
        ''',
        'choices': [
            {'text':'Pick up the phone',
             'goto':'answer_phone'},
            {'text':'Ignore the phone',
             'goto':'ignore_phone'},
            {'text':'Throw the phone against the wall',
             'goto':'throw_phone'},
        ],
    },
    'answer_phone': {
        'title': 'Office',
        'desc': '''
    You pick up the phone. 
    ???: "Hi, how are ya?"
        ''',
        'choices': [
            {'text':'"Who is this?"',
             'goto':'answer_phone_2'},
            {'text':'Hang up.',
             'goto':'hangup_phone'},
        ],
    },
    'ignore_phone': {
        'title': 'Office',
        'desc': '''
    The phone continues to ring.
        ''',
        'choices': [
            {'text':'Give in and answer the phone.',
             'goto':'answer_phone'},
            {'text':'Throw the phone.',
             'goto':'throw_phone'},
        ],
    },
    'throw_phone': {
        'title': 'Office',
        'desc': '''
    You chuck the phone at the wall.
    There is a now a phone-shaped hole in the wall.
    You hear the ringing gradually fade into the distance.
        ''',
        'choices': [
            {'text':'...',
             'goto':''},
        ],
    },
}

if __name__ == '__main__':
    main()
