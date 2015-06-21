#!/usr/bin/python
# -*- coding:utf-8 -*-
import random
import time
import math
"""
    python 求最大公约数和最小公倍数
"""
def is_prime(n):
    """ 
        求一个数是否是素数
    """
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

def greatest_common_divisior(a, b):
    """ 
    求最大公约数：
    1、我自己的解法：求出a 的约数，b的约数，最后算公共的约数，求最大数
    2、质因数分解法：把每个数分别分解质因数，再把各数中的全部公有质因数提取出来连乘，所得的积就是这几个数的最大公约数。（质因数：能整除给定正整数的质数/素数）
    3、短除法：先用这几个数的公约数连续去除，一直除到所有的商互质为止，然后把所有的除数连乘起来，所得的积就是这几个数的最大公约数
    4、辗转相除法：辗转相除法是求两个自然数的最大公约数的一种方法，也叫欧几里德算法。
    5、更相减损法：

    """
    def myself_divisior(a, b):
        a_list = []
        for i in xrange(2, a):
            if a % i == 0:
                a_list.append(i)
        b_list = []
        for j in xrange(2, b):
            if b % j == 0:
                b_list.append(j)
        a_set, b_set = set(a_list), set(b_list)
        if a_set & b_set:
            return max(a_set & b_set)
        return 1

    def func_prime_factors(a, b):
        """ 质因数分解法 """
        def min_prime_factors(num):
            """ 求最小的因数:  """
            for x in xrange(2, num+1):
                if num % x == 0:
                    return x
            return 0
        a_list = []
        while a != 1:
            if min_prime_factors(a):
                mina = min_prime_factors(a)
                a_list.append(mina)
                a = a / mina
            else:
                break
        b_list = []
        while b != 1:
            if min_prime_factors(b):
                minb = min_prime_factors(b)
                b_list.append(minb)
                b = b / minb
            else:
                break
        # print 'a_list: %s, b_list: %s' %(a_list, b_list)
        common = []
        for x in a_list:
            if x in b_list:
                common.append(x)
                b_list.remove(x)
        # print 'common: %s' %common
        if not common:
            return 1
        return reduce(lambda x,y: x*y, common)

    def short_division(a, b):
        def common_factors(num1, num2):
            """ 拿公因数去除，一直到结果互质为止。最大公约数就是 所有除数的乘积  """
            common = []
            while True:
                max_num = max(num1, num2)
                for x in xrange(2, int(math.sqrt(max_num + 1)) + 1):
                    if num1 % x == 0 and num2 % x == 0:
                        num1 /= x
                        num2 /= x
                        common.append(x)
                        break
                if is_prime(num1) and is_prime(num2):
                    return common
                    break
        lst = common_factors(a, b)
        if lst:
            if len(lst) == 1:
                lst.append(1)
            return reduce(lambda x,y: x*y, lst)
        return 1

    def euclidean_algorithm(num1, num2):
        """
            欧几里得算法原理：
            设两数为a、b(b<a），用gcd(a,b）表示a，b的最大公约数，r=a mod b 为a除以b以后的余数，k为a除以b的商，即a÷b=k...r。
                辗转相除法即是要证明gcd(a,b)=gcd(b,r）。
            第一步：令c=gcd(a,b），则设a=mc，b=nc
            第二步：根据前提可知 r = a-kb = mc - knc = (m-kn)c
            第三步：根据第二步结果可知c也是r的因数
            第四步：可以断定m-kn与n互质【否则，可设m-kn=xd，n=yd，（d>1），则m=kn+xd=kyd+xd=(ky+x)d，
                则a=mc=(ky+x)dc，b=nc=ycd，故a与b最大公约数成为cd，而非c，与前面结论矛盾】
            欧几里得算法解法：
            1、a ÷ b，令r为所得余数（0≤r<b），若 r = 0，算法结束；b 即为答案。
            2、互换：置 a←b，b←r，并返回第一步
            欧几里得算法解法：
            1、若 r 是 a ÷ b 的余数，则gcd(a,b) = gcd(b,r)
            2、a 和其倍数之最大公因子为 b。
        """
        while True:
            r = num1 % num2
            if r == 0:
                break
            num1, num2 = num2, r

        return num2

    def equivalent_algorithm(num1, num2):
        """
            更相减损法，也叫等值算法
            第一步：任意给定两个正整数；判断它们是否都是偶数。若是，则用2约简；若不是则执行第二步。
            第二步：以较大的数减较小的数，接着把所得的差与较小的数比较，并以大数减小数。继续这个操作，直到所得的减数和差相等为止。
            则第一步中约掉的若干个2与第二步中等数的乘积就是所求的最大公约数。
        """
        result = []
        ### 如果是偶数，则使用2约简
        while True:
            if num1 % 2 == 0 and num2 % 2 == 0:
                num1 /= 2
                num2 /= 2
                result.append(2)
                continue
            else:
                break
        ### 以大数，减去小数，差与较小的数比较，并相减。一直减，直到 差和被减数相等为止
        while True:
            max_num = max(num1, num2)
            min_num = min(num1, num2)
            sub = max_num - min_num
            if sub == min_num:
                result.append(sub)
                break
            num1 = min_num
            num2 = sub

        if not result:
            return 1
        return reduce(lambda x,y:x*y, result)

    # start_time = time.time()
    # max_number = myself_divisior(a, b)
    # use_time = time.time() - start_time
    # print 'a为：%s, b为：%s, 最大公约数是：%s, 耗时：%s' %(a, b, max_number, use_time)

    # print '-'*30 + '质因数分解法求最大公约数' + '-'*30
    # start_time = time.time()
    # max_number = func_prime_factors(a, b)
    # use_time = time.time() - start_time
    # print 'a为：%s, b为：%s, 最大公约数是：%s, 耗时：%s' %(a, b, max_number, use_time)


    # print '-'*30 + '短除法求最大公约数' + '-'*30
    # start_time = time.time()
    # max_number = short_division(a, b)
    # use_time = time.time() - start_time
    # print 'a为：%s, b为：%s, 最大公约数是：%s, 耗时：%s' %(a, b, max_number, use_time)


    # print '-'*30 + '辗转相除法（欧几里得算法）求最大公约数' + '-'*30
    # start_time = time.time()
    # max_number = euclidean_algorithm(a, b)
    # use_time = time.time() - start_time
    # print 'a为：%s, b为：%s, 最大公约数是：%s, 耗时：%s' %(a, b, max_number, use_time)


    print '-'*30 + '更相减损法法（等值算法）求最大公约数' + '-'*30
    start_time = time.time()
    max_number = equivalent_algorithm(a, b)
    use_time = time.time() - start_time
    print 'a为：%s, b为：%s, 最大公约数是：%s, 耗时：%s' %(a, b, max_number, use_time)


