# Encypt and Decrypt Capital Words using Logical Number System [COLLEGE Final Year PROJECT]

<b><ul>This is a simple encryption and decrption algorithm for Capital or Lower Case alphabetic Characters</ul></b>

To run :
    For Encrypting the character

    use the command as "python encryptText.py" in command prompt

    For Decrypting the encrypted character

    use the command as "python decryptText.py" in command prompt

# Limitations



# Algorithm Explanation

Performing the XOR operation for particular data word at the time of encryption. 
Suppose text: Monster , the value got as ['23546', '7737144224366’].
Then we perform XOR operation between the both the values to get the secret key.
This secret key is required at the time of decryption along with the encrypted text in order to verify , whether the secret key is the correct value for that particular encryption or not.
If the secret key entered is correct we get the decoded word otherwise error will be thrown regarding the secret key. 

For single based alphabetic character, encryption is done simple just by using the next character value.
For example character ‘A’ is converted to ‘B’, ‘C’ is converted to ‘D’  and so on and so forth.
The decrypting of single character is similar to that of encrypting the single character. Just we are reversing the process that what we have done in case of encrypting.

<b>Encrypting</b>:  
<li>
Z => A,
X => W
Till
B => A
</li>


Decrypting:
A => B,
B => C
Till
Z => A

The decryption process will be the reverse procedure of encrypted one. But in reality it should be more complicated otherwise its can easily be cracked.

<i>Suppose</i>:
Encrypted text = “HJ6UUZ”
Split the values and then extract the decimal value from it.
Then we will convert this into 127 bit number system.
Finally we will get  the desired integer value that was taken at the time of encryption and from that we will get the original value.

<h3>Limitation </h3>
This project is limited only to words and not to sentence.

<h2>License</h2>

<p>The project is released under <a href="https://github.com/sandeepmaxpayne/Capital_Word_Encrypt_Decrypt/blob/master/LICENSE">MIT License</a></p>

<h2> To test this with n number of words test.py is written for that </h2>
<p>Test the code<a>href="https://github.com/sandeepmaxpayne/Capital_Word_Encrypt_Decrypt/blob/master/test.py"</a></p>

