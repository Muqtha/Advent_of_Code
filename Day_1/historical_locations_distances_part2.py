import bisect

#################################
#
# @Title: historical_locations_distances.
# @Author: Al-Muqthadir Ajiboye.
# @Date: December 1st, 2024.
#
# @Description:
# The Chief Historian is nowhere to be found. The Elves discover an assortment of notes
# and lists of historically significant locations! This seems to be the planning the Chief Historian was doing
# before he left. Perhaps these notes can be used to determine which locations to search?
# The historically significant locations are listed not by name but by a unique number called the location ID. To
# make sure they don't miss anything, The Historians split into two groups, each searching the office and trying to
# create their own complete list of location IDs.
# There's just one problem: by holding the two lists up side by side, it quickly becomes clear that the lists aren't
# very similar. Maybe you can help The Historians reconcile their lists?
#
# @Task:
# This time, you'll need to figure out exactly how often each number from the left list appears in the right list.
# Calculate a total similarity score by adding up each number in the left list after multiplying it by the number of
# times that number appears in the right list.
#
#################################

def solution(list_file):
    list_left, list_right = [], []
    total_distance = 0

    for each_line in list_file.readlines():
        tmp_list = each_line.split()
        bisect.insort(list_left,int(tmp_list[0]))
        bisect.insort(list_right,int(tmp_list[1]))

    for index in range(len(list_left)):
        total_distance += abs(list_left[index] - list_right[index])

    return total_distance


# Example Test Case
example = open("../files/Example_day_1.txt", "r")

# Test Case(s)
test_case = open("../files/input_day_1", "r")

output = solution(test_case)

example.close()
test_case.close()

print(output)