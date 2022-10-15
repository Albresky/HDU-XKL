#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Author  : Loot at the stars
# @Time    : 2022/10/15 13:07
# @File    : des.py
# @Software: PyCharm

"""
<str>data: 待加密字符串
<str>firstKey: 第一个密钥
<str>secondKey: 第二个密钥
<str>thirdKey: 第三个密钥
"""


def strEnc(data, firstKey, secondKey, thirdKey):
    leng = len(data)
    encData = ""
    firstKeyBt = None
    secondKeyBt = None
    thirdKeyBt = None
    firstLength = None
    secondLength = None
    thirdLength = None
    if not firstKey is None and firstKey != "":
        firstKeyBt = getKeyBytes(firstKey)
        firstLength = len(firstKeyBt)
    if not secondKey is None and secondKey != "":
        secondKeyBt = getKeyBytes(secondKey)
        secondLength = len(secondKeyBt)
    if not thirdKey is None and thirdKey != "":
        thirdKeyBt = getKeyBytes(thirdKey)
        thirdLength = len(thirdKeyBt)

    if leng > 0:
        if leng < 4:
            bt = strToBt(data)
            encByte = None
            if not firstKey is None and firstKey != "" and not secondKey is None and secondKey != "" and not thirdKey is None and thirdKey != "":
                tempBt = bt
                for x in range(firstLength):
                    tempBt = enc(tempBt, firstKeyBt[x])
                for y in range(secondLength):
                    tempBt = enc(tempBt, secondKeyBt[y])
                for z in range(thirdLength):
                    tempBt = enc(tempBt, thirdKeyBt[z])
                encByte = tempBt
            elif not firstKey is None and firstKey != "" and not secondKey is None and secondKey != "":
                tempBt = bt
                for x in range(firstLength):
                    tempBt = enc(tempBt, firstKeyBt[x])
                for y in range(secondLength):
                    tempBt = enc(tempBt, secondKeyBt[y])
                encByte = tempBt
            elif not firstKey is None and firstKey != "":
                tempBt = bt
                for x in range(firstLength):
                    tempBt = enc(tempBt, firstKeyBt[x])
                encByte = tempBt
            encData = bt64ToHex(encByte)
        else:
            _iterator = int(leng / 4)
            _remainder = leng % 4
            for i in range(_iterator):
                tempData = data[i * 4:i * 4 + 4]
                tempByte = strToBt(tempData)
                encByte = None
                if not firstKey is None and firstKey != "" and not secondKey is None and secondKey != "" and not thirdKey is None and thirdKey != "":
                    tempBt = tempByte
                    for x in range(firstLength):
                        tempBt = enc(tempBt, firstKeyBt[x])
                    for y in range(secondLength):
                        tempBt = enc(tempBt, secondKeyBt[y])
                    for z in range(thirdLength):
                        tempBt = enc(tempBt, thirdKeyBt[z])
                    encByte = tempBt
                elif not firstKey is None and firstKey != "" and not secondKey is None and secondKey != "":
                    tempBt = tempByte
                    for x in range(firstLength):
                        tempBt = enc(tempBt, firstKeyBt[x])
                    for y in range(secondLength):
                        tempBt = enc(tempBt, secondKeyBt[y])
                    encByte = tempBt
                elif not firstKey is None and firstKey != "":
                    tempBt = tempByte
                    for x in range(firstLength):
                        tempBt = enc(tempBt, firstKeyBt[x])
                    encByte = tempBt
                encData += bt64ToHex(encByte)
            if _remainder > 0:
                remainderData = data[_iterator * 4:leng]
                tempByte = strToBt(remainderData)
                encByte = None
                if not firstKey is None and firstKey != "" and not secondKey is None and secondKey != "" and not thirdKey is None and thirdKey != "":
                    tempBt = tempByte
                    for x in range(firstLength):
                        tempBt = enc(tempBt, firstKeyBt[x])
                    for y in range(secondLength):
                        tempBt = enc(tempBt, secondKeyBt[y])
                    for z in range(thirdLength):
                        tempBt = enc(tempBt, thirdKeyBt[z])
                    encByte = tempBt
                elif not firstKey is None and firstKey != "" and not secondKey is None and secondKey != "":
                    tempBt = tempByte
                    for x in range(firstLength):
                        tempBt = enc(tempBt, firstKeyBt[x])
                    for y in range(secondLength):
                        tempBt = enc(tempBt, secondKeyBt[y])
                    encByte = tempBt
                elif not firstKey is None and firstKey != "":
                    tempBt = tempByte
                    for x in range(firstLength):
                        tempBt = enc(tempBt, firstKeyBt[x])
                    encByte = tempBt
                encData += bt64ToHex(encByte)
    return encData


