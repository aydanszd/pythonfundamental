number = []

for i in range(5):
    k = int(input("Ədəd daxil et: "))
    number.append(k)

a = max(number)
b = min(number)
s = sum(number)
f = sum(number) / len(number)

print("Max:", a)
print("Min:", b)
print("Cəm:", s)
print("Ortalama:", f)
# This code takes 5 numbers as input from the user, stores them in a list, and then calculates and prints the maximum, minimum, sum, and average of those numbers. The max() function is used to find the largest number, the min() function is used to find the smallest number, the sum() function is used to calculate the total sum of the numbers, and the average is calculated by dividing 