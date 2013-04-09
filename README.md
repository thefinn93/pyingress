Ingress.py
==========

Python library for interacting with the [Ingress](https://www.ingress.com)
game. Requires you to have an Ingress account. The process of getting
your cookies is rather confusing, but that is a one time thing and once
it's done you can get down to coding.

Getting the cookies
----------
Since Google does not offer a proper way to do this, we simply ask for
the cookies that the intel map uses. Simplest way to do that is go to
the map in Chrome, open the Developer Tools pane or window (ctrl-shift-J
on everything except Mac) and wait for a request (move the map around to
force it to make some requests). Once ya get one, click it. On the right
hand pane a lot of data about the request will be shown, you just want
the block of text that is labeled "cookie". It appears to be different
from `document.cookie`, although I'm unclear why. This needs to be fed
to the library somehow. You can load it several ways:

When you initialize your `ingess` object:

```python
ingress = Ingress(cookies="blah blah blah")
```

or in a file. Stick it in `cookies.txt` in the working directory. This
will change in the future, likely to `~/.config/ingress.ini` with
ConfigParser syntext.

It will check for them in that order, and if it still does not have them
it will prompt the user for them.

Connecting to Ingress
----------

Once you've got your cookies, you can load them up in the ways explained
above. A simple program might look like this:

```python
#!/usr/bin/env python
from ingress import Ingress

ingress = Ingress() # cookies are stored in cookies.txt or the user is prompted for them


