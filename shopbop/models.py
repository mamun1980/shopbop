from sqlalchemy import create_engine, Column, BigInteger, String, Integer, Text, Boolean, DateTime, Numeric, LargeBinary
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine.url import URL

import settings

DeclarativeBase = declarative_base()


def db_connect():
    """
    Performs database connection using database settings from settings.py.
    Returns sqlalchemy engine instance
    """
    return create_engine(URL(**settings.DATABASE))


def create_deals_table(engine):
    """"""
    DeclarativeBase.metadata.create_all(engine)

class Product(DeclarativeBase):
    __tablename__ = "catalogue_product"

    id = Column(Integer, primary_key=True)
    product_id = Column('product_id', String(50))
    product_sku = Column('product_sku', String(100))
    brand_name = Column('brand_name', String(100))
    title = Column('title', String(200))
    slug = Column('slug', String(200))
    description = Column('description', Text)
    score = Column('score', Integer)
    date_created = Column('date_created', DateTime)
    date_updated = Column('date_updated', DateTime)
    is_discountable = Column('is_discountable', Boolean)
    product_class_id = Column('product_class_id', Integer)

class ProductClass(DeclarativeBase):
    """Sqlalchemy deals model"""
    __tablename__ = "catalogue_productclass"

    id = Column(Integer, primary_key=True)
    name = Column('name', String)
    slug = Column('slug', String)
    requires_shipping = Column('requires_shipping', Boolean)
    track_stock = Column('track_stock', Boolean)

class Category(DeclarativeBase):
    __tablename__ = "catalogue_category"

    id = Column(Integer, primary_key=True)
    name = Column('name', String(100) )
    slug = Column('slug', String(100) )
    path = Column('path', String(250))
    depth = Column('depth', Integer, autoincrement=True)


class ProductCategory(DeclarativeBase):
    __tablename__ = "catalogue_productcategory"

    id = Column(Integer, primary_key=True)
    product_id = Column('product_id', Integer)
    category_id = Column('category_id', Integer)


class ProductSize(DeclarativeBase):
    __tablename__ = "catalogue_productsize"

    id = Column(Integer, primary_key=True)
    product_id = Column('product_id', Integer)
    size = Column('size', String(10))

class ProductColor(DeclarativeBase):
    __tablename__ = "catalogue_productcolor"

    id = Column(Integer, primary_key=True)
    product_id = Column('product_id', Integer)
    color_code_id = Column('color_code_id', Integer)
    primary_color = Column("primary_color", Boolean)    
    color_order = Column('color_order', Integer)

class ColorCode(DeclarativeBase):
    __tablename__ = "catalogue_colorcode"
    
    id = Column(Integer, primary_key=True)
    color_name = Column('color_name', String(100))
    color_code = Column('color_code', String(100))
    color_thumnail_url = Column('color_thumnail_url', String(500))


class ProductImage(DeclarativeBase):
    __tablename__ = "catalogue_productimage"

    id = Column(Integer, primary_key=True)
    product_id = Column('product_id', Integer)
    original = Column("original", String(250))
    caption = Column("caption", String(250))
    display_order = Column("display_order", Integer)
    date_created = Column('date_created', DateTime)
    thumb_url = Column("thumb_url", String(500))
    small_image_url = Column("small_image_url", String(500))
    image_url = Column("image_url", String(500))
    big_image_url = Column("big_image_url", String(500))
    color_code = Column("color_code", String)

class StockRecord(DeclarativeBase):
    __tablename__ = "partner_stockrecord"

    id = Column(Integer, primary_key=True)
    product_id = Column('product_id', Integer)
    partner_id = Column('partner_id', Integer)
    partner_sku = Column('partner_sku', String(50))
    price_currency = Column('price_currency', String(10))
    date_created = Column('date_created', DateTime)
    date_updated = Column('date_updated', DateTime)
    price_retail = Column('price_retail', Numeric)
    price_excl_tax = Column('price_excl_tax', Numeric)
    num_in_stock = Column('num_in_stock', Integer)


class SizeNfit(DeclarativeBase):
    __tablename__ = "catalogue_sizenfit"

    id = Column(Integer, primary_key=True)
    fit = Column("fit", Text)
    product = Column("product_id", Integer)

class RelatedProduct(DeclarativeBase):
    __tablename__ = "catalogue_relatedproduct"

    id = Column(Integer, primary_key=True)
    product = Column("product_id", Integer)
    releted_product_id  = Column('releted_product_id', String(50))


