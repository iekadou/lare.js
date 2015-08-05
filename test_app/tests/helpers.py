from __future__ import unicode_literals

import base64
import httplib
import json
from os import getenv
import sys

from django.core.urlresolvers import reverse
from django.test import LiveServerTestCase

from selenium import webdriver
from selenium.webdriver.support import ui


class SeleniumTestCase(LiveServerTestCase):

    def setUp(self):
        if getenv('SAUCE_USERNAME'):
            self.browser = self.sauce_labs_driver()
        else:
            self.browser = webdriver.Chrome(executable_path='/Users/jonas/Coding/iekadou/lare.js/venv/bin/chromedriver')
        self.browser.set_window_size(50, 50)
        self.wait = ui.WebDriverWait(self.browser, 10)
        super(SeleniumTestCase, self).setUp()

    def tearDown(self):
        if hasattr(self, 'sauce_username'):
            self.report_status()
        self.browser.close()
        self.browser.quit()
        super(SeleniumTestCase, self).tearDown()

    def sauce_labs_driver(self):
        self.sauce_username = getenv('SAUCE_USERNAME')
        self.sauce_access_key = getenv('SAUCE_ACCESS_KEY')
        self.sauce_auth = base64.encodestring('{0}:{1}'.format(self.sauce_username, self.sauce_access_key))[:-1]
        caps = {
            'platform': getenv('SELENIUM_PLATFORM'),
            'browserName': getenv('SELENIUM_BROWSER'),
            'version': getenv('SELENIUM_VERSION'),
            'javascriptEnabled': getenv('SELENIUM_JAVASCRIPT', True),
            'tunnel-identifier': getenv('TRAVIS_JOB_NUMBER'),
            'name': 'jquery-lare-{}'.format(self._testMethodName),
            'build': getenv('TRAVIS_BUILD_NUMBER'),
        }
        hub_url = 'http://{0}:{1}@ondemand.saucelabs.com/wd/hub'.format(self.sauce_username, self.sauce_access_key)
        return webdriver.Remote(desired_capabilities=caps, command_executor=str(hub_url))  # webdriver.Remote only accepts str - not unicode

    def report_status(self):
        info = sys.exc_info()
        passed = info[0] is None

        url = '/rest/v1/{0}/jobs/{1}'.format(self.sauce_username, self.browser.session_id)
        data = {'passed': passed}
        headers = {'Authorization': 'Basic {0}'.format(self.sauce_auth)}

        connection = httplib.HTTPConnection('saucelabs.com')
        connection.request('PUT', url, json.dumps(data), headers)
        result = connection.getresponse()
        return result.status == 200

    def reverse_url(self, name, **kwargs):
        return '{0}{1}'.format(self.live_server_url, reverse(name, kwargs=kwargs))

    def browser_get_reverse(self, name, **kwargs):
        self.browser.get(self.reverse_url(name, **kwargs))

    def browser_go_back(self):
        if getenv('SELENIUM_BROWSER') == 'safari':
            self.browser.execute_script('history.go(-1);')
        else:
            self.browser.back()

    def browser_go_forward(self):
        if getenv('SELENIUM_BROWSER') == 'safari':
            # safari don't know how to go back
            self.browser.execute_script('history.go(1);')
        else:
            self.browser.forward()

    def assert_title(self, title):
        self.assertEqual(self.browser.title, title)

    def assert_content(self, content):
        c = self.browser.find_element_by_css_selector('#content').text
        self.assertEqual(c, content)

    def assert_current_url(self, name, **kwargs):
        self.assertEqual(self.browser.current_url, self.reverse_url(name, **kwargs))

    def assert_body_namespace(self, namespace):
        body = self.browser.find_element_by_css_selector('body')
        body_attr = body.get_attribute('data-lare-namespace')
        self.assertEqual(body_attr, namespace)

    def assert_current_namespace(self, namespace):
        self.browser.execute_script("$('body').attr('data-selenium-lare-current-namespace', $.fn.lare.state.namespace);")
        self.assert_body_attr('lare-current-namespace', namespace)

    def assert_body_attr(self, attribute, value):
        body = self.browser.find_element_by_css_selector('body')
        body_attr = body.get_attribute('data-selenium-' + attribute)
        self.assertEqual(body_attr, value)

    def reset_body_attrs(self):
        self.browser.execute_script('$("body").removeAttrs(/^data-selenium-/);')
