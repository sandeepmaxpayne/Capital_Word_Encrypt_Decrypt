class Number:
    def __init__(self, input):
        self.input = input
        self.__num_ascii = []
    def encrypt_number(self):
        for i in self.input:
            self.__num_ascii.append(str(ord(i)))
        return "".join(self.__num_ascii)

''' list of generated ascii from 0 to 9 are [48, 49, 50, 51, 52, 53, 54, 55, 56, 57]
    So concatenate  all the generated values in order to get our concatenated list
'''

'''
'''