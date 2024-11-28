th_ch = 'ภถูุึคตจขชๆไำฎพฑะธัํี๊รณนฯยญบฐลฃฅฟฤหฆกฏดโเฌ้็่๋าษสศวซงผปแฉอฮิื์ทมฒใฬฝฦ'
en_ch = "456^7890-=qweErRtTyYuUiIoOpP[{]\|aAsSdDfFgGhHjJkKlL;:'zxcCvVbnNm,<.>/?"


def main():
    while True:
        print('1. TH -> EN\n2. EN -> TH\n3. Quit')
        inp = input('Input choice > ')

        if inp == '1':
            th_to_en()
        elif inp == '2':
            en_to_th()
        elif inp == '3':
            print('Goodbye!')
            break
        else:
            print('Invalid input!')


def th_to_en():
    dict_ = {}
    for i in range(len(th_ch)):
        dict_[th_ch[i]] = en_ch[i]

    while True:
        inp = input("Input Thai String ('+' to quit)\n> ")
        if inp == '+':
            break
        else:
            converted = []
            for ch in inp:
                if ch in th_ch:
                    converted.append(dict_[ch])
                else:
                    converted.append(ch)

            print('\n', ''.join(converted), '\n')


def en_to_th():
    dict_ = {}
    for i in range(len(th_ch)):
        dict_[en_ch[i]] = th_ch[i]

    while True:
        inp = input("Input English String ('+' to quit)\n> ")
        if inp == '+':
            break
        else:
            converted = []
            for ch in inp:
                if ch in en_ch:
                    converted.append(dict_[ch])
                else:
                    converted.append(ch)

            print('\n', ''.join(converted), '\n')


main()