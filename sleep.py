import os
import asyncio


async def main():
    choices = {1: 15, 2: 30, 3: 60}
    while True:
        try:
            choice = int(input(
                f"\nВведи кол-во минут или цифру:\n\n{', '.join([f'{key} - {value} мин' for key, value in choices.items()])}\n\nВвод: "))

            if choice in choices.keys():
                text = f"\nЗапущен таймер гибернации на {choices[choice]} минут. Можно прервать через Ctrl + C"
                sleep = choices[choice]*60

            elif 0 < choice < 900:
                text = f"\nЗапущен таймер гибернации на {choice} минут. Можно прервать через Ctrl + C"
                sleep = choice*60

            else:
                raise Exception

            print(text)
            await asyncio.sleep(sleep)

            os.system("shutdown /h")
            break

        except KeyboardInterrupt:
            print(f"\n\nТаймер отключён")
            await asyncio.sleep(2)
            break

        except Exception:
            print(f"\nЧёт пошло не так :(")


if __name__ == '__main__':
    asyncio.run(main())
