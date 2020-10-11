# -*- coding = utf-8 -*-
from fractions import Fraction

#已经测试
class SuffixExpression:
    """
    将中缀表达式转化为后缀表达式
    计算后缀表达式的值

    """


    exp=""   #中缀表达式
    re =[]   #后缀表达式
    value = 1

    def __init__(self, exp):  # 类的构造函数
        self.exp = exp
        self.re = self.toSuffix()
        self.value = self.suffixToValue()

    def toSuffix(self):
        """
        中缀表达式转为后缀表达式
        :param: exp: 表达式字符串
        :return: result列表
        """
        if not self.exp:
            return []
        ops_rule = {
            '+': 1,
            '-': 1,
            '×': 2,
            '÷': 2,
        }
        suffix_stack = []  # 后缀表达式结果
        ops_stack = []  # 操作符栈
        infix = self.exp.split(' ')   # 将表达式分割得到单词
        # print(infix)
        for item in infix:

            if item in ['+', '-', '×', '÷']:  # 遇到运算符
                while len(ops_stack) >= 0:
                    if len(ops_stack) == 0:
                        ops_stack.append(item)
                        break
                    op = ops_stack.pop()
                    if op == '(' or ops_rule[item] > ops_rule[op]:
                        ops_stack.append(op)
                        ops_stack.append(item)
                        break
                    else:
                        suffix_stack.append(op)
            elif item == '(':  # 左括号直接入栈
                ops_stack.append(item)
            elif item == ')':  # 右括号
                while len(ops_stack) > 0:
                    op = ops_stack.pop()
                    if op == "(":        # 一直搜索到出现“(”为止
                        break
                    else:
                        suffix_stack.append(op)
            else:
                suffix_stack.append(item)  # 数值直接入栈

        while len(ops_stack) > 0:
            suffix_stack.append(ops_stack.pop())

        self.re =suffix_stack
        return suffix_stack


    def suffixToValue(self):
        """
        后缀表达式求值
        :return 运算结果
        """
        stack_value = []
        for item in self.re:
            #print("item")
            #print(item)
            if item in ['+', '-', '×', '÷']:
                n2 = stack_value.pop()
                n1 = stack_value.pop()
                result = self.cal(n1, n2, item)
                #print("resule:{}".format(result))
                # 求值过程中出现负数和n/0这个情况去除
                if result < 0 or result == False:
                    return False
                stack_value.append(result)
            else:
                if item.find('/') > 0:
                    attach = 0
                    right = ""
                    if item.find("'") > 0:
                        parts = item.split("'")
                        attach = int(parts[0])
                        right = parts[1]
                    else:
                        right = item
                    parts = right.split('/')
                    result = Fraction(attach * int(parts[1]) + int(parts[0]), int(parts[1]))
                    stack_value.append(result)
                else:
                    stack_value.append(Fraction(int(item), 1))

        return stack_value[0]


    def cal(self, n1, n2, op):
        if op == '+':
            return n1 + n2
        if op == '-':
            return n1 - n2
        if op == '×':
            return n1 * n2
        if op == '÷':
            if n2 == 0:
                return False
            return n1 / n2


