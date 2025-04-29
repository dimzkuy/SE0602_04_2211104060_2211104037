import math

def decode(chrom):
    def bin_to_real(bits):
        num = int(bits, 2)
        return -10 + (20 * num) / (2**16 - 1)
    return bin_to_real(chrom[:16]), bin_to_real(chrom[16:])

def fitness(x1, x2):
    try:
        term = math.sin(x1) * math.cos(x2) * math.tan(x1 + x2)
        expo = (3/4) * math.exp(1 - math.sqrt(x1**2))
        return - (term + expo)
    except:
        return float('inf')