def least_common_multiple(a, b):
    """
    求最小公倍数：
    1、质因数分解法：把几个数先分别分解质因数，再把各数中的全部公有的质因数和独有的质因数提取出来连乘，所得的积就是这几个数的最小公倍数。

    """
    def func_prime_factors(a, b):
        """ 质因数分解法 """
        def min_prime_factors(num):
            """ 求最小的因数:  """
            for x in xrange(2, num+1):
                if num % x == 0:
                    return x
            return 0
        a_list = []
        while a != 1:
            if min_prime_factors(a):
                mina = min_prime_factors(a)
                a_list.append(mina)
                a = a / mina
            else:
                break
        b_list = []
        while b != 1:
            if min_prime_factors(b):
                minb = min_prime_factors(b)
                b_list.append(minb)
                b = b / minb
            else:
                break
        # print 'a_list: %s, b_list: %s' %(a_list, b_list)
        multiple = []
        multiple.extend([x for x in a_list if x in b_list])
        multiple.extend([x for x in a_list if x not in b_list])
        multiple.extend([x for x in b_list if x not in a_list])

        # print 'common: %s' %common
        if not multiple:
            return 1
        return reduce(lambda x,y: x*y, multiple) 

    print '+' * 100
    print '-'*40 + '质因数分解法求最小公倍数' + '-'*40
    start_time = time.time()
    min_multiple = func_prime_factors(a, b)
    use_time = time.time() - start_time
    print 'a为：%s, b为：%s, 最小公倍数是：%s, 耗时：%s' %(a, b, min_multiple, use_time)

if __name__ == '__main__':
    a, b = 16, 24
    greatest_common_divisior(a, b)

    least_common_multiple(a, b)


