def containsDuplicate(nums):
    gorulen = set()  
    for sayi in nums:
        if sayi in gorulen:
            return True  
        gorulen.add(sayi)  
    return False  
print(containsDuplicate([1, 2, 3, 4]))       # False
print(containsDuplicate([1, 2, 3, 1]))       # True
print(containsDuplicate([5, 5, 5, 5, 5]))    # True
print(containsDuplicate([]))                # False
