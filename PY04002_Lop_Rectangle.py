import sys
arr = input().split()

a = int(arr[0])
b = int(arr[1])
c = arr[2]

if a <= 0 or b <= 0:
    print("INVALID")
else:
    perimeter = (a + b) * 2
    area = a * b
    color = c[:1].upper() + c[1:].lower()
    print(perimeter, area, color)
sys.exit()
if __name__ == '__main__':
    t = int(input())
    while t > 0:
        arr = input().split()
        r = Rectangle(int(arr[0]), int(arr[1]), int(arr[2]))
        print('{} {} {}'.format(r.perimeter(), r.area(), r.color()))
        t -= 1
