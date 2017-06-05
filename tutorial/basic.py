import keyword, unittest, math, random

class PythonBasic(unittest.TestCase):
    ''' http://www.runoob.com/python3/python3-tutorial.html '''

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

    # 数学函数
    def test_math_functions(self):
        self.assertEqual(abs(-10), 10)
        self.assertEqual(math.ceil(4.1), 5) #数字的上入整数
        self.assertEqual(math.floor(3.9), 3) #数字的下舍整数
        self.assertEqual(math.exp(1), 2.718281828459045) #返回e的x次幂
        self.assertEqual(math.fabs(-10), 10.0) #返回数字的绝对值
        self.assertEqual(math.log(100, 10), 2.0)
        self.assertEqual(math.log10(100), 2.0)
        self.assertEqual(max(1, 2, 2.2), 2.2)
        self.assertEqual(min(-1, -2, -3.2), -3.2)
        self.assertEqual(math.modf(-3.0), (-0.0, -3.0)) #返回整数部分与小数部分，两部分的数值符号与x相同，整数部分以浮点型表示
        self.assertEqual(math.pow(100, -2), 100**-2) #x**y 运算后的值
        self.assertEqual(round(56.659, 1), 56.7) #返回浮点数x的四舍五入值，如给出n值，则代表舍入到小数点后的位数
        self.assertEqual(math.sqrt(4), 2.0) #返回数字x的平方根

    # 随机数函数
    def test_random(self):
        print('\n')
        print('Random number between 1~6: %s' % random.choice(range(1, 7)))
        print('Random number between 0~6: %s' % random.randrange(7))
        print('Random odd number between 1~9: %s' % random.randrange(1, 10, 2)) #从指定范围内，按指定基数递增的集合中获取一个随机数，基数缺省值为1
        print('Random number between 0~1: %s' % random.random()) #返回随机生成的一个实数，它在[0,1)范围内
        list_ = [1,2,3]; random.shuffle(list_) #将序列的所有元素随机排序
        print('Random shuffled list: %s' % list_)
        print('Random number between given range: %s' % random.uniform(math.e, math.pi)) #随机生成下一个实数，它在[x,y]范围内


    def test_string(self):
        self.assertEqual('abC1'.capitalize(), 'Abc1')
        self.assertEqual('abC1'.title(), 'Abc1')
        self.assertEqual('abcD'.swapcase(), 'ABCd') #对字符串的大小写字母进行转换
        self.assertEqual('abcd'.center(6, '*'), '*abcd*') #返回一个指定的宽度width居中的字符串，fillchar 为填充的字符，默认为空格
        self.assertEqual('abaa'.count('a', 0, 2), 1) #统计字符串里某个字符出现的次数。可选参数为在字符串搜索的开始与结束位置
        self.assertTrue('abc'.endswith('c'))

        self.assertEqual('firsts'.find('s'), 3); self.assertEqual('first'.find('w'), -1) #如果包含子字符串返回开始的索引值，否则返回-1
        self.assertEqual('firsts'.rfind('s'), 5) #返回字符串最后一次出现的位置，如果没有匹配项则返回-1
        self.assertEqual('firsts'.index('s'), 3) #与find()方法一样，只不过如果str不在string中会报一个异常ValueError
        self.assertEqual('firsts'.rindex('s'), 5) #类似于index()，不过是从右边开始

        self.assertTrue('runoob2016'.isalnum()); self.assertFalse('www runoob.2016'.isalnum()) #检测字符串是否由字母和数字组成
        self.assertTrue('runoob'.isalpha()); self.assertFalse('runoob2016'.isalpha()) #检测字符串是否只由字母组成
        self.assertTrue('1234'.isdigit()); self.assertFalse('一二三四'.isdigit()) #检测字符串是否只由数字组成
        self.assertTrue('一二三四'.isnumeric()) #检测字符串是否只由数字组成。这种方法是只针对unicode对象，包含汉字数字
        self.assertTrue('23444'.isdecimal()); self.assertFalse('abc123'.isdecimal()) #检查字符串是否只包含十进制字符,这种方法只存在于unicode对象

        self.assertTrue('runoob..wow!!'.islower()); self.assertFalse('RUNOOB..wow!!'.islower()) #检测字符串是否由小写字母组成
        self.assertTrue('   '.isspace()) #测字符串是否只由空格组成
        self.assertTrue('This Is Title Format.'.istitle()); #检测字符串中所有的单词拼写首字母是否为大写，且其他字母为小写
        self.assertTrue('ABC...DEF'.isupper()) #检测字符串中所有的字母是否都为大写
        self.assertEqual('-'.join(('1','2','3')), '1-2-3') #将序列中的元素以指定的字符连接生成一个新的字符串

        self.assertEqual('abcd'.ljust(10, '*'), 'abcd******') #返回一个原字符串左对齐,并使用fillchar填充至长度width的新字符串
        self.assertEqual('abcd'.rjust(10, '*'), '******abcd') #返回一个原字符串右对齐,并使用fillchar填充至长度width的新字符串
        self.assertEqual('abcd'.zfill(10), '000000abcd') #返回指定长度的字符串，原字符串右对齐，前面填充0
        self.assertEqual('  abc'.lstrip(), 'abc'); self.assertEqual('888abc'.lstrip('8'), 'abc') #截掉字符串左边的空格或指定字符
        self.assertEqual('abc  '.rstrip(), 'abc'); self.assertEqual('abc888'.rstrip('8'), 'abc') #截掉字符串右边的空格或指定字符
        self.assertEqual('**abcd*****'.strip('*'), 'abcd') #移除字符串头尾指定的字符（默认为空格）

        # 创建字符映射的转换表，对于接受两个参数的最简单的调用方式，第一个参数是字符串，表示需要转换的字符，第二个参数也是字符串表示转换的目标。
        transtab = str.maketrans('aeiou', '12345')
        self.assertEqual('this is string example....wow'.translate(transtab), 'th3s 3s str3ng 2x1mpl2....w4w')
        self.assertEqual(max('aeiou'), 'u') #返回字符串中最大的字母
        self.assertEqual(min('aeiouV'), 'V') #返回字符串中最小的字母
        self.assertEqual('This is island'.replace('is', 'was', 2), 'Thwas was island') #把将字符串中的str1替换成str2,如果max指定则替换不超过max次
        self.assertEqual('this is string example'.split('t', 1), ['', 'his is string example']) #指定分隔符对字符串进行切片,仅分隔num个子字符串
        self.assertEqual('ab c\n\nde fg\rkl\r\n'.splitlines(), ['ab c', '', 'de fg', 'kl']) #按照行('\r','\r\n',\n')分隔,返回一个包含各行作为元素的列表
        self.assertEqual('ab c\n\nde fg\rkl\r\n'.splitlines(True), ['ab c\n', '\n', 'de fg\r', 'kl\r\n']) #参数keepends为False,不包含换行符;为True,保留换行符
        self.assertTrue('this is string'.startswith('th')); self.assertFalse('this is string'.startswith('th', 2)) #参数beg和end指定值，则在指定范围内检查


if __name__ == "__main__":
    unittest.main()

