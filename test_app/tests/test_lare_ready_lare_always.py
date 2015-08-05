from __future__ import unicode_literals

from .helpers import SeleniumTestCase


class LareReadyLareAlwaysTest(SeleniumTestCase):

    def test_lare_ready_lare_always(self):
        self.browser_get_reverse('index')

        self.assertEqual(len(self.browser.find_elements_by_class_name('lare-always-div')), 0)
        self.assertEqual(len(self.browser.find_elements_by_class_name('lare-ready-div')), 0)
        self.assertEqual(len(self.browser.find_elements_by_class_name('lare-ready-once-div')), 0)

        lare_ready_lare_always_link = self.browser.find_element_by_css_selector('#lare-ready-lare-always-link')
        lare_ready_lare_always_link.click()

        self.wait.until(lambda browser: len(browser.find_elements_by_class_name('lare-always-div')) == 1)
        self.wait.until(lambda browser: len(browser.find_elements_by_class_name('lare-ready-div')) == 1)
        self.wait.until(lambda browser: len(browser.find_elements_by_class_name('lare-ready-once-div')) == 1)

        about_link = self.browser.find_element_by_css_selector('#about-link')
        about_link.click()

        self.wait.until(lambda browser: len(browser.find_elements_by_class_name('lare-always-div')) == 2)
        self.wait.until(lambda browser: len(browser.find_elements_by_class_name('lare-ready-div')) == 2)
        self.assertEqual(len(self.browser.find_elements_by_class_name('lare-ready-once-div')), 1)

        project_link = self.browser.find_element_by_css_selector('#project-link')
        project_link.click()

        self.wait.until(lambda browser: len(browser.find_elements_by_class_name('lare-always-div')) == 3)
        self.wait.until(lambda browser: len(browser.find_elements_by_class_name('lare-ready-div')) == 3)
        self.assertEqual(len(self.browser.find_elements_by_class_name('lare-ready-once-div')), 1)

        self.browser.back()

        self.wait.until(lambda browser: len(browser.find_elements_by_class_name('lare-always-div')) == 4)
        self.wait.until(lambda browser: len(browser.find_elements_by_class_name('lare-ready-div')) == 3)
        self.assertEqual(len(self.browser.find_elements_by_class_name('lare-ready-once-div')), 1)

        about_link = self.browser.find_element_by_css_selector('#about-link')
        about_link.click()

        self.wait.until(lambda browser: len(browser.find_elements_by_class_name('lare-always-div')) == 5)
        self.assertEqual(len(self.browser.find_elements_by_class_name('lare-ready-div')), 4)
        self.assertEqual(len(self.browser.find_elements_by_class_name('lare-ready-once-div')), 1)

    def test_disabled_lare(self):
        self.browser_get_reverse('index')

        self.assertEqual(len(self.browser.find_elements_by_class_name('lare-always-div')), 0)
        self.assertEqual(len(self.browser.find_elements_by_class_name('lare-ready-div')), 0)
        self.assertEqual(len(self.browser.find_elements_by_class_name('lare-ready-once-div')), 0)
        self.browser.execute_script('$.fn.lare.disable();')

        self.browser_get_reverse('lare_ready_lare_always', lare_state='disabled')

        self.wait.until(lambda browser: len(browser.find_elements_by_class_name('lare-always-div')) == 1)
        self.wait.until(lambda browser: len(browser.find_elements_by_class_name('lare-ready-div')) == 1)
        self.wait.until(lambda browser: len(browser.find_elements_by_class_name('lare-ready-once-div')) == 1)

        self.browser_get_reverse('about')

        self.wait.until(lambda browser: len(browser.find_elements_by_class_name('lare-always-div')) == 0)
        self.wait.until(lambda browser: len(browser.find_elements_by_class_name('lare-ready-div')) == 0)
        self.wait.until(lambda browser: len(browser.find_elements_by_class_name('lare-ready-once-div')) == 0)
