

def dfs(root, checked):
    if root in checked:
        return
    
    checked.add(root)
    langs = employees[root]
    for lang in langs:
        emps = graph[lang]
        for emp in emps:
            dfs(emp, checked)


n, m = list(map(int, input().split()))
connections = [set() for i in range(n)]
employees = []
graph = [[] for i in range(m+1)]
for employee in range(n):
    languages = list(map(int, input().split()))[1:]
    for language in languages:
        graph[language].append(employee)
    employees.append(languages)
    
checked = set()
disconnected = 0
for i in range(n):
    if i in checked:
        continue
    disconnected +=1
    dfs(i, checked)
    
print(disconnected-1)
    
