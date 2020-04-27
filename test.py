import encryptText
import decryptText

def test():
    encrypted_texts, secret_keys, text_order = encryptText.encryptStr("SAnd124Panye")
    print(f'encrypted_texts: {encrypted_texts}, secretskeys: {secret_keys}, encrypted_text_order: {text_order}')

    print(decryptText.decryptText(encrypted_texts, secret_keys, text_order))
test()