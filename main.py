import math
import unittest


def function(*nums):
    arr=[-1]*len(nums)
    c=-1
    for x in nums:
        if type(x) == int or type(x) == float:
                if x < 1:
                    if x<0:
                        c+=1
                        print('Введённое Вами число на позиции '+str(c)+' не может быть обработано')
                    else:
                        c+=1
                        arr[c]=math.sin(x ** 0.5)
                else:
                   c+=1
                   arr[c]=math.cos(x**2)

        else:
            print('Неверный формат данных на позиции'+str(c)+'. Функция работает с числом')
    return arr


class FunctionTestCase(unittest.TestCase):
    def test_function(self):
        tested_function1 = function(12).pop()
        self.assertEqual(tested_function1,0.8711474010323434)
        tested_function2 = function(23).pop()
        self.assertEqual(tested_function2,0.3507408840091023)
        tested_function3 = function(0.3).pop()
        self.assertEqual(tested_function3,0.5207442995127205)
        tested_function4 = function(-1).pop()
        self.assertEqual(tested_function4,-1)



if __name__ == '__main__':
    unittest.main()



