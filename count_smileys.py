#!/usr/bin/python

def main():
    '''
    Given an array (arr) as an argument complete the function countSmileys that should return the total number of smiling faces.
    Rules for a smiling face:
        -Each smiley face must contain a valid pair of eyes. Eyes can be marked as : or ;
        -A smiley face can have a nose but it does not have to. Valid characters for a nose are - or ~
        -Every smiling face must have a smiling mouth that should be marked with either ) or D.
    No additional characters are allowed except for those mentioned.
    Valid smiley face examples:
        :) :D ;-D :~)
    Invalid smiley faces:
        ;( :> :} :] 
    '''

    arr = [':D',':~)',';~D',':)']
    print (count_smileys(arr))

def count_smileys(arr):
    import re
    count = 0
    for smile in arr:
        if re.match('(:|;)(-|~)*(\)|D)', smile):
            count += 1
    return count

if __name__ == "__main__":
    main()
