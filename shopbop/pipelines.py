# -*- coding: utf-8 -*-
import json
import psycopg2
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import *
from datetime import datetime
from sqlalchemy.exc import InternalError
import re

class ShopbopPipeline(object):
    def __init__(self):
        self.file = open('items.jl', 'wb')

    def process_item(self, item, spider):
        line = json.dumps(dict(item)) + "\n"
        self.file.write(line)
        return item


class CategoryStoragePipeline(object):

    def __init__(self):
        engine = db_connect()
        create_deals_table(engine)
        self.Session = sessionmaker(bind=engine)

    def close_spider(spider):
        self.con.close()

    def process_item(self, item, spider):
        session = self.Session()
        # import pdb; pdb.set_trace()
        name = item['name']
        demo = {'name': name}
        deal = Category(**demo)

        try:
            session.add(deal)
            session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.close()

        return item


class ProductStoragePipeline(object):

    def __init__(self):
        engine = db_connect()
        create_deals_table(engine)
        self.Session = sessionmaker(bind=engine)


    def process_item(self, item, spider):
        # import pdb; pdb.set_trace()
        session = self.Session()

        pid = item['product_id']
        product_sku = item['product_sku']
        brand_name = item['brand_name']
        product_title = item['title']
        product_description = item['description']

        desc_replace_Shopbop = re.sub("Shopbop","Robecart",product_description.strip())
        desc_replace_shopbop = re.sub("shopbop","Robecart",desc_replace_Shopbop.strip())
        desc_replace_SHOPBOP = re.sub("SHOPBOP","ROBECART",desc_replace_shopbop.strip())

        product_description = desc_replace_SHOPBOP

        product_price = item['price_new']
        product_currency = item['product_currency']

        size_n_fit = "<h1>Hello world!</h1>"

        related_products = item['related_products']

        product_images = item['images']
        
        product_cat = item['product_category']
        # cat_split = product_cat.split(" ")
        # cats = []
        # for cat in cat_split:
        #     cats.append(cat.strip().lower())
        # import pdb; pdb.set_trace();
        product_category = product_cat
        product_class = item['product_class']['name']

        try:
            sb_prod_class_q = session.query(ProductClass).filter(ProductClass.name == product_class)
            sb_prod_class = sb_prod_class_q.first()
        except Exception, e:
            pc = {'name': product_class, 'requires_shipping': True, 'track_stock': True, 
                    'slug': product_class.lower()}
            new_pc = ProductClass(**pc)
            sb_prod_class = session.add(new_pc)
            pass

        import pdb; pdb.set_trace()
        try:
            sb_prod_cat_q = session.query(Category).filter(Category.slug == product_category['slug'])
            sb_prod_cat = sb_prod_cat_q.first()
            if sb_prod_cat == None:
                raise
        except Exception, e:
            raise
        try:
            product_query = session.query(Product).filter(Product.product_id == pid)
            product = product_query.first()

            if product:
                new_prod_cat = {'product_id': product.id, 'category_id': sb_prod_cat.id}
                prod_cat = ProductCategory(**new_prod_cat)
                session.add(prod_cat)
                try:
                    session.commit()
                except Exception, e:
                    raise                
                
            else:
                title_remove_num = re.sub("\d+","",product_title) 
                title_remove_qout = re.sub("[\'\"]","",title_remove_num.strip())
                title_remove_slash = re.sub("[\\\/]","",title_remove_qout.strip())
                title_remove_speacial = re.sub("[!@#$&.+]","",title_remove_slash.strip())
                title_replace_Shopbop = re.sub("Shopbop","Robecart Inc",title_remove_speacial.strip())
                title_replace_shopbop = re.sub("shopbop","Robecart Inc",title_replace_Shopbop.strip())
                title_replace_SHOPBOP = re.sub("SHOPBOP","ROBECART INC",title_replace_shopbop.strip())

                slug = "-".join(title_replace_SHOPBOP.split(" ")),
                new_product_dict = {
                    'product_id': pid,
                    'product_sku': product_sku,
                    'brand_name': brand_name,
                    'title': title_replace_SHOPBOP,
                    'slug': slug,
                    'description': product_description,
                    'score': 0,
                    'date_created': datetime.now().isoformat(),
                    'date_updated': datetime.now().isoformat(),
                    'is_discountable': True,
                    'product_class_id': int(sb_prod_class.id),
                }
                add_new_prod  = Product(**new_product_dict)
                session.add(add_new_prod)
                session.flush()

                # prod_cat = ProductCategory({'product_id': add_new_prod.id, 'category_id': sb_prod_cat.id})
                new_prod_cat = {'product_id': add_new_prod.id, 'category_id': sb_prod_cat.id}
                prod_cat = ProductCategory(**new_prod_cat)
                session.add(prod_cat)

                # Add product size
                for size in item['product_sizes']:
                    pro_size = {}
                    pro_size['size'] = size['size']
                    pro_size['product_id'] = add_new_prod.id
                    prod_size = ProductSize(**pro_size)
                    session.add(prod_size)

                # Add product color
                # import pdb; pdb.set_trace()
                for color in item['product_colors']:
                    pro_color = {}
                    color_code = color['color_code']
                    try:
                        cc_q = session.query(ColorCode).filter(ColorCode.color_code == color_code)
                        color_code_ob = cc_q.first()
                        if color_code_ob == None:
                            new_cc = {
                                'color_code': color_code,
                                'color_name': color['color_name'],
                                'color_thumnail_url': color['color_thumnail_url']
                            }
                            color_code_ob = ColorCode(**new_cc)
                            session.add(color_code_ob)
                            session.flush()
                    except Exception, e:
                        raise
                    pro_color['color_code_id'] = color_code_ob.id
                    pro_color['color_order'] = color['color_order']
                    if color['color_order'] == 0:
                        pro_color['primary_color'] = True
                    else:
                        pro_color['primary_color'] = False
                        
                    pro_color['product_id'] = add_new_prod.id
                    # color_order = color_order + 1
                    prod_color = ProductColor(**pro_color)
                    session.add(prod_color)

                # Add product image
                # import pdb; pdb.set_trace();
                for product_image in product_images:
                    pro_image = {
                        'product_id': add_new_prod.id,
                        'original': product_image['original'],
                        'caption': title_replace_SHOPBOP,
                        'thumb_url': product_image['thumb_url'],
                        'small_image_url': product_image['small_image_url'],
                        'big_image_url': product_image['big_image_url'],
                        'image_url': product_image['image_url'],
                        'date_created': datetime.now().isoformat(),
                        'display_order': product_image['display_order'],
                        'color_code': product_image['color_code']
                    }
                    prod_image = ProductImage(**pro_image)
                    session.add(prod_image)
                

                # Add stock record

                st_rec = {
                    'partner_sku': product_sku,
                    'partner_id': 1,
                    'product_id': add_new_prod.id,
                    'price_currency': product_currency,
                    'date_created': datetime.now().isoformat(),
                    'date_updated': datetime.now().isoformat(),
                    'price_retail': product_price,
                    'price_excl_tax': product_price,
                    'num_in_stock': 1000
                }
                stock_record = StockRecord(**st_rec)
                session.add(stock_record)

                # Add size n fit
                snf = {
                    'fit': item['size_n_fit']['fit'],
                    'product': add_new_prod.id,
                }
                # import pdb; pdb.set_trace();
                sizenfit = SizeNfit(**snf)
                session.add(sizenfit)


                # Add reproduct info
                for rp in related_products:
                    related_pro = {
                        'product': add_new_prod.id,
                        'releted_product_id': rp['releted_product_id'],
                    }

                    related_product = RelatedProduct(**related_pro)
                    session.add(related_product)
                import pdb; pdb.set_trace();

                session.commit()
        except Exception, e:
            session.rollback()
            raise

        finally:
            session.close()

        # try:
        #     session.add(deal)
        #     session.commit()
        # except:
        #     session.rollback()
        #     raise
        # finally:
        #     session.close()

        return item

    def close_spider(spider):
        # self.con.close()
        pass
