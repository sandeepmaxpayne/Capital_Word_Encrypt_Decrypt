# Implementation of Information Security by Use of Logic Operations and Number System [COLLEGE Final Year PROJECT]

<b><ul>This is a simple encryption and decrption algorithm for Capital or Lower Case alphabetic Characters</ul></b>

To run :
    For Encrypting the character

    use the command as "python encryptText.py" in command prompt

    For Decrypting the encrypted character

    use the command as "python decryptText.py" in command prompt
    
# NEW desktop application made as an UI interaction for this whole project .
        -> Files includes app.py

# Limitations

    ```
    Only Capitals Words, or ,
    Only Small Words, or ,
    Only Numbers, or ,
    Must be a combination of capital word, small word and numbers
    For secret key get the individual secret key for the encrypted capitals, smalls, numbers 
    For the combination of capital, small and number first get each of their individual sceret key
    and finally the xor each of the individual keys
    Length of word should be 3 or greater. [Due to 127 number system the ascii value generated must be greater than 127 and is only achieved by the word of length 3 and more]```

# Algorithm Explanation

Performing the XOR operation for particular data word at the time of encryption. 
Suppose text: Monster , the value got as ['23546', '7737144224366’].
Then we perform XOR operation between the both the values to get the secret key.
This secret key is required at the time of decryption along with the encrypted text in order to verify , whether the secret key is the correct value for that particular encryption or not.
If the secret key entered is correct we get the decoded word otherwise error will be thrown regarding the secret key. 

``` TODO this is depricated due to ahead comlexity issues and is more challenging to solve because the minimum length of the encrypted word must be 3 or more other base(127) number system can't be used because the ascii length obtained is less than 127 and can't be divided using 127. 

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
```

<h2>For Encrypting the Small letters alphabets</h2>
<br>
<p>The ascii value for small alphabets is between 97 to 122 so a proper mapping of the ascii digits is required in order to get the ascii number divisible by 127 and get the accurate encrypted text and is also required same for decrypting it well as same</p>
<br>
```Reprsentaation of ascii value order from 100 to 122

    1 => 10
    
    2 => 11
    
    3 => 12
    
    # From 97 to 99 make no change 
    
    # Reason: To make simpler for calculation convert all ASCII values only upto 2 digits only
 ```
 <br>

 <h2>Encrypting the Digits </h2>
<br>
```
<p>The digits have their ascii range from <b>48</b> to <b>87</b> and the digits are from <b>0</b> to <b>9</b></p>
<br>
```
<p>Assumption : Ascii value 78</p>
<br>
```
<p>Main Assumption for this value 78 is that , the main objecive is to encrypt using some logical numbers. So Idea is to convert the Digits ascii to capital letters ascii such that
    65'<('ASCII(DIGIT)[0] + 78', 'ASCII(DIGIT)[1] + 78')<'90
</p> 
For the number encryption
            1. Reverse the acii value of the number
            2. N => Acii is 78
            3. So add each ascii value unit with 78 to generate capital letter in encrypted format  

```

The decryption process will be the reverse procedure of encrypted one. But in reality it should be more complicated otherwise its can easily be cracked.

# Decryption Process Explanation

<h2>For decrypting the number</h2>
<br>
```
<p>For ecrypting the number I used default ascii 78 so for decrypting it here I'll need the same value</p>
```
<br>

<h2>For Decrypting Small letters</h2>
<br>
```
<p>For decrypting small letters Logic is only for position 0 for each number generated and replace the 0th position with
    1 => 10
    2 => 11
    3 => 12
    For example if the number obtained is <b>10</b> then replace the first index with the above mapping and here in this example <b>1</b> => <b>10</b>
    So 10 become 100 and that reperesnts the ASCII for <b>d</b>
    Done in decrypt_ascii[]</p>
```
<br>

<h2>Decrypting the Capital letters</h2>
<br>

<p>Here in case of capital it is the reverse process of encrypting the capital letters. Just multiply the base(127) with the number of iterations that was required to encrypt the capital letters.</p>


<h2> To test this with n number of words test.py is written for that </h2>

``To run this on terminal
use python test_app.py 
after entering the dir /Capital_Word_Encrypt_Decrypt``

# Windows Executable

``` TODO ```


<h2>License</h2>

<p>The project is released under <a href="https://github.com/sandeepmaxpayne/Capital_Word_Encrypt_Decrypt/blob/master/LICENSE">MIT License</a></p>


<p>Test the code: <a href="https://github.com/sandeepmaxpayne/Capital_Word_Encrypt_Decrypt/blob/master/test_app.py">Test_app.py</a></p>

