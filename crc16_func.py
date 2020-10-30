from binascii import unhexlify
from crcmod import mkCrcFun


# CRC16/CCITT
def crc16_ccitt(s):
    crc16 = mkCrcFun(0x11021, rev=True, initCrc=0x0000, xorOut=0x0000)
    return get_crc_value(s, crc16)


# CRC16/CCITT-FALSE
def crc16_ccitt_false(s):
    crc16 = mkCrcFun(0x11021, rev=False, initCrc=0xFFFF, xorOut=0x0000)
    return get_crc_value(s, crc16)


# CRC16/MODBUS
def crc16_modbus(s):
    crc16 = mkCrcFun(0x18005, rev=True, initCrc=0xFFFF, xorOut=0x0000)
    return get_crc_value(s, crc16)


# CRC16/XMODEM
def crc16_xmodem(s):
    crc16 = mkCrcFun(0x11021, rev=False, initCrc=0x0000, xorOut=0x0000)
    return get_crc_value(s, crc16)


# common func
def get_crc_value(s, crc16):
    data = s.replace(' ', '')
    crc_out = hex(crc16(unhexlify(data))).upper()
    str_list = list(crc_out)
    if len(str_list) == 5:
        str_list.insert(2, '0')  # 位数不足补0
    crc_data = ''.join(str_list[2:])
    return crc_data[:2] + ' ' + crc_data[2:]


if __name__ == '__main__':
    s1 = crc16_ccitt("6001")
    s2 = crc16_ccitt_false("6001")
    s3 = crc16_modbus("6001")
    s4 = crc16_xmodem("6001")
    print('crc16_ccitt: ' + s1)
    print('crc16_ccitt_false: ' + s2)
    print('crc16_modbus: ' + s3)
    print('crc16_xmodem: ' + s4)
