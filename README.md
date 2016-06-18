# [lare.js](http://iekadou.com/programming/lare.js/) - lightweight asynchronous replacement engine

lare.js is [jQuery](http://jquery.com/) plugin that uses ajax and pushState to deliver a fast browsing experience.

It is able to replace **multiple containers** and different **head tags** with full back-forward functionality.

For [browsers that don't support pushState](http://caniuse.com/#search=pushstate) lare.js fully degrades.


## Why another pushstate library?

Shortly after starting with pjax a ran into some limitations like:

* how to add additional head elements?
* how to update multiple containers?

We started writing a workaround which became an own library and here we are :).

We hope lare.js will help people who are running into the same problems like we did.


## Note

There is already an awesome plugin called [jquery-pjax](https://github.com/defunkt/jquery-pjax) on which this project is based.


## Installation

* Download the latest release: [v1.0.1](https://github.com/lare-team/lare.js/archive/v1.0.1.zip)
* Clone the repository: `git clone git@github.com:lare-team/lare.js.git`.
* Curl the library: `curl -O https://raw.githubusercontent.com/lare-team/lare.js/master/lare.min.js`
* Install with [Bower](http://bower.io): `bower install lare`.


## Dependencies

Requires jQuery 1.9.x or higher.


## Usage

```javascript
$(document).lare('a');
```

That's all you need to activate lare.js functionality.

If you only want to bind lare.js when it's supported by the user's browser, you can activate lare.js like this:

```javascript
if ($.support.lare) {
    $(document).lare('a');
}
```

Or you can call the click handler by yourself and wrap it with some additional start functionality like this:

```javascript
if ($.support.lare) {
    $('#some-menu').on('click', 'a', function(event) {
        $(document).lare.click(event);
    });
}
```

Or you can make a lare.js request by pure calling:

```javascript
$(document).lare.request('/about/', {timeout: 1337});
```

If you are migrating an existing site you probably don't want to enable lare.js everywhere just yet.  Instead of using a global selector like `a` try annotating lare.js links with `data-lare`, then use `'a[data-lare]'` as your selector.

### data-lare-namespace

There is also the possibility to add a `data-lare-namespace` attribute to the body which will then be set as `X-LARE` in the request header.  This is just for initialising the namespace - Any further values should come from lare.js responses via `<lare-namespace>`.

By passing the namespace it's possible to limit the replacement area on the server side.  Checkout existing lare.js libraries below.


## Settings

Of course there are some options which will change your lare.js behavior:

* `timeout`: the time in ms lare.js will wait for a server response before hard loading the page. (default: `2000`)
* `push`: determines whether to push the lare.js request or not (default: `true`)
* `replace`: determines whether to replace the history state or not. will be ignored if `push` is `true`. (default: `false`)
* `scrollTo`: position in pixel the to scroll after lare.js requests. (default: `0`)
* `supportedVersion`: sends the minimal backend version which is supported by lare.js, backends should not respond with lare if own version is too low.
* `version`: delivered lare.js version. used to compare with `X-LARE-VERSION` of the response header to force hard load on mismatch.
You can either pass them as a second parameter on your `lare` call or override them globally via `$.fn.lare.defaults`.


## Ready functions

The following functions duplicate the behavior of `$(document).ready(function() {});` by [jQuery](http://jquery.com/) with additional features regarding lare.js.


* lareReady: Called on `$(document).ready()` and `lare:done`
* lareReadyOnce: Called on `$(document).ready()` and `lare:done` but only once
* lareAlways: Called on `$(document).ready()` and `lare:end`


## Signals

lare.js fires a number of events regardless of how its invoked.

All events are fired from the document, cause the actions concern the whole page.

* `lare:beforeSend` - Fired when request seems to be a valid request
* `lare:start` - Fired when request is sent to server and `popstate` is triggered
* `lare:send` - Fired when request is sent to server

* `lare:success`   remove 144
* `lare:done` - Fired when request is successfully processed

* `lare:fail` - Fired when request failed

* `lare:always` - Fired after request is finished, successful or not
* `lare:end` - Fired after request is completed, successful or not and `popstate` is completed

* `lare:timeout` - Fired when request timed out
* `lare:click` - Fired when a lare.js link is clicked

`send` and `complete` are a good pair of events to use if you are implementing a loading indicator. They'll only be triggered if an actual request is made, not if it's loaded from cache.

```javascript
$(document).on('lare:send', function() {
  $('#loading').show()
})
$(document).on('lare:complete', function() {
  $('#loading').hide()
})
```


## Response Structure & Rules

Check if the request header have **X-LARE-VERSION** set with a supported backend version and return rendered html in like this format:

```html
<lare-head>
    <title>...</title>
    <meta name="..." ...>
    <meta property="..." ...>
    <link href="..." ...>
    <script src="..."></script>
    <style>...</style>
</lare-head>
<lare-body>
    <... id="..." ...></...>
    <... id="..." ...></...>
    <... id="..." ...></...>
</lare-body>
<lare-namespace>...</lare-namespace>
```

* `lare-head` and `lare-body` are optional but if both are missing, lare will hard load the giving url.
* `lare-head`
    * `title` will always be replaced if given.
    * `meta` will be replaced if `name` or `property` find a match, otherwise it will be appended.
    * `link` will be replaced if `href` finds a match, otherwise it will be appended.
    * `script` will be replaced if `href` finds a match, otherwise it will be appended.
    * `style` will always be appended.
    * `data-remove-on-lare` can the written to any tag and will force the element to be removed with the next pjaxr request and restored on popstate.
* `lare-body`
    * every child must have an id.
* `lare-namespace` is optional but when given - it's value will be passed on further request via `X-LARE-NAMESPACE` by `lare.js`.
* any other content will be ignored.

### Existing Lare Server Side Libraries

These libs are making use of the advanced pjaxr namespacing functionality:

* Django: https://github.com/lare-team/django-lare
* PHP: https://github.com/lare-team/php-lare
* Twig: https://github.com/lare-team/twig-lare

### Existing Lare Server Side Libraries

There are many available plugins for different languages and frameworks which will lift the heavy work for you:

* Asp.Net MVC3: http://biasecurities.com/blog/2011/using-pjax-with-asp-net-mvc3/
* Aspen: https://gist.github.com/whit537/6059536
* CakePHP : https://github.com/sanojimaru/CakePjax
* Express: https://github.com/abdelsaid/express-pjax-demo
* Flask: https://github.com/zachwill/pjax_flask
* FuelPHP: https://github.com/rcrowe/fuel-pjax
* Grails: http://www.bobbywarner.com/2012/04/23/add-some-pjax-to-grails/
* Rails: https://github.com/rails/pjax_rails


## Testing

As noted above: the testcases are **incomplete**

The main reason for this is that it's really hard to simulate complex page transitions. If you want to support this project - you can take a look at the structure of the existing ones an write some additional tests. Help is always welcome!

To run the tests locally you have to follow these steps:

1. clone the repository

    ```
git clone git@github.com:lare-team/lare.js.git
    ```
2. install python dependencies for test suite

    ```
pip install Django==1.6.6
pip install django-lare==1.0.0
pip install selenium==2.42.1
    ```
3. install node dependencies for test suite

    ```
npm install
    ```
4. copy pjaxr js into test_app

    ```
npm run-script prepare-tests
    ```
5. install node dependencies for test_app (bower)

    ```
cd test_app
npm install
    ```
6. install bower dependencies for test_app

    ```
npm run-script bower-install
    ```
7. run the tests

    ```
cd ..
python test_app/tests/runtests.py
    ```
    
Note: you may need to download the [ChromeDriver](http://chromedriver.storage.googleapis.com/index.html) if it's not already installed. 


## Sites using lare.js

If you are using this library and want to get listed below.  Please let me know.  Just make a pull request.

* https://socialfunders.org
* http://iekadou.com


## Contributing

Help is appreciated!


## Thanks

We like to thank [Chris Wanstrath](https://github.com/defunkt) for his really awesome [jquery-pjax](https://github.com/defunkt/jquery-pjax) library.  This project wouldn't exist without his work.


## Copyright and license

Copyright 2013-2016 Lare-Team, under [MIT license](https://github.com/lare-team/lare.js/blob/master/LICENSE).
