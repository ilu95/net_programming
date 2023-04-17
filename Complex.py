class MyComplex:
    def Complex(a, b):
        if a[0] == '-':
            if '-' in a[1:]:
                a = a[1:].split('-')
                real_1 = -int(a[0])
                imaginary_1 = -int(a[1][:-1])
            else:
                a = a[1:].split('+')
                real_1 = -int(a[0])
                imaginary_1 = int(a[1][:-1])
        else:
            if '-' in a:
                a = a.split('-')
                real_1 = int(a[0])
                imaginary_1 = -int(a[1][:-1])
            else:
                a = a.split('+')
                real_1 = int(a[0])
                imaginary_1 = int(a[1][:-1])
        if b[0] == '-':
            if '-' in b[1:]:
                b = b[1:].split('-')
                real_2 = -int(b[0])
                imaginary_2 = -int(b[1][:-1])
            else:
                b = b[1:].split('+')
                real_2 = -int(b[0])
                imaginary_2 = int(b[1][:-1])
        else:
            if '-' in b:
                b = b.split('-')
                real_2 = int(b[0])
                imaginary_2 = -int(b[1][:-1])
            else:
                b = b.split('+')
                real_2 = int(b[0])
                imaginary_2 = int(b[1][:-1])

        real_result = str((real_1*real_2)-(imaginary_1*imaginary_2))
        imaginary_result = str((real_1*imaginary_2)+(imaginary_1*real_2))+"i"
        if '-' not in imaginary_result:
            imaginary_result = "+" + imaginary_result
        print(real_result + imaginary_result)


a = "3-4i"
b = "-5+2i"
MyComplex.Complex(a, b)
