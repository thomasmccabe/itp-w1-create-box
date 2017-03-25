"""This is the entry point of the program."""


def create_box(height, width, character):
    
    if height <= 1:
        return "invalid height"
    if width <= 1:
        return "invalid width"
    i = 0
    answer = ''
    
    for x in range(height): # range(5) = (0,1,2,3,4)
        while i < width: # answer += (character * width)
            i += 1
            answer += (character)
        answer += '\n'
        i = 0

    return answer
        
def create_external_box(height, width, character):
    i = 1
    answer = ''
    x = 1
    while x < height:
        if x == 1 or x == height:
            answer += character * width
            answer += '\n'
        answer += character
        i += 1
        answer += (' ' * (height - 2) ) # for a perfect box, (' ' * height) for a misaligned box
        answer += character
        answer += '\n'
        x += 1
        if x == height:
          answer += character * width
    print answer
    
""" 
########
heightLine = ''
i = 0
while i < height:
    heightLine += character
    i += 1

########
widthLine = '' 
i = 0
while i < width:
    widthLine = ''
    i += 1
"""

if __name__ == '__main__':
    create_box(3, 4, '*')

'''
i = 0
answer = ''
while i < height: 
    i += 1
    answer += (character * width)
    answer += ('\n')
return answer
'''