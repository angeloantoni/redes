def ip_bin(ip):
    return ''.join([f'{int(octet):08b}' for octet in ip.split('.')])

def mesma_rede(ip1, ip2, mask):

    ip1_bin = ip_bin(ip1)
    ip2_bin = ip_bin(ip2)
    
    mask_bin = '1' * mask + '0' * (32 - mask)

    rede1 = int(ip1_bin, 2) & int(mask_bin, 2)
    rede2 = int(ip2_bin, 2) & int(mask_bin, 2)
    
    return rede1 == rede2

ip1 = '192.168.1.10'
ip2 = '192.168.1.20'
mask = 24

print(mesma_rede(ip1, ip2, mask))

