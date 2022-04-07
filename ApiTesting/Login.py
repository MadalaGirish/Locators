import requests

from ApiTesting.config import TestdataApi


class Test_Login_Api:

    def test_login(self):

        # request Post
        resp = requests.post(TestdataApi.Login_url, json=TestdataApi.payload)
        print(resp)

        # Display Response Content
        print("content = ", resp.content)

        # Display Status Code
        print("status_code = ", resp.status_code)

        code = resp.status_code
        assert code == 200, "does not match"
        print(resp.json())
        assert resp.json()['user'] == 'Test Recruiter1'
