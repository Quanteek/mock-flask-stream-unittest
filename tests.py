import json
import subprocess
import time
import unittest

import requests


class FlaskTestCase(unittest.TestCase):

    def setUp(self):
        self.process = subprocess.Popen(["python", "main.py"])
        time.sleep(2)

    def tearDown(self) -> None:
        self.process.terminate()

    def test_object_list(self):
        obj_list = []
        with requests.get("http://0.0.0.0:5000/object_list", stream=True) as stream:
            for data in stream.iter_lines():
                obj = json.loads(data)
                obj_list.append(obj)
        self.assertListEqual(obj_list, [{"id": "0", "version": "0"},
                                        {"id": "1", "version": "0"},
                                        {"id": "2", "version": "0"},
                                        {"id": "3", "version": "0"},
                                        {"id": "4", "version": "0"}])


if __name__ == '__main__':
    unittest.main()
