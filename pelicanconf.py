AUTHOR = 'Adrian Loo'
SITENAME = 'SpyderMaxi'
SITEURL = 'https://spydermaxi.com'
SITESUBTITLE = ""
TIMEZONE = 'Asia/Singapore'

THEME = "pelican-progem"

# can be useful in development, but set to False when you're ready to publish
RELATIVE_URLS = True
ARTICLE_URL = 'posts/{date:%Y}/{date:%b}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%b}/{date:%d}/{slug}/index.html'

FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/{slug}.atom.xml'

PATH = 'content'
DEFAULT_LANG = 'en'

GITHUB_URL = 'http://github.com/spydermaxi/'
# DISQUS_SITENAME = "spydermaxi"
DEFAULT_PAGINATION = 5
DEFAULT_DATE = (2012, 3, 2, 14, 1, 1)

LINKS = ()

# Social widget should be in tuple format ('social-name', 'social-website') #
SOCIAL = (('github', 'http://github.com/spydermaxi'),
          ('twitter', 'https://twitter.com/spydermaxi'))

# path-specific metadata
EXTRA_PATH_METADATA = {
    'extra/favicon.ico': {'path': 'favicon.ico'},
}

# static paths will be copied without parsing their contents
STATIC_PATHS = [
    'images',
    'extra',
]

# there is no other HTML content
READERS = {'html': None}

# code blocks with line numbers
# PYGMENTS_RST_OPTIONS = {'linenos': 'table'}

# Image process configuration
IMAGE_PROCESS = {
    "large-photo": {
        "type": "responsive-image",
        "sizes": (
            "(min-width: 1200px) 800px, "
            "(min-width: 992px) 650px, "
            "(min-width: 768px) 718px, "
            "100vw"
        ),
        "srcset": [
            ("600w", ["scale_in 600 450 True"]),
            ("800w", ["scale_in 800 600 True"]),
            ("1600w", ["scale_in 1600 1200 True"]),
        ],
        "default": "800w",
    },
}
