even_count = 0  # ������� ������ �����

# ��������� 10 ����� � ��������� ������ �� ��������
for i in range(10):
    num = int(input())
    if num % 2 == 0:
        even_count += 1

# ���� ���������� ������ ����� ����� 10, �� ��� ����� ������, ����� - ���
if even_count == 10:
    print("YES")
else:
    print("NO")
    
