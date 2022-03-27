
# Question 1: (A.) 請寫⼀個程式把裡⾯的字串反過來。 (B.) 請寫⼀個程式把裡⾯的字串，每個單字本⾝做反轉，但是
# 單字的順序不變。

def flip_one_word(word):

    return word[::-1]

def flip_sentence(words):
    result = [flip_one_word(word) for word in words.strip().split()]
    return " ".join(result)

# Question 2: 請寫⼀個程式，Input 是⼀個數字，Output 是從 1 到這個數字，扣除掉所有 3 的倍數以及 5 的倍數，但是
# 需要保留同時是 3 和 5 的倍數的總數字數。
def delet_numbers(number):
    answer = []
    for i in range(1, number+1):
        if i % 3 == 0 and i % 5 == 0:
            answer.append(i)             
        if i % 3 != 0 and i % 5 != 0:
            answer.append(i)
    return len(answer)

# Question 3: 印出所有數字
def print_number(numbers):
    summ = sum(numbers)
    return summ

# result is below~
# print(flip_one_word("amy"))
# print(flip_sentence("flipped class room is important"))
# print(delet_numbers(15))
