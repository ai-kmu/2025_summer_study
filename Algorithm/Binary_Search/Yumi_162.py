class Solution(object):
    def findPeakElement(self, nums):
        peaks = {}

        for i in range(1, len(nums) - 1):
            if (nums[i] > nums[i-1]) and (nums[i] > nums[i+1]):
                peaks[nums[i]] = i
        if (len(nums) > 1):
            if (nums[0] > nums[1]) :
                peaks[nums[0]] = 0
            if (nums[len(nums)-1] > nums[len(nums)-2]) :
                peaks[nums[len(nums)-1]] = len(nums)-1
        else :
            return 0

        max_key = max(peaks, key=peaks.get)
        return peaks[max_key]

        
