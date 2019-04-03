#average numbers

# Ask the user to enter the numbers one at a time, putting them into a list. If the user enters 'done', then calculate and display the average. The following code demonstrates how to add an element to the end of a list.
#
# nums = []
# nums.append(5)
# print(nums)
# Below is an example input/output:
#
# > enter a number, or 'done': 5
# > enter a number, or 'done': 3
# > enter a number, or 'done': 4
# > enter a number, or 'done': done
# average: 4


nums = []
sum = 0

while True:
    num_choice = input("\nEnter an integer, or (done): ")
    if num_choice == "done":
        break
    else:
        num_choice = int(num_choice)
        sum = num_choice + sum
        nums.append(num_choice)
        print(f"You added {num_choice} to your list.")

average = sum / len(nums)

print(f"\nSum: {sum}\nCount: {len(nums)}\nAverage: {average}")
