# __init__ 메소드는 클래스의 인스턴스가 생성될 때 자동으로 호출되는 생성자 함수입니다. 여기서는 클래스의 멤버 변수들을 초기화하고 있습니다.
# multiplication 메소드는 클래스 내부에서 곱셈 연산을 수행하고, 결과를 출력하는 함수입니다. 곱셈 연산에 대한 계산식을 그대로 구현하였습니다.
# 마지막으로, a라는 이름으로 MyComplex 클래스의 인스턴스를 생성하고, multiplication 메소드를 호출하여 결과를 출력하고 있습니다.

class MyComplex:
    def __init__(self, real_1, imaginary_1, real_2, imaginary_2):
        self.real_1 = real_1
        self.imaginary_1 = imaginary_1
        self.real_2 = real_2
        self.imaginary_2 = imaginary_2

    def multiplication(self):
        real_part = self.real_1 * self.real_2 - self.imaginary_1 * self.imaginary_2
        imaginary_part = self.real_1 * self.imaginary_2 + self.real_2 * self.imaginary_1
        print(f'({self.real_1}-{self.imaginary_1}i) x ({self.real_2}-{self.imaginary_2}i) = {real_part}+{imaginary_part}i')


a = MyComplex(3, -4, -5, 2)
a.multiplication()
