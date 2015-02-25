data = b'\x00\x124V\x00x\x90\xab\x00\xcd\xef\x01\x00#\x004'

print(int.from_bytes(data, 'little'))
print(int.from_bytes(data, 'big'))

import struct
hi, lo = struct.unpack('>QQ', data)
print(hi, lo)
print((hi << 64) + lo)

x = 523 ** 23
print(x)
nbytes, rem = divmod(x.bit_length(), 8)
if rem:
    nbytes += 1
print(x.to_bytes(nbytes, 'little'))
