class Book():

    def __init__(self,author,title,description,pages):
        self.author=author
        self.title=title
        self.description = description
        self.pages = pages


    def __str__(self):
        return "title :{},author: {}, description: {},pages : {}".format(self.title,self.author,self.description,self.pages)

    def __len__(self):
        return self.Book

    def __len__(self):
        return self.Book

x = Book("alsaheem","theMan","a great man",500)
print(x)













# class Animal():
#
#     def __init__ (self):
#         print("Animal Creatd successfully")
#
#     def whatami(self):
#         print("i am an Animal")
#
#     def canieat(self):
#         print("this Animal can Eat")
#
#
# class Dog(Animal):
#
#     def __init__ (self):
#         # Animal.__init__(self)
#         print("dog created")
#
#     def dogbark(self):
#         print("woofaoof")
#
# x=Animal()
# x.whatami()
