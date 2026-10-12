class Solution:
    def trap(self, height: List[int]) -> int:
        
        left_max_arr = [0] * len(height)
        left_max = 0
        for i in range(0, len(height)):
            left_max_arr[i] = left_max
            left_max = max(height[i], left_max)
            
        right_max_arr = [0] * len(height)
        right_max = 0
        for i in range(len(height)-1, -1, -1):
            right_max_arr[i] = right_max 
            right_max = max(height[i], right_max)
        
        total_water = 0
        for i in range(0, len(height)):
            rain_water = min(left_max_arr[i], right_max_arr[i]) - height[i]
            if rain_water < 0:
                rain_water = 0
            
            total_water += rain_water

        return total_water