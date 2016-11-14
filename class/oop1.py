#Here's how you define the blueprint for your new Bookcase objects
class Bookcase(object):
    def __init__(self, w, h):
        print "Making a new bookcase..."
        self.width = w
        self.height = h
        self.upright = False

    def fall(self):
        print "The bookcase falls over"
        self.upright = False

    def right(self):
        print "You put the bookcase upright"
        self.upright = True



#Here's how you make a new bookcase instance
myBookcase = Bookcase(10, 200)

#Using the dot operator, you can access methods and variables of the objects
myBookcase.fall()
myBookcase.right()

print myBookcase.width, myBookcase.height, myBookcase.upright
print "My Bookcase is %d x %d cm" % (myBookcase.width, myBookcase.height)
