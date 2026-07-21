# My First Text Adventure

A Python script for creating a text adventure game aimed at introducing people who are new to Python. 

To create your own adventure, you can modify the `story` dictionary as shown below:

```python
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
```

To run the adventure:

```bash
python text-adventure.py
```
