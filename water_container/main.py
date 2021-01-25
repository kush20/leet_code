class Solution:

    def max_area(self, height: list) -> int:
        """
          contraints: inputs and outputs. 
          exceptions thrown.
        """
        num_walls = len(height)
        current_record = 0
        for start_index, start_height in enumerate(height, 1):
            for end_index in range(num_walls - 1, start_index, -1):
                end_height = height[end_index]
                current_area = min(start_height, end_height) * (end_index - start_index + 1)
                current_record = max(current_area, current_record)
        return current_record

