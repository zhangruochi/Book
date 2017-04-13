import numpy as np

np.random.seed(10)
cake_size_list = [np.random.randint(100) for x in range(10)]
print(cake_size_list)


def main(cake_size_list):
    result = []
    while len(cake_size_list) != 0:
     
        max_index = cake_size_list.index(max(cake_size_list))
        if max_index != len(cake_size_list):
            front_list = cake_size_list[:max_index+1]
            front_list.reverse()
            cake_size_list = front_list + cake_size_list[max_index+1:]
            cake_size_list.reverse()

        result.insert(0,cake_size_list.pop())
    print(result)    

        


if __name__ == '__main__':
    main(cake_size_list)        







