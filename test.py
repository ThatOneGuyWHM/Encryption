import encode , decode

str_in = input("-")
enc_str = encode.encode(str_in)
print("Encoded : \n {0}".format(enc_str))

dec_str = decode.decode(enc_str)
print("Decoded : \n {0}".format(dec_str))