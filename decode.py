import random

def char_arr(str_input):
    """
        This function converts an array of ASCII integers to their corresponding characters \n
        Returns an array of characters 
    """
    ret = []
    for char in str_input:
        ret.append(chr(char))
    return ret

def srand_sub_for_ascii_arr(arr,seed):
    """
        Takes the seed and uses the inbuilt random libraray and gives the original ASCII code
    """
    random.seed(seed)
    sub_val = random.randint(1,512)
    ret = []
    for c in arr:
        ret.append(int(c)-sub_val)
    return ret

def arr_str(arr):
    """
        Uses a array of values and returns a string with all values added \n
        Example : [1,3,"6"] -> "136"
    """
    ret=""
    for val in arr:
        ret+=str(val)
    return ret

def ascii_3digit_int_arr(string_input):
    """
        Takes the encoded string and returns an array of integers from them of 3 characters length \n
        Example : \n
        "234001567" -> [234,1,567]
    """
    x = 0
    ret = []
    while x < len(string_input):
        ret.append(int(string_input[x:(x+3)]))
        x+=3
    return ret


def decode(string_input):
    """
        A simple decoding function that decodes a string of numbers to a readable cleartext \n
        Can only be decode results from its sister encodimg function \n
        Returns a string of alphanumeric text which is usually same to the original message
    """
    seed_val=int(string_input[:5])
    enc_string = string_input[5:]
    ascii_arr_int = ascii_3digit_int_arr(enc_string)
    ascii_arr = srand_sub_for_ascii_arr(ascii_arr_int,seed_val)
    char_array = char_arr(ascii_arr)
    ret = arr_str(char_array)

    return ret

if __name__ == "__main__":
    val = input("-")
    print(decode(val))
