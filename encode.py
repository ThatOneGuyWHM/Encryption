import random

def char_arr(str_input):
    """
        This function converts a string into an array of integers which corresponds to the ASCII character set 
    """
    ret = []
    for char in str_input:
        ret.append(ord(char))
    return ret

def ascii_3digit_string(arr):
    """
        This function converts ASCII integer codes into 3 character strings \n
        Example : \n
        32 -> "032" \n
        1  -> "001"
    """
    ret = []
    for num in arr:
        temp = str(num)
        if len(temp) == 3:
            pass
        elif len(temp) == 2:
            temp = "0"+temp
        elif len(temp) == 1:
            temp = "00"+temp
        
        ret.append(temp)

    return ret

def srand_add_for_ascii_arr(arr,seed):
    """
        Using the inbuilt random library the function takes a seed to produce random values which are added to the ASCII value array
    """
    random.seed(seed)
    add_val = random.randint(1,512)
    for i in range(len(arr)):
        arr[i]=arr[i]+add_val
    return arr

def arr_str(arr):
    """
        Uses a array of values and returns a string with all values added \n
        Example : [1,3,"6"] -> "136"
    """
    ret=""
    for val in arr:
        ret+=str(val)
    return ret

def encode(string_input):
    """
        A simple encoding function that uses basic random functions to code ASCII characters \n
        Can only be decoded by its sister function decode \n
        Returns a string which has only numeric characters with a minimum length of 8 characters
    """

    char_array = char_arr(string_input)
    seed_num = random.randint(10000,99999)
    enc_char_array = srand_add_for_ascii_arr(char_array,seed_num)
    digit3 = ascii_3digit_string(enc_char_array)
    ret_str_raw = arr_str(digit3)
    ret_str = (str(seed_num)) + ret_str_raw

    return ret_str

if __name__ == "__main__":
    val = input("-")
    print(encode(val))