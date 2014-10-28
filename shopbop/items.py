# -*- coding: utf-8 -*-

import scrapy


class ProductClass(scrapy.Item):
    name = scrapy.Field()
    slug = scrapy.Field()
    requires_shipping = scrapy.Field()
    track_stock = scrapy.Field()

class Category(scrapy.Item):
	name = scrapy.Field()
	slug = scrapy.Field()
	full_name = scrapy.Field()
	path = scrapy.Field()
	depth = scrapy.Field()


class ProductCategory(scrapy.Item):
	name = scrapy.Field()
	parent_cat = scrapy.Field()
	# description = scrapy.Field()
	# relative_to = scrapy.Field()

class ProductImage(scrapy.Item):
	thumb_url = scrapy.Field()
	small_image_url = scrapy.Field()
	image_url = scrapy.Field()
	big_image_url = scrapy.Field()
	color_code = scrapy.Field()
	display_order = scrapy.Field()
	original = scrapy.Field()


class SizeNFitItem(scrapy.Item):
	fit = scrapy.Field()
	product = scrapy.Field()
	# measurement = scrapy.Field()
	# model_measurement = scrapy.Field()
	# size_table = scrapy.Field()

class ProductSize(scrapy.Item):
	size = scrapy.Field()
	selected = scrapy.Field()


class ProductColor(scrapy.Item):
	color_code = scrapy.Field()
	color_name = scrapy.Field()
	color_thumnail_url = scrapy.Field()
	color_order = scrapy.Field()
	product = scrapy.Field()
	


class RelatedProduct(scrapy.Item):
	releted_product_id = scrapy.Field()


class Product(scrapy.Item):
	product_id = scrapy.Field()
	product_sku = scrapy.Field()
	brand_name = scrapy.Field()
	title = scrapy.Field()
	slug = scrapy.Field()
	description = scrapy.Field()
	score = scrapy.Field()
	date_created = scrapy.Field()
	date_updated = scrapy.Field()
	is_discountable = scrapy.Field()

	price = scrapy.Field()
	price_new = scrapy.Field()
	product_currency = scrapy.Field()
	product_sizes = scrapy.Field()
	product_colors = scrapy.Field()
	product_class = scrapy.Field()
	product_category = scrapy.Field()
	description = scrapy.Field()
	images = scrapy.Field()
	size_n_fit = scrapy.Field()
	related_products = scrapy.Field()
	# related_product = scrapy.Field()
	