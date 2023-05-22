import bchlib
import math
import os
import random

def get_degree_field(data_bits, t):
    min_mt = math.log2(t * 4)
    min_mb = math.log2(data_bits + 1)
    if(min_mt > min_mb):
        m = min_mt
    else:
        m = min_mb
    
    done = 0
    while (~done and m <= 15):
        k = ((1 << m) - 1)

    return math.ceil(m)

def ByteArrayToString(byteArray):
    return "0x" + (''.join(format(x, '02X') for x in byteArray))

def StringToByteArray(hexString):
    byte_array = bytearray.fromhex(hexString)
    return byte_array

def bitflip(packet):
    byte_num = random.randint(0, len(packet) - 1)
    bit_num = random.randint(0, 7)
    packet[byte_num] ^= (1 << bit_num)

def reverse(byteArray):
    reverse_array = bytearray([0] * len(byteArray))
    for i in range(len(byteArray)):
        reverse_array[i] = int('{:08b}'.format(byteArray[len(byteArray) - i - 1])[::-1], 2) 
    return reverse_array
# range form 5 to 15
prim_poly = [0x13, 0x25, 0x43, 0x83, 0x11d, 0x211, 0x409, 0x805, 0x1053, 0x201b, 0x402b, 0x8003]

# create a bch object
BCH_DEGREE_FIELD = 7
BCH_BITS = 6
DATA_BITS = 64
BCH_POLYNOMIAL = prim_poly[BCH_DEGREE_FIELD - 4]

bch = bchlib.BCH(BCH_POLYNOMIAL, BCH_BITS)
print("GF(2^m), m = ", bch.m)
print("Block length, n = ", bch.n)
print("Error correction capability in bits, t = ", bch.t)
print("ECC bits = ", bch.ecc_bits)
print("Data bits, k = ", bch.n - bch.ecc_bits)

# hex_string = "12153524"

# data = StringToByteArray(hex_string)

# reverse_data = reverse(data)
# print(reverse_data)
# print("\nData in:", ByteArrayToString(data))

# ecc = bch.encode(reverse_data)
# print("\nECC:", ByteArrayToString(ecc))

# packet = reverse_data + ecc
# print(ByteArrayToString(packet))

# # make BCH_BITS errors
# for _ in range(BCH_BITS):
#     bitflip(packet)

# # de-packetize
# data, ecc = packet[:-bch.ecc_bytes], packet[-bch.ecc_bytes:]

# print(bch.decode_inplace( data, ecc))
# print(ByteArrayToString(data))
# r = bytearray([0x24, 0xec, 0xa8, 0x48]) + bytearray([0x0c, 0x2d, 0xc0])
# print(ByteArrayToString(reverse(r)))

data = bytearray([0x24, 0xa8, 0xa8, 0x48, 0x99, 0x7e, 0x91, 0x43])

for a in data:
    # print(format(a, '08h') )
    print(hex(a))
print()
ecc = bytearray([0xfa, 0x74, 0x56, 0xe2, 0xfc, 0x00])
print(bch.decode_inplace(data, ecc))
# print(ByteArrayToString(data))
# print(ByteArrayToString(ecc))

syn = bch.syndromes

for a in syn:
    # print(format(a, '08h') )
    print(hex(a))
print(syn)


