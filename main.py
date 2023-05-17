command_dict = {'W': 'write',
                'R': 'read',
                'X': 'execute'
                }
available_files = {}
operation_with_file = {}
result = ''

n = int(input('Enter quantity of files: '))
for i in range(1, n + 1):
    file_list = input('Enter file name and commands (W, R, X): ').split(" ")
    file_list = [command_dict.get(item, item) for item in file_list]
    new_file = {file_list[0]: [file_list[j] for j in range(1, len(file_list))]}
    available_files.update(new_file)

m = int(input('Enter quantity of operations: '))
for k in range(1, m + 1):
    operation_list = input('Enter operation (read, write, execute) and file name: ').split(" ")
    if operation_list[0] in available_files.get(operation_list[1]):
        result += 'OK\n'
    else:
        result += 'Access Denied\n'
print('\n' + result)
