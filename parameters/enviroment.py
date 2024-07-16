import os
from enum import Enum

# https://www.twilio.com/en-us/blog/environment-variables-python
# https://www.google.com/search?q=python+env+variables&sca_esv=8c74246d85a060e1&ei=OT-WZrrCPKzJwPAPsLWrmAI&oq=jghtltktybt+env+python&gs_lp=Egxnd3Mtd2l6LXNlcnAiFmpnaHRsdGt0eWJ0IGVudiBweXRob24qAggAMggQABiABBiiBDIIEAAYgAQYogQyCBAAGIAEGKIEMggQABiABBiiBDIIEAAYgAQYogRIzipQiAlY_hRwAngBkAEAmAF0oAGcCaoBAzYuNrgBA8gBAPgBAZgCC6ACjAfCAgoQABiwAxjWBBhHwgINEAAYgAQYsAMYQxiKBcICChAAGIAEGLEDGA3CAgcQABiABBgNwgIIEAAYogQYiQWYAwCIBgGQBgqSBwM2LjWgB_oz&sclient=gws-wiz-serp
class Environment(Enum):
    DATABASE_TYPE = os.environ.get('DATABASE_TYPE')
    DATABASE_FILE_PATH = os.environ.get('DATABASE_FILE_PATH')