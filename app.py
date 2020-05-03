from tkinter import *
from termcolor import colored

import encryptText
import decryptText


def encryptUI():

    sentences = enter_value.get()
    display_encrypted_text.delete(0.0, END)
    display_key_list.delete(0.0, END)
    display_key_order.delete(0.0, END)
    display_key_order.update()
    err_msg.delete(0.0, END)
    

    sentences = sentences.rstrip(" ").lstrip(" ").split(" ")
    sentence = []
    for i in sentences:
        if len(i) > 2:
            sentence.append(i)

    encrypted_sentence, keylist, order,  = [], [], []

    for i in sentence:
        if len(i) > 2:
            try:
                encrypted_texts, secret_keys, text_order = encryptText.encryptStr(i)
                # print(f'encrypted_texts: {encrypted_texts}, secretskeys: {secret_keys}, encrypted_text_order: {text_order}')
                encrypted_sentence.append(encrypted_texts)
                keylist.append(secret_keys)
                order.append(text_order)
                # print(encrypted_sentence, keylist, order)
            except:
                print(colored("Unable to fetch the keys. Make sure that word must be a combination of  Capital, Small and number or Single Capital , Small, length words of minimum size 3", color='red'))
                err_msg.insert(END, "Unable to fetch the keys. Make sure that word must be a combination of  Capital, Small and number or Single Capital , Small, length words of minimum size 3")
        else:
            print(colored("Word length is less than 3, cannot encrypt it", color='red'))
            err_msg.insert(END, "Word length is less than 3, cannot encrypt it")

        # print(sentence)
    print(encrypted_sentence, keylist, order)
    display_encrypted_text.insert(END, encrypted_sentence)
    display_key_list.insert(END, keylist)
    display_key_order.insert(END, order)
    return (sentence, sentences)
  
def clear_encrypted_all():
    display_encrypted_text.delete(1.0, END)
    display_key_list.delete(1.0, END)
    display_key_order.delete(1.0, END)
    err_msg.delete(0.0, END)

def clear_decrypted_all():
    display_decrypted_text.delete(0.0, END)
    enter_encr_value.set("")
    enter_key.set("")
    enter_map_key.set("")
    err_msg.delete(0.0, END)



def decryptUI():
    decrypted_result = []
    check_decrypt_status = []
    success_count = 0

    display_decrypted_text.delete(0.0, END)
    org_sent.delete(0.0, END)
    success_rate.delete(0.0, END)

    sentence = encryptUI()[0]
    sentences = encryptUI()[1]
    encrypted_sentence = enter_encr_value.get().split(" ")
    keylist = enter_key.get().split(" ")
    order = enter_map_key.get().split(" ")

    print("from user input", encrypted_sentence, keylist, order)

    for i in range(len(sentence)):
        try: 
            decrypted_result.append(decryptText.decryptText(encrypted_sentence[i], keylist[i], order[i]))
        except:
            pass
    for j in decrypted_result:
        if j in sentence:
            check_decrypt_status.append("success")
            success_count += 1
        else:
            check_decrypt_status.append("unsuccessful")
    print()
    print(colored(f'input sentence or word: \'{" ".join(sentences)}\'', color='white', attrs=['underline']))
    print(colored(f'original sentence after loss: \'{" ".join(sentence)}\'', color='yellow', attrs=['underline']))
    print(colored(f'encrypted sentence: \'{" ".join(encrypted_sentence)}\'', color='green', attrs=['underline']))
    print(f'encryption success count: {success_count}')
    print('\n')
    print(colored("Decrypted Text:", attrs=['bold', 'underline']))
    print(" ".join(decrypted_result))
    print(" ".join(check_decrypt_status))
    get_success_rate = ""
    if round(((success_count / len(sentences)) * 100), 2) > 80.0:
        print(colored(f'Decrypting Success rate : {round(((success_count / len(sentences)) * 100), 2)} %', color='green'))
        get_success_rate = f'{round(((success_count / len(sentences)) * 100), 2)} %'
    elif round(((success_count / len(sentences)) * 100), 2) >= 50.0 and round(((success_count / len(sentence)) * 100), 2) <= 80.0:
        print(colored(f'Decrypting Success rate: {round(((success_count / len(sentences)) * 100), 2)}%', color='cyan'))
        get_success_rate = f'{round(((success_count / len(sentences)) * 100), 2)} %'
    else:
        print(colored(f'Decrypting Success rate: {round(((success_count / len(sentences)) * 100), 2)}%', color='red'))
        get_success_rate = f'{round(((success_count / len(sentences)) * 100), 2)} %'
    display_decrypted_text.insert(END, decrypted_result)
    org_sent.insert(END, sentences)
    success_rate.insert(END, get_success_rate)