def getKeyBytes(_key):
    keyBytes = []
    leng = len(_key)
    iterator = int(leng / 4)
    for i in range(iterator):
        keyBytes.append(strToBt(_key[i * 4:i * 4 + 4]))
    if leng % 4 > 0:
        keyBytes.append(strToBt(_key[iterator * 4:leng]))
    return keyBytes


def strToBt(_str):
    result = []
    for c in _str:
        bits = bin(ord(c))[2:]
        bits = '0000000000000000'[len(bits):] + bits
        result.extend([int(b) for b in bits])
    c = '0' * 16 * (4 - len(_str))
    result.extend([int(c) for c in c])
    return result


def enc(dataByte, keyByte):
    keys = generateKeys(keyByte)
    ipByte = initPermute(dataByte)
    ipLeft = [0] * 32
    ipRight = [0] * 32
    tempLeft = [0] * 32
    for k in range(32):
        ipLeft[k] = ipByte[k]
        ipRight[k] = ipByte[32 + k]
    for i in range(16):
        for j in range(32):
            tempLeft[j] = ipLeft[j]
            ipLeft[j] = ipRight[j]
        _key = [0] * 48
        for m in range(48):
            _key[m] = keys[i][m]
        tempRight = xor(pPermute(sBoxPermute(xor(expandPermute(ipRight), _key))), tempLeft)
        for n in range(32):
            ipRight[n] = tempRight[n]
    finalData = [0] * 64
    for i in range(32):
        finalData[i] = ipRight[i]
        finalData[32 + i] = ipLeft[i]
    return finallyPermute(finalData)


def generateKeys(keyByte):
    _key = [0] * 56
    keys = []
    for i in range(16):
        keys.append([0] * 48)
    loop = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]

    for i in range(7):
        k = 7
        for j in range(8):
            _key[i * 8 + j] = keyByte[8 * k + i]
            k -= 1

    for i in range(16):
        _tempLeft = 0
        _tempRight = 0
        for j in range(loop[i]):
            _tempLeft = _key[0]
            _tempRight = _key[28]
            for k in range(27):
                _key[k] = _key[k + 1]
                _key[28 + k] = _key[29 + k]
            _key[27] = _tempLeft
            _key[55] = _tempRight
        tempKey = [0] * 48
        keyIndex = [13, 16, 10, 23, 0, 4, 2, 27, 14, 5, 20, 9, 22, 18, 11, 3, 25, 7, 15, 6, 26, 19, 12, 1, 40, 51, 30,
                    36, 46, 54, 29, 39, 50, 44, 32, 47, 43, 48, 38, 55, 33, 52, 45, 41, 49, 35, 28, 31]
        for o in range(48):
            tempKey[o] = _key[keyIndex[o]]
        for m in range(48):
            keys[i][m] = tempKey[m]
    return keys


# convert byte 64 to hex string
def bt64ToHex(byteData):
    hexChar = "0123456789ABCDEF"
    _hex = ""
    weight = [8, 4, 2, 1]
    for i in range(16):
        bt = 0
        for j in range(4):
            bt += byteData[i * 4 + j] * weight[j]
        _hex += hexChar[bt]
    return _hex


def initPermute(originalData):
    ipByte = [0] * 64
    m = 1
    n = 0
    for i in range(4):
        k = 0
        for j in range(7, -1, -1):
            ipByte[i * 8 + k] = originalData[j * 8 + m]
            ipByte[i * 8 + k + 32] = originalData[j * 8 + n]
            k += 1
        m += 2
        n += 2
    return ipByte


def expandPermute(rightData):
    epByte = [0] * 48
    for i in range(8):
        if i == 0:
            epByte[i * 6 + 0] = rightData[31]
        else:
            epByte[i * 6 + 0] = rightData[i * 4 - 1]
        epByte[i * 6 + 1] = rightData[i * 4 + 0]
        epByte[i * 6 + 2] = rightData[i * 4 + 1]
        epByte[i * 6 + 3] = rightData[i * 4 + 2]
        epByte[i * 6 + 4] = rightData[i * 4 + 3]
        if i == 7:
            epByte[i * 6 + 5] = rightData[0]
        else:
            epByte[i * 6 + 5] = rightData[i * 4 + 4]
    return epByte


