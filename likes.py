#!/usr/bin/python

def main():
    '''
    You probably know the "like" system from Facebook and other pages. 
    People can "like" blog posts, pictures or other items. 
    We want to create the text that should be displayed next to such an item.

    Implement a function likes :: [String] -> String, which must take in input array, 
    containing the names of people who like an item. It must return the display text as shown in the examples:

    likes [] // must be "no one likes this"
    likes ["Peter"] // must be "Peter likes this"
    likes ["Jacob", "Alex"] // must be "Jacob and Alex like this"
    likes ["Max", "John", "Mark"] // must be "Max, John and Mark like this"
    likes ["Alex", "Jacob", "Mark", "Max"] // must be "Alex, Jacob and 2 others like this"
    '''

    names = []
    print (likes(names))

    names = ["Peter"]
    print (likes(names))

    names = ["Jacob", "Alex"]
    print (likes(names))

    names = ["Max", "John", "Mark"]
    print (likes(names))

    names = ["Alex", "Jacob", "Mark", "Max"]
    print likes(names)

def likes(names):
    if not names:
        return "no one likes this"
    else:
        size = len(names)
        if size == 1:
            return "%s likes this" % names[0]
        elif size == 2:
            return "%s and %s like this" % (names[0], names[1])
        elif size == 3:
            return "%s, %s and %s like this" % (names[0], names[1], names[2])
        else:
            return "%s, %s and %d others like this" % (names[0], names[1], size-2)


if __name__ == "__main__":
    main()
