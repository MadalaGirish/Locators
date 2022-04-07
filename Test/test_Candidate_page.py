import time
from gettext import gettext

from driver import driver
from Pages.Canditate_page import Homepage
from Pages.Login_page import login_page
from Test.Test_base import Basetest
from config.config import Testdata


class Test_Home(Basetest):
    """"Validating Home Page"""

    def test_user_details(self, ):
        """take Login Page"""
        self.loginpage = login_page(self.driver)
        homepage = self.loginpage.Login_in(Testdata.Candidate, Testdata.Password)
        homepage.home_page_title(Testdata.LoginPageTitle)

        """I am Using Boolean Value When it's Pass True else False"""
        # Verify Full-name"""
        fullname = homepage.is_display_full_name()
        assert fullname == Testdata.ExpectedValue
        print(fullname)

        # Verify email"""
        email = homepage.is_display_email()
        assert email == Testdata.ExpectedValue
        print(email)

        # Verify Phone"""
        phone = homepage.is_display_phone()
        assert phone == Testdata.ExpectedValue
        print(phone)

        # Verify Mobile"""
        mobile = homepage.is_display_mobile()
        assert mobile == Testdata.ExpectedValue
        print(mobile)

        # Verify address"""
        address = homepage.is_display_address()
        assert address == Testdata.ExpectedValue
        print(address)

        # Verify Interview name"""
        interview = homepage.is_display_interview_home()
        assert interview == Testdata.ExpectedValue
        print(interview)

        # Verify Interview-email"""
        interview_email = homepage.is_display_interview_email_home()
        assert interview_email == Testdata.ExpectedValue
        print(interview_email)

        # Verify Job-role"""
        job_role = homepage.is_display_job_role_home()
        assert job_role == Testdata.ExpectedValue
        print(job_role)

        # Verify Metting-ID"""
        meeting_id = homepage.is_display_meeting_id_home()
        assert meeting_id == Testdata.ExpectedValue
        print(meeting_id)

        # Verify-Meeting-password"""
        meeting_password = homepage.is_display_meeting_pass_home()
        assert meeting_password == Testdata.ExpectedValue
        print(meeting_password)

        # Verify-Image
        img = homepage.is_display_image()
        assert img == Testdata.ExpectedValue
        print(img)

        # verify-skills
        skill = homepage.is_display_skill()
        assert skill == Testdata.ExpectedValue
        print(skill, "Primary skills")