def xor(byteOne, byteTwo):
    xorByte = [0] * len(byteOne)
    for i in range(len(byteOne)):
        xorByte[i] = byteOne[i] ^ byteTwo[i]
    return xorByte


def sBoxPermute(expandByte):
    sBoxByte = [0] * 32
    _binary = ""
    s1 = [
        [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
        [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
        [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
        [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]]

    # Table - s2
    s2 = [
        [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
        [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
        [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
        [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]]

    # Table - s3
    s3 = [
        [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
        [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
        [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
        [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]]

    # Table - s4 
    s4 = [
        [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
        [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
        [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
        [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]]

    # Table - s5
    s5 = [
        [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
        [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
        [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
        [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]]

    # Table - s6
    s6 = [
        [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
        [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
        [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
        [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]]

    # Table - s7
    s7 = [
        [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
        [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
        [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
        [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]]

    # Table - s8
    s8 = [
        [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
        [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
        [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
        [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]]

    tables = [s1, s2, s3, s4, s5, s6, s7, s8]

    for m in range(8):
        i = expandByte[m * 6 + 0] * 2 + expandByte[m * 6 + 5]
        j = expandByte[m * 6 + 1] * 2 * 2 * 2 + expandByte[m * 6 + 2] * 2 * 2 + expandByte[m * 6 + 3] * 2 + expandByte[
            m * 6 + 4]
        _binary = getBoxBinary(tables[m][i][j])
        sBoxByte[m * 4 + 0] = int(_binary[0])
        sBoxByte[m * 4 + 1] = int(_binary[1])
        sBoxByte[m * 4 + 2] = int(_binary[2])
        sBoxByte[m * 4 + 3] = int(_binary[3])
    return sBoxByte


def getBoxBinary(i):
    hexBin = ["0000", "0001", "0010", "0011", "0100", "0101", "0110", "0111", "1000", "1001", "1010", "1011", "1100",
              "1101", "1110", "1111"]
    return hexBin[i]


def pPermute(sBoxByte):
    pBoxPermute = [0] * 32
    sBoxByteIndex = [15, 6, 19, 20, 28, 11, 27, 16, 0, 14, 22, 25, 4, 17, 30, 9, 1, 7, 23, 13, 31, 26, 2, 8, 18, 12, 29,
                     5, 21, 10, 3, 24]
    for i in range(32):
        pBoxPermute[i] = sBoxByte[sBoxByteIndex[i]]
    return pBoxPermute


def finallyPermute(endByte):
    fpByte = [0] * 64
    endByteIndex = [39, 7, 47, 15, 55, 23, 63, 31, 38, 6, 46, 14, 54, 22, 62, 30, 37, 5, 45, 13, 53, 21, 61, 29, 36, 4,
                    44, 12, 52, 20, 60, 28, 35, 3, 43, 11, 51, 19, 59, 27, 34, 2, 42, 10, 50, 18, 58, 26, 33, 1, 41, 9,
                    49, 17, 57, 25, 32, 0, 40, 8, 48, 16, 56, 24]
    for m in range(64):
        fpByte[m] = endByte[endByteIndex[m]]
    return fpByte


if __name__ == "__main__":
    """
    key：待加密字符串
    right_answer：（先验）正确的加密后的字符串
    this_answer：（待验证）本算法加密后的字符串
    """
    key = '20041423ThisIsHDULT-5912-ap7HPHblcWOCOrO74xgaUQK9g31wyf-cas'
    right_answer = '09E3E584C903479D7384D195E28E2218451B9BBCC6999227E51D5036CDEEA86B662F46605CE5E1DE8BD88FFE8425C5B58CAA5B079FAC8EA0BEC285F1C506F6A043A5F3021EDA8B345C284532082FDEE1EFDB8212C7438972EFD9FBC19F72B837B547ABBC7FC188D4F68FA1A0067675C7369041DED879FBF3'
    this_answer = strEnc(key, '1', '2', '3')

    print("[Y]{}".format(right_answer))
    print("[N]{}".format(this_answer))

    if this_answer == right_answer:
        print('Congratulations! You are right!')
    else:
        print('Sorry! You are wrong!')
