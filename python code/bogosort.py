import random
  
# Sorts array a[0..n-1] using Bogo sort
def bogoSort(a):
    n = len(a)
    while not sorted(a) == a:
        random.shuffle(a)
        print(a)
  
# Driver code to test above
a = [3, 2, 4, 1, 0, 5, -2, 10]
bogoSort(a)
print("Sorted array:")
for i in range(len(a)):
    print ("%d" %a[i]),