from func import encrypt, decrypt

if __name__ == '__main__':
    message = str(input("Message:"))
    [code, cards] = encrypt(message)
    print("Coded message: ", code)
    decode = decrypt(code, cards)
    print("Your original message:", decode)