# -*-coding:utf-8 -*-
import asyncio, logging
import aiomysql


def log(sql, args=()):
    logging.info('sql:%s' % sql)
