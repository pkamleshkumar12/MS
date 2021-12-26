
if __name__ == '__main__':
    a = 10
    b = 4

    # 1010
    # 0100
    print("a & b", a & b) # 0000
    print("a | b =", a | b)  # 1110
    # Bitwise NOTing any number x yields -(x + 1). For example, ~10 yields -11.
    print("~a =", ~a)

    # print bitwise XOR operation
    # The bitwise XOR operator (^) returns a 1 in each bit position for which the corresponding bits of either
    # but not both operands are 1s.
    print("a ^ b =", a ^ b)

    x = 10 # 1010
    y = 3  # 0011
    carry = x & y
    print("carry = ", carry)
    x = x ^ y
    print("x = ", x)
