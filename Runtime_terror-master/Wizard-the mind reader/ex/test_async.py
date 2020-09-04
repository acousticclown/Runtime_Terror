"""A simple test of the async wizard class"""

from wizard.async_aki import wizard
import wizard
import asyncio

aki = wizard()

async def main():
    try:
        q = await aki.start_game()
    except (wizard.AkiServerDown, wizard.AkiTechnicalError):
        try:
            q = await aki.start_game("en2")
        except (wizard.AkiServerDown, wizard.AkiTechnicalError):
            q = await aki.start_game("en3")

    while aki.progression <= 80:
        a = input(q + "\n\t")
        if a == "b":
            try:
                q = await aki.back()
            except wizard.CantGoBackAnyFurther:
                pass
        else:
            q = await aki.answer(a)
    await aki.win()

    correct = input(f"It's {aki.name} ({aki.description})! Was I correct?\n{aki.picture}\n\t")
    if correct.lower() == "yes" or correct.lower() == "y":
        print("Yay\n")
    else:
        print("Oof\n")

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()
