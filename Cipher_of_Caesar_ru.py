arr1 = ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф',
        'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я',
        'а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф',
        'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я'
        ]
arr2 = arr1.copy()



crypt = 'crypt_ru.txt'
decrypt = 'decrypt_ru.txt'


def change_arr2():
    for i in range(number):
        arr2.append(arr2[0])
        arr2.remove(arr2[0])


print('1) Шифровать текст/файл')
print('2) Расшифровать текст из файла')
print('3) Расшифровать текст с терминала\n')

try:
    ans = int(input('[*] Напишите номер: \n[Номер] > '))

    if ans == 1:
        number = int(input('[*] Введите номер ключа [0-{0}] '.format(str(len(arr1)))))

        change_arr2()

        msg = input('\n[*]  Напишите текст:\n [Текст] >> ')

        msgc = ''
        for i in msg:
            for j in range(len(arr1)):
                if i == arr1[j]:
                    msgc += arr2[j]

        crypt = open(crypt, 'w')
        print('\nCrypt-text: {0}\n'.format(msgc))
        crypt.write(msgc)
        crypt.close()

    elif ans == 2:

        number = int(input('[*] Введите номер ключа [0-{0}] '.format(str(len(arr1)))))

        change_arr2()

        decrypt_r = open(crypt, 'r')
        read = decrypt_r.read()
        msgd = ''
        for i in read:
            for j in range(len(arr1)):
                if i == arr2[j]:
                    msgd += arr1[j]

        print('\n[*] Расшифрованный текст:')
        print('[Текст] << {0}'.format(str(msgd)))

        answer = input('\n[*] Сохранить расшифрованный текст в файле?\n[y/n] > ')

        if answer == 'Y' or answer == 'y':
            decrypt_w = open(decrypt, 'w')
            decrypt_w.write(msgd)
            decrypt_w.close()
            print("\n[+] Файл 'decrypt_ru.txt' успешно сохранен! ")
        else:
            pass
        decrypt_r.close()

    elif ans == 3:

        number = int(input('[*] Введите номер ключа [0-{0}] '.format(str(len(arr1)))))

        change_arr2()

        msg = input('\n[*] Запись зашифрованного текста:\n[text] >> ')
        msgd = ''
        for i in msg:
            for j in range(len(arr1)):
                if i == arr2[j]:
                    msgd += arr1[j]

        print('\n[*] Расшифрованный текст:\n')
        print('[Текст] << {0}'.format(str(msgd)))
    else:
        print('Номер не определен!')

except ValueError:
    print('Ошибка! Введите число!')
