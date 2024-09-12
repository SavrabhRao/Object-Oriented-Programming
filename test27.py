class outer:
    def __init__(self):
        print("outer class")
        self.innd = self.inner().innerinner()
    class inner:
        def __init__(self):
            print("inner")
        class innerinner:
            def __init__(self):
                print("inner inner")
            def method(self):
                print("method of innerinner")

out = outer()
inn = out.inner()
inin = inn.innerinner()  
inin.method()
out.innd

# to execute any inner class we required the object of its outer class