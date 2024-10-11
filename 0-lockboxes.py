#!/usr/bin/python3
def canUnlockAll(boxes):
    """
    Determines if all boxes can be opened.
    
    Args:
        boxes: A list of lists, where each sublist contains the keys to other boxes.
    
    Returns:
        True if all boxes can be opened, False otherwise.
    """
    n = len(boxes)
    unlocked = [False] * n  # Keep track of unlocked boxes
    unlocked[0] = True  # Box 0 is initially unlocked
    keys = [0]  # Start with the keys from box 0
    
    while keys:
        current_box = keys.pop()  # Get the next box to explore
        
        for key in boxes[current_box]:
            if key < n and not unlocked[key]:
                unlocked[key] = True  # Unlock the box
                keys.append(key)  # Add the keys from the newly unlocked box
    
    # Check if all boxes are unlocked
    return all(unlocked)
