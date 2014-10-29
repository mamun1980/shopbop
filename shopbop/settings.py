# -*- coding: utf-8 -*-

# Scrapy settings for shopbop project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'shopbop'

SPIDER_MODULES = ['shopbop.spiders']
NEWSPIDER_MODULE = 'shopbop.spiders'

ITEM_PIPELINES = {
    # 'shopbop.pipelines.ShopbopPipeline': 0,
    # 'shopbop.pipelines.TestPipeline': 0,
    'shopbop.pipelines.ProductStoragePipeline': 0,
}

DATABASE = {'drivername': 'postgres',
            # 'host': '104.131.83.68',
            'host': 'localhost',
            'port': '5432',
            'username': 'postgres',
            'password': 'qweqwe',
            'database': 'robecart_hello'}
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'shopbop (+http://www.yourdomain.com)'
