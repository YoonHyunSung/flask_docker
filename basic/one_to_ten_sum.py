#def one_to_ten_sum1():
   #example 1
#    sum = 0
    #function 조건 parametherzone과 앞에 호출이없다(example --.sum..).
 #   for i in range(1, 11):
  #      sum += i
   # print(sum)
class one_to_ten_sum(object):
    def one_to_ten_sum1(self):
        a = sum(i for i in range(1, 11))
        print(a)
        return a
    def one_to_ten_sum2(self):
        a = sum(range(1, 11))
        print(a)
        return a
#print(sum(return i for i in range(1, 11))) return omission되어있는거임.


