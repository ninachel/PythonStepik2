import os


result = []
with open('result.txt', 'a') as f:
    for current_dir, dirs, files in os.walk('main'):
        if list(filter(lambda x: x.endswith('.py'), files)):
            result.append(current_dir)
    f.write('\n'.join(sorted(result)))
