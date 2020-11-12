import sys

LEN = int(sys.argv[1])

def c121(s):
    return '121' in s

def nc212(s):
    return '212' not in s

print("Start generating ...")
f = open('test-suite', 'w+')

cases = ['']
for i in range(LEN):
    new_cases = []
    for case in cases:
        for ch in ['1', '2']:
            new_case = case + ch
            status = c121(new_case) and nc212(new_case)
            f.write('{0} {1}\n'.format(new_case, status))
            new_cases.append(new_case)
    cases = new_cases
print("Done!")
