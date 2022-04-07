import json
import requests
import jsonpath

from ApiTesting.config import TestdataApi

class Test_InterviewsById_list:

    def test_Get(self):

        # Send Get Request
        response = requests.get(TestdataApi.interview_ById_url)
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

        # fetch value using json path



