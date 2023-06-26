
class Solution:
    def ipToCIDR(self, ip: str, n: int):
        def ipToInt(ip: str) -> int:
            parts = ip.split('.')
            return (int(parts[0]) << 24) + (int(parts[1]) << 16) + (int(parts[2]) << 8) + int(parts[3])

        def intToIP(num: int) -> str:
            return '.'.join([str((num >> 24) & 255), str((num >> 16) & 255), str((num >> 8) & 255), str(num & 255)])

        start = ipToInt(ip)
        result = []

        while n > 0:
            mask = max(33 - (start & -start).bit_length(), 33 - n.bit_length())
            result.append(intToIP(start) + '/' + str(mask))
            start += 1 << (32 - mask)
            n -= 1 << (32 - mask)

        return result
                
def main():
    solution = Solution()
    optput = solution.ipToCIDR("255.0.0.7",10)
    print("output:", optput)

if __name__ == "__main__":
    main()
