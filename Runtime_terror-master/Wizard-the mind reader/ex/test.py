"""A simple test of the wizard class"""

import wizard

aki = wizard.wizard()

try:
    q = aki.start_game()
except (wizard.AkiServerDown, wizard.AkiTechnicalError):
    try:
        q = aki.start_game("en2")
    except (wizard.AkiServerDown, wizard.AkiTechnicalError):
        q = aki.start_game("en3")

while aki.progression <= 80:
    a = input(q + "\n\t")
    if a == "b":
        try:
            q = aki.back()
        except wizard.CantGoBackAnyFurther:
            pass
    else:
        q = aki.answer(a)
aki.win()

correct = input(f"It's {aki.name} ({aki.description})! Was I correct?\n{aki.picture}\n\t")
if correct.lower() == "yes" or correct.lower() == "y":
    print("Yay\n")
else:
    print("Oof\n")
