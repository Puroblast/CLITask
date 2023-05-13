# CLITask - CLI creation task for test case

## CLI available commands:
  ### tasks
  check all available tasks in current tasks.yaml file
  ### builds
  check all available builds in current builds.yaml file
  ### list <list_category>
  check names of available builds/tasks
  ### get (build | task) \<name>
  check concrete build with all dependent tasks that it have, or check concrete task

## CLI usage example through terminal:
 ### to get all tasks :
 python main.py tasks
 ### to get all builds:
 python main.py builds
 ### to get all build/tasks names:
 python main.py list builds<br>
 python main.py list tasks
 ### to get concrete build/task:
 python main.py get build #BUILDNAME<br>
 python main.py get task #TASKNAME
 
 ## CLI tests:
  ### to run all tests:
  python -m unittest tests\test.py
  ### to run single test:
  python -m unittest tests.#TESTFILENAME.#TESTCLASSNAME.#TESTCASENAME
