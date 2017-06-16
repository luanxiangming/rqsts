import keyword
import unittest


class PythonBasics(unittest.TestCase):
    
    # python保留字
    def test_keyword(self):
        print(keyword.kwlist)

    # 自然字符串， 通过在字符串前加r或R。\n会显示，并不是换行。
    def test_raw_string(self): 
        print('\n')
        print(r'This is raw string\n')
        # python允许处理unicode字符串，加前缀u或U
        print('\n')
        print(u'This is unicode string')

    # 使用三引号('''或""")可以指定一个多行字符串。
    def test_cross_line_string(self):
        print('\n')
        paragraph = """这是一个多行字符串的实例
        多行字符串可以使用制表符
        TAB (\t)
        多行字符串可以使用制表符换行符[\n].
        """
        print(paragraph)

    # 在同一行中使用多条语句，语句之间使用分号(;)分割
    def test_multiple_in_one_line(self):
        print('\n')
        x = 'run'; y = 'oob'; print(x + y);

    # Print输出不换行
    def test_print_without_new_line(self):
        print('\n')
        print('a', end=' ')
        print('b', end=' ')

    # help() 函数可以打印输出一个函数的文档字符串
    def test_help(self):
        print('\n')
        help(max); help(max.__doc__)

    # 多个变量赋值
    def test_multiple_assign(self):
        print('\n')
        a = b = c = 1; print(a, b, c)
        a, b, c = 1, 2.0, '3'; print(a, b, c)

    # 内置的 type() 函数可以用来查询变量所指的对象类型
    def test_type(self):
        print('\n')
        a, b, c, d = 20, 5.5, True, 4+3j
        print(type(a), type(b), type(c), type(d))

    # 斐波纳契数列
    def test_fibonacci_series(self):
        a, b = 0, 1
        while b < 100:
            print(b, end=', ')
            a, b = b, b+a

if __name__ == '__main__':
    unittest.main()