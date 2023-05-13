from main import find_task_dependencies,list_of_needed_tasks,find_build
import unittest


class FindTaskDependenciesTest(unittest.TestCase):
    def test_task_dependencies_test_case(self):
        tasks = [{"name": "build_blue_leprechauns", "dependencies": ["bring_purple_leprechauns"]},
                  {"name": "bring_purple_leprechauns", "dependencies": ["bring_green_leprechauns"]},
                  {"name": "bring_green_leprechauns", "dependencies": []}]
        answer = ["bring_green_leprechauns","bring_purple_leprechauns","build_blue_leprechauns"]
        find_task_dependencies(tasks,"build_blue_leprechauns")
        self.assertEqual(list_of_needed_tasks,answer)

