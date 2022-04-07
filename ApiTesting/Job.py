import json

import requests

from ApiTesting.config import TestdataApi


class Test_Job_list:

    def test_Get(self):
        # Send Get Request
        response = requests.get(TestdataApi.Job_list_url)
        print(response)  # result = <Response [200]>

        # Display Response Content
        print("content = ", response.content)

        # Display Response Header
        print("headers = ", response.headers)

        # Display Status Code
        print("status_code = ", response.status_code)

        # json format
        json_path = json.loads(response.text)
        print(json_path)
