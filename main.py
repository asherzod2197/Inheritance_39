# 39. Uy hayvonlari parvarishi

class PetCare:
    def __init__(self, pet_name, monthly_cost):
        self.pet_name = pet_name          # hayvon turi/nomi
        self.cost = monthly_cost          # oylik parvarish xarajati ($)

    def get_cost(self):
        """Hayvon parvarishi uchun oylik xarajat"""
        return self.cost

    def __str__(self):
        return f"{self.pet_name:12} | {self.cost:6.2f}$ / oy"


# -----------------------------------------------
# Voris sinflar (chiroyli chiqish + emoji)
# -----------------------------------------------

class DogCare(PetCare):
    def __str__(self):
        return f"🐶 {self.pet_name:10} → {self.cost:6.2f}$ / oy"


class CatCare(PetCare):
    def __str__(self):
        return f"🐱 {self.pet_name:10} → {self.cost:6.2f}$ / oy"


# --------------------------------------------------
# Umumiy xarajatlar ro‘yxatini chiqarish
# --------------------------------------------------

def show_pet_care_expenses(pets):
    print("\n" + "═" * 55)
    print("   UY HAYVONLARI PARVARISHI — OYLIK XARAJATLAR   ".center(55))
    print("═" * 55)
    print("Hayvon turi        Oylik xarajat")
    print("─" * 55)

    total_monthly = 0

    for pet in pets:
        print(pet)
        total_monthly += pet.get_cost()

    print("─" * 55)
    print(f"Jami oylik xarajat:               {total_monthly:8.2f}$")
    print(f"Yillik taxminiy xarajat:          {total_monthly * 12:8.2f}$")
    print("═" * 55 + "\n")


# Test ma'lumotlari
hayvonlar = [
    DogCare("It (katta zot)", 85.00),
    CatCare("Mushuk", 42.50),
    DogCare("It (kichik zot)", 55.00),
    CatCare("Mushuk (Persiya)", 65.00),
    DogCare("It (o'rta zot)", 70.00),
]

show_pet_care_expenses(hayvonlar)


# Sizning misol qiymatlaringiz bilan:
print("\nSizning misol hayvonlaringiz:\n")
misol_hayvonlar = [
    DogCare("It", 50),
    CatCare("Mushuk", 30),
]

show_pet_care_expenses(misol_hayvonlar)
