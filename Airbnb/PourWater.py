class PourWater:
    def pourWater(self, heights, water, location):
        waters = [0] * len(heights)
        pourLocation = 0

        while water > 0:
            left = location - 1
            while left >= 0:
                if heights[left] + waters[left] > heights[left + 1] + waters[left + 1]:
                    break
                left -= 1
            if heights[left + 1] + waters[left + 1] < heights[location] + waters[location]:
                pourLocation = left + 1
                waters[pourLocation] += 1
                water -= 1
                continue

            right = location + 1
            while right < len(heights):
                if heights[right] + waters[right] > heights[right - 1] + waters[right - 1]:
                    break
                right += 1
            if heights[right - 1] + waters[right - 1] < heights[location] + waters[location]:
                pourLocation = right - 1
                waters[pourLocation] += 1
                water -= 1
                continue

            pourLocation = location
            waters[pourLocation] += 1
            water -= 1

        self.print(heights, waters)

    def print(self, heights, waters):
        n = len(heights)

        maxHeight = 0
        for i in range(n):
            maxHeight = max(maxHeight, heights[i] + waters[i])

        for height in range(maxHeight, -1, -1):
            for i in range(n):
                if height <= heights[i]:
                    print("+", end="")
                elif height > heights[i] and height <= heights[i] + waters[i]:
                    print("W", end="")
                else:
                    print(" ", end="")
            print()
        print()


# Test the code
pw = PourWater()
heights = [5, 4, 2, 1, 2, 3, 2, 1, 0, 1, 2, 4]
for i in range(1, 10):
    pw.pourWater(heights, i, 5)
