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


def main():
    repeat = True
    while repeat:
        print("=== Program Enkripsi ===")
        plaintext = input("Masukkan teks: ")
        shift = int(input("Masukkan jumlah pergeseran: "))
        encrypted_text = encrypt(plaintext, shift)
        print("Hasil enkripsi: ", encrypted_text)

        choice = input("Apakah Anda ingin melakukan program lagi? (y/n): ")
        if choice.lower() != "y":
            repeat = False
            print("Terima kasih telah menggunakan program.")


if __name__ == "__main__":
    main()
