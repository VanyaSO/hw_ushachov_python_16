import random
arr = []

def generate_list():
    for i in range(100):
        arr.append(random.randint(1,5))
        
        
def find_min_ten(list, current_index=0, min_index=0, min_sum=float("inf")):
    
    if current_index + 10 > len(list):
        return min_index
    
    current_sum = 0
    for i in range(10):
        current_sum += list[current_index + i]
        
    if min_sum > current_sum:
        min_sum = current_sum
        min_index = current_index
        
    current_index += 10
    
    print(min_sum)
    
    return find_min_ten(list, current_index, min_index, min_sum)
        
        
    
    
    


def main():
    generate_list()
    print(find_min_ten(arr))
main()