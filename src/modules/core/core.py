import os
from utils.dynamic_router import search_routers

MODULE_PATH = f'{os.getcwd()}{os.path.sep}src{os.path.sep}modules{os.path.sep}core'

router_urls = search_routers(MODULE_PATH)

print(router_urls, len(router_urls))
print(os.getcwd())
