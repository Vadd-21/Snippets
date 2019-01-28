import struct
import socket
import random

def bin_to_IP(ip, mask):
    base = mask&int(ip, 2)
    print(0b11111111111111111111111111111111)
    limit = mask ^ 0b11111111111111111111111111111111
    while True:
        randnum = random.randint(1, limit)
        addr = '0b'+(bin(base + randnum)[2:].zfill(32))                
        yield socket.inet_ntoa(struct.pack('!I',int(addr,2)))

def get_ip_generator(ip, mask):
    '''
    bin_to_ip(str, str)
    bin_to_ip
    '''
    ip = int(ip, 2)
    mask = int(mask, 2)
    base = int(bin(mask&ip),2)
    limit = mask ^ 0b11111111111111111111111111111111
    while True:
        randnum = random.randint(1, limit)
        addr = '0b'+(bin(base + randnum)[2:].zfill(32))                
        yield socket.inet_ntoa(struct.pack('!I',int(addr,2)))

if __name__ == "__main__":
    x = [bin(struct.unpack('!I', socket.inet_aton(str(x)+'.0.0.0'))[0]) for x in range(1, 256)]
    for i in range(len(x)):
            x[i] = '0b' + '0'*(32 - len(x[i][2:]))+str(x[i][2:])
    gen_list = []
    for i in x:
        gen_list.append(bin_to_IP(i, 0b11111111111111110000000000000000))
    for i in range(10000):
        print(next(random.choice(gen_list)))
    for gen in gen_list:
        gen.close()
    input()
