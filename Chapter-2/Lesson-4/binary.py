# coding:utf-8
# Frank的工具箱
# 凌云工具箱
# 起因：前几天用python实现了几种古典密码算法，期间频繁涉及到字符串、二进制、数字串之间的转换，
# 前几次都是在多个文件中分别去写，一点也不美，现在将其打包在一起，我也可以增加一些其他功能，构成
# 我的专属工具箱O(∩_∩)O哈哈~

# 更新日期 2019.3.29
# 更新内容：新增swap()函数

'''
ItoB(int n):
    功能：数字转二进制
    输入：0-255之间的整数
    返回：8位二进制字符串，不足8位用0补齐

CtoB(char ch): 
    功能：单字符转二进制
    输入：单字符;
    返回：8位二进制字符串，不足8位用0补齐。

BtoS(string s): 
    功能：将二进制字符串转为字符串;
    注意：每8位二进制对应一个字符，无奇偶校验;
    返回：转换后的字符串。

OXR(string L, string R): 
    功能: 将另个二进制字符串逐位进行异或运算;
    输入：两个等长二进制字符串;
    输出：异或运算后的等长二进制字符串。

swap(a, b):
    用于交换a, b两个变量的值
'''

def ItoB(I):
    '''
    功能：数字转二进制
    输入：0-255之间的整数
    返回：8位二进制字符串，不足8位用0补齐
    '''
    if(isinstance(I,int) == False or I < 0 or I > 255):
        return '参数错误！'

    BinarySequence = ''
    while(True):
        if(I % 2 == 0):
            BinarySequence += '0'
        else:
            BinarySequence += '1'
        I = I // 2
        if(I == 1):
            break
        #print(OrdCh,BinarySequence)
    BinarySequence += '1'
    # 补齐8位
    length = 8 - len(BinarySequence)
    while(length):
        BinarySequence += '0'
        length -= 1
    #print('BinarySequence:{}'.format(BinarySequence))
    return BinarySequence[::-1]

def StoB( S, n=8):
    '''
    功能：字符串转二进制
    输入：字符串s, 每个字母位数n(默认值为8，实际输入至少7)
    返回：二进制字符串，单字符不足n位用0补齐
    '''
    if(isinstance(n,int) == False or n < 7):
        return '参数错误！'

    Bin = ''

    for c in [ord(i) for i in S]:
        #print('c',c)
        bin_unit = ''
        while(True):
            if(c % 2 == 0):
                bin_unit += '0'
            else:
                bin_unit += '1'
            c = c // 2
            if(c == 1):
                break
        bin_unit += '1'

        # 补齐n位
        length = n - len(bin_unit)
        #print(length)
        while(length):
            bin_unit += '0'
            length -= 1 
            #print(length,bin_unit)
        #print(bin_unit)
        Bin += bin_unit[::-1]
    return Bin

# 二进制转字符串（或单字符）
def BtoS(Bin,n=8):
    '''
    功能：将二进制字符串转为字符串
    注意：每n位二进制对应一个字符，无奇偶校验
    返回：转换后的字符串
    '''
    St = ''
    OrdCh = 0
    length = n
    for i in Bin:
        length -= 1
        OrdCh += (ord(i)-ord('0'))*(2**length)
        #print(length,i,OrdCh)
        if(length == 0):
            St += chr(OrdCh)
            length = n
            OrdCh = 0
    return St

# 二进制异或运算
# exclusive OR，缩写成xor
def XOR(L, R):
    '''
    功能: 将两个二进制字符串逐位进行异或运算
    输入：两个等长二进制字符串
    输出：异或运算后的等长二进制字符串
    '''
    result = ''
    for i,j in zip(L, R):
        #print(i,j)
        if(i == j):
            result += '0'
        else:
            result += '1'
    #print('result:{}'.format(result))
    return result

# swap
def swap(a,b):
    '''
    输入：a,b;
    输出：b,a.
    '''
    return b,a
