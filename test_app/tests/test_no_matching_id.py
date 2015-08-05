from __future__ import unicode_literals

from selenium.common.exceptions import NoSuchElementException

from .helpers import SeleniumTestCase


class LareNoMatchingIDTest(SeleniumTestCase):

    def test_no_matching_id_lare_request(self):
        self.browser_get_reverse('index')
        self.assert_title('index-title')
        self.assert_content('index-content')
        self.assert_body_attr('lare-done', None)

        no_matching_id_link = self.browser.find_element_by_css_selector('#no-matching-id-link')
        no_matching_id_link.click()

        self.wait.until(lambda browser: browser.title == 'no-matching-id-title')
        self.assert_title('no-matching-id-title')
        self.assert_content('index-content')  # container not found --> not applied

        self.assert_body_attr('lare-click', 'true')
        self.assert_body_attr('lare-before-send', 'true')
        self.assert_body_attr('lare-send', 'true')
        self.assert_body_attr('lare-timeout', None)
        self.assert_body_attr('lare-start', 'true')
        self.assert_body_attr('lare-success', 'true')
        self.assert_body_attr('lare-done', 'true')
        self.assert_body_attr('lare-fail', None)
        self.assert_body_attr('lare-always', 'true')
        self.assert_body_attr('lare-end', 'true')

        self.reset_body_attrs()

        self.assert_body_attr('lare-click', None)
        self.assert_body_attr('lare-before-send', None)
        self.assert_body_attr('lare-send', None)
        self.assert_body_attr('lare-timeout', None)
        self.assert_body_attr('lare-start', None)
        self.assert_body_attr('lare-success', None)
        self.assert_body_attr('lare-done', None)
        self.assert_body_attr('lare-fail', None)
        self.assert_body_attr('lare-always', None)
        self.assert_body_attr('lare-end', None)

        self.browser_go_back()

        self.wait.until(lambda browser: browser.title == 'index-title')
        self.assert_title('index-title')
        self.assert_content('index-content')

    def test_no_matching_id_initial_request(self):
        self.browser_get_reverse('no_matching_id')
        self.assert_title('no-matching-id-title')
        with self.assertRaises(NoSuchElementException):
            self.assert_content('no-matching-id-content')
        self.assertEqual(self.browser.find_element_by_id('not-matching-456').text, 'no-matching-id-content')
        self.assert_body_attr('lare-done', None)

        index_link = self.browser.find_element_by_css_selector('#index-link')
        index_link.click()

        self.wait.until(lambda browser: browser.title == 'index-title')
        self.assert_title('index-title')
        with self.assertRaises(NoSuchElementException):
            self.assert_content('index-content')
        self.assertEqual(self.browser.find_element_by_id('not-matching-456').text, 'no-matching-id-content')

        self.assert_body_attr('lare-click', 'true')
        self.assert_body_attr('lare-before-send', 'true')
        self.assert_body_attr('lare-send', 'true')
        self.assert_body_attr('lare-timeout', None)
        self.assert_body_attr('lare-start', 'true')
        self.assert_body_attr('lare-success', 'true')
        self.assert_body_attr('lare-done', 'true')
        self.assert_body_attr('lare-fail', None)
        self.assert_body_attr('lare-always', 'true')
        self.assert_body_attr('lare-end', 'true')

        self.reset_body_attrs()

        self.assert_body_attr('lare-click', None)
        self.assert_body_attr('lare-before-send', None)
        self.assert_body_attr('lare-send', None)
        self.assert_body_attr('lare-timeout', None)
        self.assert_body_attr('lare-start', None)
        self.assert_body_attr('lare-success', None)
        self.assert_body_attr('lare-done', None)
        self.assert_body_attr('lare-fail', None)
        self.assert_body_attr('lare-always', None)
        self.assert_body_attr('lare-end', None)

        self.browser_go_back()

        self.wait.until(lambda browser: browser.title == 'no-matching-id-title')
        self.assert_title('no-matching-id-title')
        with self.assertRaises(NoSuchElementException):
            self.assert_content('no-matching-id-content')
        self.assertEqual(self.browser.find_element_by_id('not-matching-456').text, 'no-matching-id-content')
