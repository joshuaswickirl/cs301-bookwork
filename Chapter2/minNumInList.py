def findMinNum_Quadratic(list_of_nums):
    min_num = list_of_nums[0]
    for current_num in list_of_nums:
        smallest_num = True
        for num in list_of_nums:
            if num < current_num :
                smallest_num = False
        if smallest_num:
            min_num = current_num
    return min_num
    
def findMinNum_Linear(list_of_nums):
    min_num = list_of_nums[0]
    for current_num in list_of_nums:
        if current_num < min_num:
            min_num = current_num
    return min_num


if __name__ == "__main__":
    list_of_nums = [5,4,2,1,0]
    print(findMinNum_Quadratic(list_of_nums))
    print(findMinNum_Linear(list_of_nums))