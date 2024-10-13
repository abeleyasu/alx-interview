#!/usr/bin/python3
"""
Module to determine if all boxes can be opened.
"""

def canUnlockAll(boxes):
    """
    Determines if all boxes can be opened.

    Args:
        boxes (list): A list of lists where each list represents
                      the keys in that box.

    Returns:
        bool: True if all boxes can be opened, False otherwise.
    """
    n = len(boxes)
    opened = [False] * n  # Track which boxes are opened
    opened[0] = True  # The first box is already unlocked
    keys = boxes[0]  # Start with the keys in the first box

    while keys:
        key = keys.pop()  # Get the next key
        if not opened[key]:  # If this box is not opened yet
            opened[key] = True  # Mark the box as opened
            keys.extend(boxes[key])  # Add its keys to the keys list

    return all(opened)  # Check if all boxes are opened
