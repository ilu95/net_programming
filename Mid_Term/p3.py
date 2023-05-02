class MyComplex:
    def __init__(self, real_1, imaginary_1, real_2, imaginary_2):
        self.real_1 = real_1
        self.imaginary_1 = imaginary_1
        self.real_2 = real_2
        self.imaginary_2 = imaginary_2

    def plus(self):
        real_part = self.real_1 + self.real_2
        imaginary_part = self.imaginary_1 + self.imaginary_2
        if '-' in str(imaginary_part):
            print(f'{real_part}{imaginary_part}i')
        else:
            print(f'{real_part}+{imaginary_part}i')

    def minus(self):
        real_part = self.real_1 - self.real_2
        imaginary_part = self.imaginary_1 - self.imaginary_2
        if '-' in str(imaginary_part):
            print(f'{real_part}{imaginary_part}i')
        else:
            print(f'{real_part}-{imaginary_part}i')


a = MyComplex(2, -3, -5, 4)
a.plus()
a.minus()
