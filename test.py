import requests

with open('cookies.txt', 'r') as file:
    f = file.readlines()

cookies = {}
for line in f:
    key, value = line.split()
    cookies[key] = value

print(cookies)

test = []
for line in f:
    test.append(line.split())

print(test)


# r = requests.get('https://www.furaffinity.net/user/j.a.r.v.i.s.', cookies=cookies)
#
# with open('file.html', 'w') as f:
#     f.write(r.text)