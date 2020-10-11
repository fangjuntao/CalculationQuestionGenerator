# -*- coding = 'uft-8' -*-

import re
import os

from SuffixExpression import SuffixExpression

#未测试
class Answer:

    exp_list = []
    exercisefile  = ""
    answerfile  = ""



    def __init__(self):  # 类的构造函数
        print("创建Answer类")



    def expression_result(self,exp_list):
        """
        求表达式的结果
            :param exp_list: 表达式列表
            :return: None
        """

        self.exp_list  =exp_list
        if os.path.exists('Answer.txt'):   # 清空上一次的答案
            with open('Answer.txt', 'r+') as file:
                file.truncate(0)

        for i, exp in enumerate(self.exp_list):
            order_str = str(i + 1)
            suffixExpression  = SuffixExpression(exp)
            #print("------suffixExpression:{}---------".format(str(suffixExpression.suffixToValue()) ))
            exp_value = str(suffixExpression.suffixToValue()) + '\n'
            result = "Answer"+order_str + ': ' + exp_value

            with open('Answer.txt', 'a+', encoding='utf-8') as f:
                f.write(result)





    def check_answer(self,exercisefile,answerfile):
        """
        校对答案
        :return: None
        """
        wrong_num = 0
        correct_num = 0
        exercise_answer = []
        correct_list = []  # 正确题目序号
        wrong_list = []  # 错误题目序号
        self.exercisefile = exercisefile
        self.answerfile  = answerfile
        try:
            with open(self.exercisefile, 'r', encoding='utf-8') as f:
                for line in f:
                    # 匹配出正则表达式

                    exp_str = re.findall(r'Question\d+: (.*) =\n', line)
                    if exp_str:
                        exp = exp_str[0]
                    else:
                        continue
                    p  = SuffixExpression(exp)
                    exp_value = str(p.suffixToValue())
                    exercise_answer.append(exp_value)
        except IOError:
            print('please check if the path is correct')

    # 判断表达式列表是否为空
        try:
            with open(self.answerfile, 'r', encoding='utf-8') as f:
                for i, line in enumerate(f):
                    ans_str = re.findall(r'Answer\d+: (.*)\n', line)
                    # 容错
                    if ans_str:
                        ans = ans_str[0]
                    else:
                        continue
                    # 判断是否正确
                    if ans == exercise_answer[i]:
                        correct_num += 1
                        correct_list.append(i + 1)
                    else:
                        wrong_num += 1
                        wrong_list.append(i + 1)
            with open('Grade.txt', 'w+', encoding='utf-8') as f:
                correct_str = 'Correct: ' + str(correct_num) + ' ' + str(correct_list) + '\n'
                wrong_str = 'Wrong: ' + str(wrong_num) + ' ' + str(wrong_list)
                f.write(correct_str)
                f.write(wrong_str)
        except IOError:
            print('please check if the path is correct')


if __name__ == '__main__':
    # exp_file = r'Exercises.txt'
    # ans_file = r'Answer.txt'
    exp_file = 'Exercises.txt'
    ans_file = 'Answer.txt'
    o  =  Answer(exp_file,ans_file)
    o.check_answer()
