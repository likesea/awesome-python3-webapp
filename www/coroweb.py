__author__ = 'yanbi_000'
import asyncio, os, inspect, logging, functools
from urllib import  parse
from aiohttp import  web

def get(path):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            return func(*args,**kw)
        wrapper.__method__="GET"
        wrapper.__route__=path
        return wrapper
    return decorator
