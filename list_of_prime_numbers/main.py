
def _is_prime(number):
    if(number ==0):
        return False
    if (number == 1):
        return False
    if (number == 2):
        return True
    for i in range(2, number):
        if (number % i == 0):
            return False
    return True
    
#print(_is_prime(23)) #prime
#print(_is_prime(26)) #not prime
#print(_is_prime(45)) #not prime
#print(_is_prime(73)) #prime
#print(_is_prime(5))  #prime
#print(_is_prime(2))  #prime

def list_of_prime_numbers(max_number):
    arr = []
    
    for i in range(2, max_number + 1):
        if(_is_prime(i)):
            arr.append(i)
            
        
    return arr
  
    
#list_of_prime_numbers(100)
#list_of_prime_numbers(59)

# =================== #
# ====== Tests ====== #
# =================== #

# Test: `is_prime`


def test_big_number_prime_true():
    assert _is_prime(19) is True


def test_big_number_prime_false():
    assert _is_prime(20) is False


def test_two_prime():
    assert _is_prime(2) is True


def test_three_prime():
    assert _is_prime(3) is True


def test_four_prime():
    assert _is_prime(4) is False


# Test: `list_of_prime_numbers`

def test_big_number_list():
    assert list_of_prime_numbers(19) == [2, 3, 5, 7, 11, 13, 17, 19]


def test_list_one():
    assert list_of_prime_numbers(2) == [2]


def test_list_zero():
    assert list_of_prime_numbers(0) == []
    
#test_big_number_prime_true() 
#test_big_number_list()

