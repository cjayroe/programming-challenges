def longestPeak(array):
    peak_start_index = 0
    peak_direction = ""
    longest_peak = 0

    for index, number in enumerate(array):
        if index > 0:
            previous = array[index - 1]

            if previous < number and peak_direction == "down":
                peak_direction = ""
                longest_peak = max(longest_peak, index - peak_start_index)
                peak_start_index = index - 1

            if previous < number and not peak_direction:
                peak_direction = "up"
                continue

            if previous < number and peak_direction == "up":
                continue

            if previous > number and peak_direction == "up":
                peak_direction = "down"
                longest_peak = max(longest_peak, index - peak_start_index + 1)
                continue

            if previous > number and peak_direction == "down":
                longest_peak = max(longest_peak, index - peak_start_index + 1)
                continue


            peak_direction = ""
            peak_start_index = index

    return longest_peak
