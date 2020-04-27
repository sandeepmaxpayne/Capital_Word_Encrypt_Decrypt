''' All the important commments on solving out this problem is made using this comments'''

'''Reprsentaation of ascii value order from 100 to 122
    1 => 10
    2 => 11
    3 => 12

    # From 97 to 99 make no change 
    # Reason: To make simpler for calculation convert all ASCII values only upto 2 digits only
 '''
class Small_Letter:
    def __init__(self, message):
        self.message = message
        self.__conv_list = []
        self.__conv_and_concat = []
    def encrypt_small_message(self):
        msg = self.message
        for i in msg:
            conv = ord(i)
            self.__conv_list.append(conv)
      #  print(self.__conv_list)
        for i in self.__conv_list:
            if len(str(i)).__eq__(3):
                x = str(i)
                ''' take the first two number one side and last two number other side '''
                x_first_two_dig = x[:2]
                x_last_dig = x[-1]
       #         print(x_first_two_dig, x_last_dig)
                ''' get the sum of first two number '''
                x_fdig_sum = sum([int(j) for j in x_first_two_dig])
        #        print(x_fdig_sum)
                '''concate the x_fdig_sum with the x_last_dig'''
                concat_x = str(x_fdig_sum) + x_last_dig
         #       print(f'concated 3 digit to 2 digit: {concat_x}')

                self.__conv_and_concat.append(concat_x)

            else:
                self.__conv_and_concat.append(str(i))
        '''finally concat it and add a special code to identify that its for the actual small letters'''
        # print(__conv_and_concat)
        # print(f'concated format: {"".join(__conv_and_concat)}')
       
      
        return "".join(self.__conv_and_concat)
        