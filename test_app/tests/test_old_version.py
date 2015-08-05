from __future__ import unicode_literals

from selenium.common.exceptions import NoSuchElementException

from .helpers import SeleniumTestCase


class OldVersionTest(SeleniumTestCase):

    def test_old_version_lare(self):
        self.browser_get_reverse('about')
        self.assert_title('about-title')
        self.assert_content('about-content')
        old_version_link = self.browser.find_element_by_css_selector('#old-version-link')
        old_version_link.click()

        self.wait.until(lambda browser: browser.title == 'index-title')
        self.assert_title('index-title')
        self.assert_content('index-content')

        self.assert_body_attr('lare-success', None)
        self.assert_body_attr('lare-done', None)
