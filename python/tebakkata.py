import random

# Daftar kata yang bisa ditebak
word_list = ["python", "java", "koding", "komputer", "program", "algoritma", "developer"]

# Memilih kata secara acak
selected_word = random.choice(word_list)

# Membuat list yang menunjukkan posisi huruf yang sudah ditebak
guessed_word = ["_"] * len(selected_word)

# Jumlah maksimal percakapan
max_attempts = 6
attempts = 0

print("Selamat datang di permainan Tebak Kata!")
print("Kata yang harus ditebak memiliki", len(selected_word), "huruf.")
print("Coba tebak kata tersebut!")

# Permainan dimulai
while attempts < max_attempts:
    print("\nKata yang sedang kamu coba tebak:", " ".join(guessed_word))
    guess = input("Masukkan satu huruf: ").lower()

    # Mengecek input pemain
    if len(guess) != 1 or not guess.isalpha():
        print("Masukkan hanya satu huruf yang valid.")
        continue

    # Mengecek apakah huruf sudah ditebak sebelumnya
    if guess in guessed_word:
        print("Huruf ini sudah kamu tebak sebelumnya.")
        continue

    # Mengecek apakah huruf ada dalam kata yang dipilih
    if guess in selected_word:
        print(f"Selamat! Huruf '{guess}' ada dalam kata.")
        # Memperbarui kata yang sedang ditebak
        for index, letter in enumerate(selected_word):
            if letter == guess:
                guessed_word[index] = guess
    else:
        print(f"Sayang sekali, huruf '{guess}' tidak ada dalam kata.")
        attempts += 1

    # Mengecek apakah pemain sudah menebak kata dengan benar
    if "_" not in guessed_word:
        print(f"\nSelamat! Kamu berhasil menebak kata: {''.join(guessed_word)}")
        break
else:
    print(f"\nGame over! Kamu gagal menebak kata. Kata yang benar adalah: {selected_word}")
    



