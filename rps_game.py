import random

def main():
    choices = ["batu", "gunting", "kertas"]
    user = input("Pilih batu, gunting, atau kertas: ").lower()
    computer = random.choice(choices)

    print(f"Komputer memilih: {computer}")

    if user == computer:
        print("Seri!")
    elif (user == "batu" and computer == "gunting") or \
         (user == "gunting" and computer == "kertas") or \
         (user == "kertas" and computer == "batu"):
        print("Kamu menang!")
    else:
        print("Kamu kalah!")

if __name__ == "__main__":
    main()
