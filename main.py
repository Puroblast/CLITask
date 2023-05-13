import yaml
from docopt import docopt
import sys
from definitions import *

list_of_needed_tasks = []


def find_task_dependencies(tasks, task_name):
    for concrete_task in tasks:
        if concrete_task['name'] == task_name:
            if not concrete_task['dependencies']:
                list_of_needed_tasks.append(concrete_task['name'])
            else:
                for dependency_name in concrete_task['dependencies']:
                    find_task_dependencies(tasks, dependency_name)
                list_of_needed_tasks.append(concrete_task['name'])


def find_build(builds):
    build_exist = False
    print("Build info:")
    for build in builds:
        if build['name'] == args['<name>']:
            build_exist = True
            print(f" name: {build['name']}")
            for task_name in build['tasks']:
                find_task_dependencies(tasks, task_name)
            print(" tasks:")
            for task in list_of_needed_tasks:
                print(f"  {task}")
    if not build_exist:
        print(f"No such build, try 'python {sys.argv[0]} builds' to see list of available builds")


def find_task(tasks):
    task_exist = False
    print("Task info:")
    for task in tasks:
        if task['name'] == args['<name>']:
            task_exist = True
            print(f" name: {task['name']}\n dependencies: {','.join(task['dependencies'])}")
    if not task_exist:
        print(f"No such task, try 'python {sys.argv[0]} tasks' to see list of available tasks")


if __name__ == '__main__':

    with open(BUILDS_PATH) as file:
        builds = yaml.load(file, Loader=yaml.FullLoader)['builds']
    with open(TASKS_PATH) as file:
        tasks = yaml.load(file, Loader=yaml.FullLoader)['tasks']

    usage = f'''
    Usage:
     {sys.argv[0]} tasks
     {sys.argv[0]} builds
     {sys.argv[0]} list <list_category>
     {sys.argv[0]} get (build | task) <name>
    '''

    args = docopt(usage)

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
            find_build(builds)

        if args['task']:
            find_task(tasks)
