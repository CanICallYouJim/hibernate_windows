# Hibernate windows
Гибернация - это как выключение ноутбука, только при включении все приложения работают как и прежде. Нужно, если надоедает открывать приложения при включении системы, а сон ест много энергии и со временем, по-тихоньку, убивает вашу батарею.

По какой-то причине, в windows 10 (лицензии) обнаружен баг - таймер на гибернацию не работает. На выключение и сон работает. На гибернацию - нет.

Мне эта проблема надоела и я накидал за час небольшой скрипт, который ждёт обозначенное время и исполняет команду shutdown /h.

Функционал:
- Запуская скрипт через .bat файл - можно ввести как цифру, означающую какое-то количество минут, так и число превышающее 0 и меньше 900 - оно будет использоваться как кол-во минут, после которого нужно исполнить команду.

Дополнительно:
- Внутри скрипта можно поставить какая цифра будет равна скольки минутам - эти данные подставятся и будут работать;
- .bat файл можно переместить например на рабочий стол, изменив скрипт внутри. Нужно добавить эту команду первой строкой - cd "%~dp0SomePath\", где SomePath - это путь до папки (!) с исполняемым файлом.
