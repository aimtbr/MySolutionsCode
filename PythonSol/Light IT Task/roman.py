import romanconvert, sys
from PyQt5 import QtWidgets

#Корректно конвертирует числа до 3999 включительно, так как для чисел выше 3999 используется несколько другая нотация.


class romanConverter(QtWidgets.QDialog):
    def __init__(self):
        super(romanConverter, self).__init__()
        self.ui = romanconvert.Ui_Dialog()  #создаёт экземпляр класса интерфейса
        self.form = QtWidgets.QWidget()     #создаёт экземпляр класса QWidget
        self.ui_init()

    def ui_init(self):
        self.ui.setupUi(self.form)  #инициализирует форму
        self.form.show()            #выводит на экран форму
        self.run()

    def run(self):
        self.ui.convert.clicked.connect(self.solution)      #при нажатии на кнопку выполняется функция

    def solution(self):
        roman = self.ui.typein.text()           #записывает строку из QLineEdit в переменную roman
        pat = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

        #-----------------НАЧАЛО ПРОВЕРКИ-----------------
        if len(roman) == 0:
            self.ui.result.setText("Arabic result: " + "0")
            self.ui.typein.clear()     #после нажатия кнопки "Convert" очищает строку ввода
            return 0
        elif len(list(filter((lambda x: x not in list(pat.keys())), roman))) != 0:  #если ввели не римское число, то также
            self.ui.result.setText("Arabic result: " + "0")                         #возвращает 0
            self.ui.typein.clear()
            return 0
        elif len(roman) > 3:      #если длина римского числа больше 3, то...
            for i in range(len(roman)):      #переменная i инкрементируется в цикле от 0 до длины введённого римского числа
                if roman[i:i+4].count(roman[i]) == 4:       #проверяет введённое римское число на стоящие подряд 4 одинаковых числа
                    self.ui.result.setText("Arabic result: " + "0")   #записывает результат в QLabel
                    self.ui.typein.clear()
                    return 0                                #если 4 одинаковых числа стоят подряд, то возвращает 0
        #-----------------КОНЕЦ ПРОВЕРКИ-----------------

        o = [pat[x] for x in roman.strip()]  #для каждого числа из введённой римской строки берёт соответствующее значение
                                             #из словаря pat
        res, i = 0, 0                        #переменная res для хранения результата конвертации
        while i <= len(o) - 1:
            if i == len(o) - 1:             #если цикл дошёл до конца, то последнее число из списка о прибавляется к
                res += o[i]                 #переменной res, которая собирает в себя результат
            elif o[i] >= o[i + 1]:      #если данное римское число больше или равно следующему римскому числу в строке
                res += o[i]             #то данное число прибавляется к результату
            else:
                res += o[i + 1] - o[i]  #а если наоборот, данное число меньше, чем следующее, то следующее число вычитает данное
                                        #и прибавляется к переменной res, а то есть, к результату
                i += 1                  #и увеличивает цикл еще на один шаг, чтобы пропустить одно число, которое было вычтено
            i += 1
        self.ui.result.setText("Arabic result: " + str(res))
        self.ui.typein.clear()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    cnvrt = romanConverter()
    sys.exit(app.exec_())
