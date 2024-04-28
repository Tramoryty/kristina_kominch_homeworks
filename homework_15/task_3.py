# 3) Требуется создать csv-файл «rows_300.csv» со следующими столбцами:
# – № - номер по порядку (от 1 до 300);
# – Секунда – текущая секунда на вашем ПК;
# – Микросекунда – текущая миллисекунда на часах.
# На каждой итерации цикла искусственно приостанавливайте скрипт на 0,01 секунды.

import csv, time, datetime

with open('task_3.csv', 'w', encoding='utf-8', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['№', 'Секунда', 'Микросекунда'])

    for i in range(1,301):
        now = datetime.datetime.now()
        seconds = now.second
        microseconds = now.microsecond
        writer.writerow([i, seconds, microseconds])

        time.sleep(0.01)
