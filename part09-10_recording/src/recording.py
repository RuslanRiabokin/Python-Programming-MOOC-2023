class Recording:
    def __init__(self, length):
        if length < 0:
            raise ValueError("Length of recording cannot be negative")
        self.__length = length

    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self, value):
        if value < 0:
            raise ValueError("Length of recording cannot be negative")
        self.__length = value