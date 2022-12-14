# with open('./data.txt', 'w', encoding='utf-8') as f:
#     f.write('Python (МФА: [ˈpʌɪθ(ə)n]; в русском языке встречаются названия пито́н[23] или па́йтон[24]) — высокоуровневый язык программирования общего назначения с динамической строгой типизацией и автоматическим управлением памятью[25][26], ориентированный на повышение производительности разработчика, читаемости кода и его качества, а также на обеспечение переносимости написанных на нём программ[27]. Язык является полностью объектно-ориентированным в том плане, что всё является объектами[25]. Необычной особенностью языка является выделение блоков кода пробельными отступами[28]. Синтаксис ядра языка минималистичен, за счёт чего на практике редко возникает необходимость обращаться к документации[27]. Сам же язык известен как интерпретируемый и используется в том числе для написания скриптов[25]. Недостатками языка являются зачастую более низкая скорость работы и более высокое потребление памяти написанных на нём программ по сравнению с аналогичным кодом, написанным на компилируемых языках, таких как C или C++[27][25].')

def read_file(file_name):
    with open(file_name, 'r', encoding='UTF-8') as f:
        words = f.read().split()
        my_list = []
        for word in words:
            if word.isalpha() and word.islower() and len(word) > 3:
                my_list.append(word + '\n')
                unique_1 = set(my_list)
                unique = list(unique_1)
    return unique


def save_file(file_name):
    with open(file_name, 'w', encoding='utf-8') as f:
        a = str(len(read_file('data.txt')))
        f.write(a + '\n')
        f.writelines(sorted(read_file('data.txt')))

save_file('./save.txt')
