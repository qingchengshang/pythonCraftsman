# coding=utf-8
import re


class Count:

    def add(self):
        print("______________")
        pass


def send_shell_cmd():
    return "Response from send_shell_cmd function"


def check_cmd_response():
    response = send_shell_cmd()
    print("response: {}".format(response))
    return re.search(r"mock_send_shell_cmd", response)



