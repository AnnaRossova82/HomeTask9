class Car (object):
    """Describes car characteristics and functions"""
    def __init__(self, brand, color, engine):
        self.brand = brand
        self.color = color
        self._engine = engine
    def move_directly (self):
        print (f"{self.brand} moves directly")
    def move_back (self):
        print (f"{self.brand} moves back")

class Car2 (Car):
    def __init__ (self, brand, color, engine):
        Car.__init__ (self, brand, color, engine)
    def turn_right (self):
        print(f"{self.brand} turns right")
    def turn_left (self):
        print(f"{self.brand} turns left")

desc = Car ("Ford", "white", 3)
desc2 = Car2 ("Audi", "Red", 4)
print (desc.color)
print (desc.move_back())
print (desc2.turn_left())
print (desc2.move_directly())


class Parallelogram (object):
    def __init__ (self, width, length):
        self.width = width
        self.length = length
    def get_area (self, width = 0, length = 0):
        print ("Get area of parallelogram")
        return self.width * self.length

par = Parallelogram (4, 7)
print (par.get_area())

class Square (Parallelogram):
    def get_area (self, width = 0, length = 0):
        print ("Get area of square")
        return self.width * self.width

par2 = Square (9, 9)
print (par2.get_area ())

class TextProcessor ():
    def __init__ (self, char):
        self.char = char()

    def get_clean_string (self, char):
        self.char = char()
        import string
        return char.translate(str.maketrans('', '', string.punctuation))
        return char.translate
        print(char.translate)
char = TextProcessor(', . " ! ? : ; *')
res = TextProcessor.char.translate
@property
def res(self):
    return self._res
res = char.translate()
print("Already cleaned text is printed:", res.get_clean_string)

def _is_punktiantian (self, char, symb):
    self.char = char()
    self.symb = symb()
    for i in self.char:
        if i in self.symb:
            print (i, "=", True)
            _true_list.append (i)
        else:
            print (i, "=", False)
            _false_list.append (i)
        return self.char in self.symb

symb = {'yehw?!hfje:"jdjdk'}
char = TextProcessor.char.self
_true_list = []
_false_list = []

class TextLoader (TextProcessor):
    def __init__ (self, clean_string):
        self._clean_string = None

    def set_clean_text (self, text_processor):
        self.__text_processor = text_processor
TextLoader._clean_string = TextProcessor.res
print (TextLoader._clean_string)

@_clean_string.setter
def get_clean_string(self, clean_string):
    self_clean_string = clean_string

@property
def res(self):
    return self._res
res = TextLoader.clean_string()
print ("Already clean text is printed")


class Datainterface (TextLoader):
    def __init__ (self, _clean_string):
        self._clean_string = None
print (__TextLoader.__clean_string)


@_clean_string.getter
def get_clean_string(self, clean_string):
    self._clean_string = clean_string

    def process_texts():
        list_of_lines = input()
        for line in list_of_lines:
        line.append {"some appended text"}
print (Datainterface.list_of_lines)






