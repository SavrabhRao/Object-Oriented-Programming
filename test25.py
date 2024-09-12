""" parul university """
    # parul institute of tecnology
    # pias
    # pim
    ############################### Composition

# teacher can exist without parul university so 
# its composition
################################### Aggregation

''' composition and aggregation are type of - has a relation - '''


# composition
# composition means one class is totally dependent on another one without existance 
# of another one class there is no existance of another class that is called as composition
# university has a collage

class library:
    def __init__(self,books):
        self.books = []

class book:
    def __init__(self,bookname):
        self.book = bookname

# aggregation 
# there is no strong reltion between two classes this relation is called as aggregation
# like one class can exist without another class as given above 
# library has a books

