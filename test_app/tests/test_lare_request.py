from __future__ import unicode_literals

from django.core.urlresolvers import reverse
from selenium.common.exceptions import NoSuchElementException

from .helpers import SeleniumTestCase


class LareRequestTest(SeleniumTestCase):

    def test_lare_request_depth_1(self):
        self.browser_get_reverse('index')
        self.assert_title('index-title')
        self.assert_content('index-content')
        self.assert_body_attr('lare-done', None)

        self.browser.find_element_by_class_name('to_be_removed_script')

        about_link = self.browser.find_element_by_css_selector('#about-link')
        about_link.click()

        self.wait.until(lambda browser: browser.title == 'about-title')
        self.assert_title('about-title')
        self.assert_content('about-content')
        keywords_metatag = self.browser.find_element_by_css_selector('meta[name="keywords"]')
        self.assertEqual(keywords_metatag.get_attribute('content'), 'This is a test')

        with self.assertRaises(NoSuchElementException):
            self.browser.find_element_by_class_name('to_be_removed_script')

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

    def test_lare_request_depth_1_and_back(self):
        self.browser_get_reverse('index')
        self.assert_title('index-title')
        self.assert_content('index-content')
        self.assert_body_attr('lare-done', None)

        self.browser.find_element_by_class_name('to_be_removed_script')

        about_link = self.browser.find_element_by_css_selector('#about-link')
        about_link.click()

        self.wait.until(lambda browser: browser.title == 'about-title')
        self.assert_title('about-title')
        self.assert_content('about-content')
        keywords_metatag = self.browser.find_element_by_css_selector('meta[name="keywords"]')
        self.assertEqual(keywords_metatag.get_attribute('content'), 'This is a test')

        with self.assertRaises(NoSuchElementException):
            self.browser.find_element_by_class_name('to_be_removed_script')
            
        self.assert_body_attr('lare-done', 'true')

        self.reset_body_attrs()
        self.assert_body_attr('lare-done', None)

        self.browser_go_back()

        self.assert_title('index-title')
        self.assert_content('index-content')
        self.assert_body_attr('lare-done', None)

        self.browser.find_element_by_class_name('to_be_removed_script')

    def test_lare_request_javascript(self):
        self.browser_get_reverse('index')
        self.assert_title('index-title')
        self.assert_content('index-content')
        self.assert_body_attr('lare-done', None)

        self.browser.find_element_by_class_name('to_be_removed_script')

        self.browser.execute_script("$(document).lare.request('{0}')".format(reverse('about')))

        self.wait.until(lambda browser: browser.title == 'about-title')
        self.assert_title('about-title')
        self.assert_content('about-content')
        keywords_metatag = self.browser.find_element_by_css_selector('meta[name="keywords"]')
        self.assertEqual(keywords_metatag.get_attribute('content'), 'This is a test')

        with self.assertRaises(NoSuchElementException):
            self.browser.find_element_by_class_name('to_be_removed_script')

        self.assert_body_attr('lare-click', None)
        self.assert_body_attr('lare-before-send', 'true')
        self.assert_body_attr('lare-send', 'true')
        self.assert_body_attr('lare-timeout', None)
        self.assert_body_attr('lare-start', 'true')
        self.assert_body_attr('lare-success', 'true')
        self.assert_body_attr('lare-done', 'true')
        self.assert_body_attr('lare-fail', None)
        self.assert_body_attr('lare-always', 'true')
        self.assert_body_attr('lare-end', 'true')

    def test_lare_request_javascript_and_back(self):
        self.browser_get_reverse('index')
        self.assert_title('index-title')
        self.assert_content('index-content')
        self.assert_body_attr('lare-done', None)

        self.browser.find_element_by_class_name('to_be_removed_script')

        self.browser.execute_script("$(document).lare.request('{0}')".format(reverse('about')))

        self.wait.until(lambda browser: browser.title == 'about-title')
        self.assert_title('about-title')
        self.assert_content('about-content')
        keywords_metatag = self.browser.find_element_by_css_selector('meta[name="keywords"]')
        self.assertEqual(keywords_metatag.get_attribute('content'), 'This is a test')

        with self.assertRaises(NoSuchElementException):
            self.browser.find_element_by_class_name('to_be_removed_script')

        self.assert_body_attr('lare-done', 'true')

        self.reset_body_attrs()
        self.assert_body_attr('lare-done', None)

        self.browser_go_back()

        self.assert_title('index-title')
        self.assert_content('index-content')
        self.assert_body_attr('lare-done', None)

        self.browser.find_element_by_class_name('to_be_removed_script')

    def test_lare_request_depth_2_to_no_lare_and_back(self):
        self.browser_get_reverse('index')
        self.assert_title('index-title')
        self.assert_content('index-content')
        self.assert_body_attr('lare-done', None)

        about_link = self.browser.find_element_by_css_selector('#about-link')
        about_link.click()

        self.wait.until(lambda browser: browser.title == 'about-title')
        self.assert_title('about-title')
        self.assert_content('about-content')

        self.assert_body_attr('lare-done', 'true')
        self.reset_body_attrs()
        self.assert_body_attr('lare-done', None)

        project_link = self.browser.find_element_by_css_selector('#project-link')
        project_link.click()

        self.wait.until(lambda browser: browser.title == 'project-title')
        self.assert_title('project-title')
        self.assert_content('project-content')

        self.assert_body_attr('lare-done', 'true')
        self.reset_body_attrs()
        self.assert_body_attr('lare-done', None)

        no_lare_response_link = self.browser.find_element_by_css_selector('#no-lare-response-link')
        no_lare_response_link.click()

        self.wait.until(lambda browser: browser.title == 'no-lare-response-title')
        self.assert_title('no-lare-response-title')
        self.assert_content('no-lare-response-content')
        self.assert_body_attr('lare-done', None)

        self.browser_go_back()

        # On Chrome/Webkit caching will return the content out of the lare xhr-response, not a new initial content.
        # fix #16 - lare load + fallback
        self.wait.until(lambda browser: browser.find_element_by_css_selector('#site'))

        self.wait.until(lambda browser: browser.title == 'project-title')
        self.assert_title('project-title')
        self.assert_content('project-content')
        self.assert_body_attr('lare-done', None)

    def test_lare_request_depth_2_to_no_lare_through_hard_load_and_back(self):
        self.browser_get_reverse('index')
        self.assert_title('index-title')
        self.assert_content('index-content')
        self.assert_body_attr('lare-done', None)

        about_link = self.browser.find_element_by_css_selector('#about-link')
        about_link.click()

        self.wait.until(lambda browser: browser.title == 'about-title')
        self.assert_title('about-title')
        self.assert_content('about-content')

        self.assert_body_attr('lare-done', 'true')
        self.reset_body_attrs()
        self.assert_body_attr('lare-done', None)

        project_link = self.browser.find_element_by_css_selector('#project-link')
        project_link.click()

        self.wait.until(lambda browser: browser.title == 'project-title')
        self.assert_title('project-title')
        self.assert_content('project-content')

        self.assert_body_attr('lare-done', 'true')
        self.reset_body_attrs()
        self.assert_body_attr('lare-done', None)

        self.browser.execute_script('location.href="{0}"'.format(reverse('no_lare_response')))

        self.wait.until(lambda browser: browser.title == 'no-lare-response-title')
        self.assert_title('no-lare-response-title')
        self.assert_content('no-lare-response-content')
        self.assert_body_attr('lare-done', None)

        self.browser_go_back()

        # On Chrome/Webkit caching will return the content out of the lare xhr-response, not a new initial content.
        # fix #16 - hard load
        self.wait.until(lambda browser: browser.find_element_by_css_selector('#site'))

        self.wait.until(lambda browser: browser.title == 'project-title')
        self.assert_title('project-title')
        self.assert_content('project-content')
        self.assert_body_attr('lare-done', None)
