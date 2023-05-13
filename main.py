import yaml
from docopt import docopt
import sys

if __name__ == '__main__':

    usage = f'''
    Usage:
     {sys.argv[0]} tasks
     {sys.argv[0]} builds
     {sys.argv[0]} list <list_category>
     {sys.argv[0]} get (build | task) <name>
    '''

    args = docopt(usage)

    list_of_needed_tasks = []

    with open("data/builds.yaml") as file:
        builds = yaml.load(file, Loader=yaml.FullLoader)['builds']
    with open("data/tasks.yaml") as file:
        tasks = yaml.load(file, Loader=yaml.FullLoader)['tasks']


    def task_dependencies_finder(task_name):
        for concrete_task in tasks:
            if concrete_task['name'] == task_name:
                if not concrete_task['dependencies']:
                    list_of_needed_tasks.append(concrete_task['name'])
                else:
                    for dependency_name in concrete_task['dependencies']:
                        task_dependencies_finder(dependency_name)
                    list_of_needed_tasks.append(concrete_task['name'])


    if args['tasks']:
        print("List of available tasks:")
        for task in tasks:
            print(f" {task['name']}")
    if args['builds']:
        print("List of available builds:")
        for build in builds:
            print(f" {build['name']}")
    if args['get']:
        if args['build']:
            buildExist = False
            print("Build info:")
            for build in builds:
                if build['name'] == args['<name>']:
                    buildExist = True
                    print(f" name: {build['name']}")
                    for i in build['tasks']:
                        task_dependencies_finder(i)
                    print(" tasks:")
                    for i in list_of_needed_tasks:
                        print(f"  {i}")
            if not buildExist:
                print(f"No such build, try 'python {sys.argv[0]} builds' to see list of available builds")

        if args['task']:
            taskExist = False
            print("Task info:")
            for task in tasks:
                if task['name'] == args['<name>']:
                    taskExist = True
                    print(f" name: {task['name']}\n dependencies: {','.join(task['dependencies'])}")
            if not taskExist:
                print(f"No such task, try 'python {sys.argv[0]} tasks' to see list of available tasks")
