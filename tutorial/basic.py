import keyword
import unittest

class PythonBasic(unittest.TestCase):
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
        paragraph = '''This is paragraph 
        Section A 
        Section B'''
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

    # 数值运算
    def test_number_operations(self):
        self.assertEqual(2 / 4, 0.5)  # 除法(总是返回一个浮点数)，得到一个浮点数0.5
        self.assertEqual(2 // 4, 0) # 除法(总是返回一个整数)，得到一个整数0
        self.assertEqual(17 % 3, 2) # 取余 , 得到2
        self.assertEqual(2 ** 5, 32) # 乘方, 得到32

    # String（字符串）
    def test_string_operations(self):
        str = 'Runoob'
        self.assertEqual(str, 'Runoob')
        self.assertEqual(str[0:-1], 'Runoo')
        self.assertEqual(str[0], 'R')
        self.assertEqual(str[2:5], 'noo')
        self.assertEqual(str[2:], 'noob')
        self.assertEqual(str * 2, 'RunoobRunoob')
        self.assertEqual(str + "TEST", 'RunoobTEST')

    # List（列表）
    def test_list_operations(self):
        list = ['abcd', 786, 2.23, 'runoob', 70.2]
        tinylist = [123, 'runoob']
        self.assertEqual(list, ['abcd', 786 , 2.23, 'runoob', 70.2])
        self.assertEqual(list[0], 'abcd')
        self.assertEqual(list[1:3], [786 , 2.23])
        self.assertEqual(list[2:], [2.23, 'runoob', 70.2])
        self.assertEqual(tinylist * 2, [123, 'runoob',123, 'runoob'])
        self.assertEqual(list + tinylist, ['abcd', 786 , 2.23, 'runoob', 70.2, 123, 'runoob'])

    # Tuple（元组）
    def test_tupel_operations(self):
        tuple = ('abcd', 786, 2.23, 'runoob', 70.2)
        tinytuple = (123, 'runoob')
        self.assertEqual(tuple, ('abcd', 786 , 2.23, 'runoob', 70.2))
        self.assertEqual(tuple[0], 'abcd')
        self.assertEqual(tuple[1:3], (786, 2.23))
        self.assertEqual(tuple[2:], (2.23, 'runoob', 70.2))
        self.assertEqual(tinytuple * 2, (123, 'runoob', 123, 'runoob'))
        self.assertEqual(tuple + tinytuple, ('abcd', 786, 2.23, 'runoob', 70.2, 123, 'runoob'))

    # Set（集合）
    def test_set_operations(self):
        student = {'Tom', 'Jim', 'Mary', 'Tom', 'Jack', 'Rose'}
        print(student) # 输出集合，重复的元素被自动去掉
        # set可以进行集合运算
        a = set('abcdcd')
        b = set('cdefef')
        self.assertEqual(a, {'a', 'b', 'c', 'd'}) 
        self.assertEqual(b, {'c', 'd', 'e', 'f'})
        self.assertEqual(a - b, {'a', 'b'}) # a和b的差集
        self.assertEqual(a | b, {'a', 'b', 'c', 'd', 'e', 'f'}) # a和b的并集
        self.assertEqual(a & b, {'c', 'd'}) # a和b的交集
        self.assertEqual(a ^ b, {'a', 'b', 'e', 'f'}) # a和b中不同时存在的元素

    # Dictionary（字典）
    def test_dict_operations(self):
        new_dict = {}
        new_dict['one'] = "1 - 菜鸟教程"
        new_dict[2] = "2 - 菜鸟工具"
        tiny_dict = {'name': 'runoob', 'code': '1', 'site': 'www.runoob.com'}
        self.assertEqual(new_dict['one'], '1 - 菜鸟教程')
        self.assertEqual(new_dict[2], '2 - 菜鸟工具')
        self.assertEqual(sorted(tiny_dict.keys()), ['code', 'name', 'site'])
        self.assertEqual(sorted(tiny_dict.values()), ['1', 'runoob', 'www.runoob.com'])
        # 构造函数 dict() 可以直接从键值对序列中构建字典如下：
        new_dict2 = dict([('google', '1'), ('baidu', '2'), ('bing', '3')])
        self.assertEqual(new_dict2, {'baidu': '2', 'bing': '3', 'google': '1'})
        new_dict3 = {x: x**2 for x in range(1,5)}
        self.assertEqual(new_dict3, {1:1, 2:4, 3:9, 4:16})
        new_dict4 = dict(google=1, baidu=2, bing=3)
        self.assertEqual(new_dict4, {'baidu': 2, 'bing': 3, 'google': 1})



if __name__ == "__main__":
    unittest.main()