window = Tk()
window.geometry('1024x720')
window.title("DIATM FINAL YEAR PROJECT (YEAR 2020)")
window.iconbitmap("logo.ico")

### For Encryption ###
lab1 = Label(window, text="----ENCRYPTION----",  fg="black", font="Helvetica 25 bold italic")
lab1.grid(row=0, column=50)
lab1.grid_rowconfigure(1, weight=1)
lab1.grid_columnconfigure(0, weight=1)


Label(window, text="Enter Sentence:  ", fg="black").grid(row=3, column=4)
enter_value = StringVar()
input_word = Entry(window, textvariable=enter_value, width=60)
input_word.grid(row=3, column=6)


Label(window, text="Encrypted Text:  ", fg="black").grid(row=5, column=4)
display_encrypted_text = Text(window, width=50, height=2)
display_encrypted_text.grid(row=5, column=6)
scroll = Scrollbar(master=window)
scroll.config(command=display_encrypted_text.yview)
display_encrypted_text.config(yscrollcommand=scroll.set)
scroll.grid(row=5, column=7, sticky='ns')


Label(window, text="Key List:  ", fg="black").grid(row=6, column=4)
display_key_list = Text(window, width=50, height=2)
display_key_list.grid(row=6, column=6)
scroll = Scrollbar(master=window)
scroll.config(command=display_key_list.yview)
display_key_list.config(yscrollcommand=scroll.set)
scroll.grid(row=6, column=7, sticky='ns')


Label(window, text="Key Order:  ", fg="black").grid(row=7, column=4)
display_key_order = Text(window, width=50, height=2)
display_key_order.grid(row=7, column=6)
scroll = Scrollbar(master=window)
scroll.config(command=display_key_order.yview)
display_key_order.config(yscrollcommand=scroll.set)
scroll.grid(row=7, column=7, sticky='ns')

# Encrypt Button
enc_btn = Button(window, text="ENCRYPT", width=10, command=encryptUI)
enc_btn.grid(row=9, column=4)

clear_btn = Button(window, text="CLEAR", width=10, command=clear_encrypted_all)
clear_btn.grid(row=9, column=5)


''' Decryption UI '''

lab1 = Label(window, text="----DECRYPTION----",  fg="black", font="Helvetica 25 bold italic")
lab1.grid(row=15, column=50)


Label(window, text="Enter Encrypted Sentence:  ", fg="black").grid(row=17, column=4)
enter_encr_value = StringVar()
input_word = Entry(window, textvariable=enter_encr_value, width=60)
input_word.grid(row=17, column=6)

Label(window, text="Enter secret Keys:  ", fg="black").grid(row=18, column=4)
enter_key = StringVar()
input_word = Entry(window, textvariable=enter_key, width=60)
input_word.grid(row=18, column=6)

Label(window, text="Enter Mapping keys:  ", fg="black").grid(row=19, column=4)
enter_map_key = StringVar()
input_word = Entry(window, textvariable=enter_map_key, width=60)
input_word.grid(row=19, column=6)

Label(window, text="Decrypted Text:  ", fg="black").grid(row=20, column=4)
display_decrypted_text = Text(window, width=50, height=2)
display_decrypted_text.grid(row=20, column=6)
scroll = Scrollbar(master=window)
scroll.config(command=display_decrypted_text.yview)
display_decrypted_text.config(yscrollcommand=scroll.set)
scroll.grid(row=20, column=7, sticky='ns')

decrypt_btn = Button(window, text="DECRYPT", width=10, command=decryptUI)
decrypt_btn.grid(row=21, column=4)

clear_btn = Button(window, text="CLEAR", width=10, command=clear_decrypted_all)
clear_btn.grid(row=21, column=5)


Label(window, text="Original Sentence:  ", fg="black").grid(row=24, column=4)
org_sent = Text(window, width=50, height=2)
org_sent.grid(row=24, column=6)
scroll = Scrollbar(master=window)
scroll.config(command=org_sent.yview)
org_sent.config(yscrollcommand=scroll.set)
scroll.grid(row=24, column=7, sticky='ns')

Label(window, text="Decrypting Success Rate:  ", fg="black").grid(row=25, column=4)
success_rate = Text(window, width=50, height=2)
success_rate.grid(row=25, column=6)
success_rate.config( foreground="green")


Label(window, text="Error Message:  ", fg="black").grid(row=26, column=4)
err_msg = Text(window, width=50, height=2)
err_msg.grid(row=26, column=6)
err_msg.config( foreground="red")
scroll.config(command=err_msg.yview)
err_msg.config(yscrollcommand=scroll.set)
scroll.grid(row=26, column=7, sticky='ns')






# ### For Decryption ###
# Label(window, text="----DECRYPTION----",  fg="black", font="Helvetica 25 bold italic").pack()

window.mainloop()