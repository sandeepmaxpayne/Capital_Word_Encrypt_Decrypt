import math

class Short_Message:
    def __init__(self, message):
        self.message = message
    def encrypt_single_msg(self):
        if int(ord(self.message)).__eq__(90):
            self.message = chr(65)
        else:
            self.message = chr(ord(self.message) + 1)
        return self.message


def encryptStr():
    msg = input('enter message: ').upper()
    x = msg.split()
    as_num = ""
    for j in x[0]:
    #    print(ord(j))
        as_num += str(ord(j))
   # print(as_num)
    b = int(as_num)
    c = 0
    b1 = b
    s = ""
    bb1 = 0


    while round(b1) > 127:

        r = b1 % 127
        s = s + str(round(r))

        c += 1
    #    print(r, c, b1, s)
        bb1 = b1

        b1 = b1 / 127

    # print(4761.5270010540025 * 127)
    # print(604713.9291338583*127)

# Use the last num 125.05380663545695 as encrypt, think other than doc

    #print(r, c, bb1, s)
    strbb1 = str(bb1)
    strbb1 = strbb1.split(".")
    #print(strbb1)
    # add the counter at end of index0
    strbb1[0] += str(c)
    #print(strbb1)

    enc1, enc2 = "", ""

    for k in (strbb1[0][:-1]):
        #print(k)
        #print(chr(65+int(k)))
        enc1 += chr(65+int(k))
   # print(enc1)

    enc1 += str(c)
   # print(enc1)

   # print("----",strbb1)
    if len(strbb1) > 1:
        for k in strbb1[1]:
            enc2 += chr(90 - int(k))
   # print(enc2)

    # append the after decimal string in a reverse order

    if len(msg).__eq__(1):
        shortMsg = Short_Message(msg)
        enc = shortMsg.encrypt_single_msg()
        print("encrypted text: ", enc)

    else:

        enc = enc1 + enc2[::-1]
        print("encrypted text: ", enc)

    ## symmetric key of 1st second array value using xor operation
    key = 0
    for i in strbb1:
        key ^= int(i)
    print("secret key: ", key)





encryptStr()