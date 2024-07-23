import asyncio
from classes import *

async def fight(frog1, frog2):
    while frog1.health > 0 and frog2.health > 0:
        frog1_attack = frog1.get_attack()
        frog2_attack = frog2.get_attack()

        frog1_armor = frog1.get_armor()
        frog2_armor = frog2.get_armor()

        frog1_damage = max(0, frog2_attack - frog1_armor)
        frog2_damage = max(0, frog1_attack - frog2_armor)

        frog1.health -= frog1_damage
        frog2.health -= frog2_damage

    if frog1.health > frog2.health:
        return 1
    else:
        return 2


async def run_battles():
    victories = {1: 0, 2: 0}    # создаём счётчик побед
    frog_classes = [Assassin, Adventurer, Artisan]

    task_fight = []

    for _ in range(100):    # Запускаем бои

        frog1_class = random.choice(frog_classes)   # Создаём жаб
        frog2_class = random.choice(frog_classes)

        frog1 = frog1_class()
        frog2 = frog2_class()

        frog1.class_bonus()     # Присваиваем классы
        frog2.class_bonus()

        task_fight.append(asyncio.create_task(fight(frog1=frog1, frog2=frog2)))     # Сооздаём бой

    results = await asyncio.gather(*task_fight)     # Асинхронной запускаем бои
    for result in results:
        victories[result] += 1      # Считаем побы

    return victories


async def main():
    results = await asyncio.gather(run_battles(), run_battles())
    total_victories = {1: 0, 2: 0}

    for result in results:
        total_victories[1] += result[1]
        total_victories[2] += result[2]

    print(f'Frog1 wins: {total_victories[1]}')
    print(f'Frog2 wins: {total_victories[2]}')


if __name__ == "__main__":
    asyncio.run(main())
