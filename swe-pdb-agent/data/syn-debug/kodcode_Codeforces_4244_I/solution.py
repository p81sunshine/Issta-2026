class FileSystem:
    def __init__(self):
        self.fs = {'': {}}

    def _get_node(self, path):
        components = path.strip('/').split('/')
        node = self.fs['']
        for comp in components:
            if comp not in node:
                node[comp] = {}
            node = node[comp]
        return node

    def mkdir(self, path):
        self._get_node(path)

    def touch(self, path):
        components = path.strip('/').split('/')
        file_name = components.pop()
        dir_path = '/' + '/'.join(components)
        dir_node = self._get_node(dir_path)
        dir_node[file_name] = {}

    def ls(self, path):
        node = self._get_node(path)
        if isinstance(node, dict):
            return sorted(node.keys())
        else:
            return [path.strip('/').split('/')[-1]]

# Function to handle the input and execute commands
def execute_commands(commands):
    fs = FileSystem()
    results = []
    for command in commands:
        operation, path = command.split()[0], command.split()[1]
        if operation == 'mkdir':
            fs.mkdir(path)
        elif operation == 'touch':
            fs.touch(path)
        elif operation == 'ls':
            results.append(' '.join(fs.ls(path)))
    return results

# Input Example
commands = [
    "mkdir /a/b/c",
    "touch /a/b/d.txt",
    "ls /a/b",
    "touch /a/b/c/e.txt",
    "ls /a/b/c",
    "ls /a"
]

# Executing commands and printing results
output = execute_commands(commands)
for line in output:
    print(line)