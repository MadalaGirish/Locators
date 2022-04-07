import requests
import json
import jsonpath
from ApiTesting.config import TestdataApi


class Test_user_list:

    def test_Get(self):
        # Send Get Request
        response = requests.get(TestdataApi.user_list_url)
        print(response)  # result = <Response [200]>

        # Display Response Content
        print("content = ", response.content)

        # Display Response Header
        print("headers = ", response.headers)

        # Display Status Code
        code = response.status_code
        assert code == 200, "does not match"
        print("status_code = ", response.status_code)

