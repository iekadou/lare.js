from __future__ import unicode_literals

from .helpers import SeleniumTestCase


class NoLareResponseTest(SeleniumTestCase):

    def test_no_lare_response(self):
        self.browser_get_reverse('index')
        self.assert_title('index-title')
        self.assert_content('index-content')
        self.assert_body_attr('lare-done', None)

        # lare request - depth 1
        about_link = self.browser.find_element_by_css_selector('#about-link')
        about_link.click()

        self.wait.until(lambda browser: browser.title == 'about-title')
        self.assert_title('about-title')
        self.assert_content('about-content')
        self.assert_body_attr('lare-done', 'true')

        self.reset_body_attrs()
        self.assert_body_attr('lare-done', None)

        # no-lare-response request - returns full page markup
        no_lare_response_link = self.browser.find_element_by_css_selector('#no-lare-response-link')
        no_lare_response_link.click()

        self.wait.until(lambda browser: browser.title == 'no-lare-response-title')
        self.assert_title('no-lare-response-title')
        self.assert_content('no-lare-response-content')
        self.assert_body_attr('lare-done', None)

        # back should trigger a full request cause namespace and blocks can't be reconstructed after a full return
        # issue: #17
        self.browser_go_back()

        self.wait.until(lambda browser: browser.title == 'about-title')
        self.assert_title('about-title')
        self.assert_content('about-content')
        self.assert_body_attr('lare-done', None)
