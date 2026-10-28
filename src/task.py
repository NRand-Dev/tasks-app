class Task:
# Basic Data container for Task Objects

# Summary of task
title: str = ""
# Long form details of task
description: str = ""
## Flag if task is completed or not
completed: bool = False


### DO I NEED THIS INITALIZER???
def __init__(self):
    self.title = title
    self.description = description
    self.completed = completed


def _set_title(text: str):
    if text:
        title = text
    else:
        print('ERROR: No text passed to _set_title function')


def toggle_completed():
    if completed:
        completed = False
    else:
        completed = True
