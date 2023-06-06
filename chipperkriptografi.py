def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            if char.islower():
                encrypted_text += chr((ord(char) - 97 + shift) % 26 + 97)
            else:
                encrypted_text += chr((ord(char) - 65 + shift) % 26 + 65)
        elif char.isdigit():
            encrypted_text += str((int(char) + shift) % 10)
        else:
            encrypted_text += char
    return encrypted_text


def decrypt(encrypted_text, shift):
    decrypted_text = ""
    for char in encrypted_text:
        if char.isalpha():
            if char.islower():
                decrypted_text += chr((ord(char) - 97 - shift) % 26 + 97)
            else:
                decrypted_text += chr((ord(char) - 65 - shift) % 26 + 65)
        elif char.isdigit():
            decrypted_text += str((int(char) - shift) % 10)
        else:
            decrypted_text += char
    return decrypted_text


def main():
    while True:
        print("==== Program Cipher Pergeseran ====")
        text = input("Masukkan pesan: ")
        shift = int(input("Masukkan jumlah pergeseran: "))
        print("\n==== hasil ====")

        encrypted_text = encrypt(text, shift)
        print("Pesan terenkripsi:", encrypted_text)
        print("---------------")
        decrypted_text = decrypt(encrypted_text, shift)
        print("Teks terdekripsi:", decrypted_text)

        repeat = input("Apakah Anda ingin melakukan enkripsi lagi? (y/n): ")
        if repeat.lower() != "y":
            break


if __name__ == "__main__":
    main()
