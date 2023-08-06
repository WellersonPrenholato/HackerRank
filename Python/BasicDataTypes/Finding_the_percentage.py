if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    soma = 0
    
    for i in student_marks[query_name]:
        # print(i)
        soma =  soma + i
        # print(soma)
        resp = soma/3
        
    print(f'{resp:.2f}')
