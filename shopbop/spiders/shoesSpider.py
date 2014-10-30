from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector
from shopbop.items import *
import re
class ClothProductSpider(CrawlSpider):
    name = "product_shoes"
    allowed_domains = ["www.shopbop.com"]
    start_urls = [
        "http://www.shopbop.com/shoes/br/v=1/2534374302024643.htm",
        "http://www.shopbop.com/shoes-booties/br/v=1/2534374302112431.htm",
        "http://www.shopbop.com/shoes-booties-flat/br/v=1/2534374302159515.htm",
        "http://www.shopbop.com/shoes-booties-heeled/br/v=1/2534374302153373.htm",
        "http://www.shopbop.com/shoes-booties-lace/br/v=1/2534374302183263.htm",

        "http://www.shopbop.com/shoes-boots/br/v=1/2534374302112432.htm",
        "http://www.shopbop.com/shoes-boots-flat/br/v=1/2534374302112433.htm",
        "http://www.shopbop.com/shoes-boots-heeled/br/v=1/2534374302153371.htm",
        "http://www.shopbop.com/shoes-boots-knee-high/br/v=1/2534374302153374.htm",
        "http://www.shopbop.com/shoes-boots-over-knee/br/v=1/13465.htm",

        "http://www.shopbop.com/shoes-flats/br/v=1/2534374302112436.htm",
        "http://www.shopbop.com/shoes-flats-ballet/br/v=1/2534374302201780.htm",
        "http://www.shopbop.com/shoes-flats-espadrilles/br/v=1/27787.htm",
        "http://www.shopbop.com/shoes-flats-loafers/br/v=1/2534374302201781.htm",
        "http://www.shopbop.com/shoes-flats-oxfords/br/v=1/2534374302201782.htm",
        "http://www.shopbop.com/shoes-flats-slippers/br/v=1/2534374302201880.htm",

        "http://www.shopbop.com/shoes-pumps/br/v=1/2534374302112441.htm",
        "http://www.shopbop.com/shoes-pumps-heels-open-toe/br/v=1/2534374302159460.htm",
        "http://www.shopbop.com/shoes-pumps-heels-platforms/br/v=1/2534374302159453.htm",

        "http://www.shopbop.com/shoes-rain-boots/br/v=1/13490.htm",
        "http://www.shopbop.com/shoes-sandals/br/v=1/2534374302112442.htm",
        "http://www.shopbop.com/shoes-sandals-flat/br/v=1/2534374302112443.htm",
        "http://www.shopbop.com/shoes-sandals-flip-flops/br/v=1/2534374302112437.htm",
        "http://www.shopbop.com/shoes-sandals-high-heeled/br/v=1/2534374302112444.htm",
        "http://www.shopbop.com/shoes-sandals-platforms/br/v=1/2534374302159496.htm",

        "http://www.shopbop.com/shoes-sneakers/br/v=1/2534374302112446.htm",
        "http://www.shopbop.com/shoes-sneakers-high-top/br/v=1/31213.htm",
        "http://www.shopbop.com/shoes-sneakers-low-top/br/v=1/31212.htm",
        "http://www.shopbop.com/shoes-sneakers-slip/br/v=1/31214.htm",
        "http://www.shopbop.com/shoes-wedges/br/v=1/13479.htm",
        "http://www.shopbop.com/shoes-winter-boots/br/v=1/33279.htm",
        "http://www.shopbop.com/shoes-shoe-accessories/br/v=1/13477.htm",
        "http://www.shopbop.com/shoes-designer-boutique/br/v=1/2534374302124543.htm",
        "http://www.shopbop.com/shoes-trend-combat-moto/br/v=1/13478.htm",
        "http://www.shopbop.com/shoes-trend-nude/br/v=1/13485.htm",
        "http://www.shopbop.com/shoes-trend-shearling-fur/br/v=1/33281.htm",

    ]

    rules = (
        Rule (SgmlLinkExtractor(allow=(),restrict_xpaths=('//*[@id="product-container"]',)), 
            callback="parse_product"),

        Rule (SgmlLinkExtractor(tags=('span'), attrs=('data-next-link'), unique=True, 
            restrict_xpaths=('//*[@id="pagination-container-top"]/div[@class="pages"]')),),
    )
    

    def parse_product(self, response):
        product = Product()
        
        path_product_info = response.xpath('//*[@id="product-information"]')
        path_product_price = response.xpath('//*[@id="productPrices"]')

        product['product_id'] = response.xpath('//*[@id="productId"]/text()').extract()[0].strip()
        product['product_sku'] = path_product_info.xpath('//*[@id="productCode"]/@content').extract()[0].strip()
        product['brand_name'] = path_product_info.xpath('a/h1/text()').extract()[0].strip()
        product['title'] = path_product_info.xpath('//*[@id="product-information"]/p/text()').extract()[0].strip()

        descs = response.xpath('//*[@id="detailsAccordion"]/div[@itemprop="description"]/node()').extract()
        description = ''
        for desc in descs:
            description = description + desc
        product['description'] = description

        product_class = ProductClass()
        product_cat = ProductCategory()
        # import pdb; pdb.set_trace()
        cat_names = response.xpath('//*[@id="right-column"]/div[@class="breadcrumbs"]/ul/li')
        
        try:
            pclass = cat_names[0].xpath('span/text()').extract()[0].strip()
        except IndexError:
            pclass = cat_names[0].xpath('a/@title').extract()[0]
            pass
        product_class['name'] = pclass
        product_class['slug'] = pclass.lower()
        product_class['requires_shipping'] = True
        product_class['track_stock'] = True
        product['product_class'] = product_class

        # import pdb; pdb.set_trace()
        cat_slug = ''
        cat_full_name = ' '
        for cat_name in cat_names:    
            try:
                cname = cat_name.xpath('a/@title').extract()[0].strip()
            except IndexError:
                cname = cat_name.xpath('span/text()').extract()[0].strip()                
                pass
            cname = re.sub(r"[:,'\/&]","",cname.strip())
            cnamesplit = re.split(r"[ /]",cname)
            cnlist = []
            for cn in cnamesplit:
                if cn != "":
                    # cn = re.sub(r"[:,'/\\]","",cn.strip())
                    cnlist.append(cn)

            csname = "-".join(cnlist)
            cat_slug = cat_slug + csname.lower() +"/"
            cat_full_name = cat_full_name + cname.strip() + " > "

        cat_full_name = cat_full_name[:-3].strip()
        cat_slug = cat_slug[:-1].strip()

        product_cat = {'full_name': cat_full_name, 
                        'slug': cat_slug, 
                        'name': cat_full_name.split(" > ")[-1]}
        # import pdb; pdb.set_trace()
        product['product_category'] = product_cat




        # if len(cat_names) == 4:
        #     pcat_name = cat_names[2].xpath('a/@title').extract()[0]
        #     product_cat['parent_cat'] = pcat_name.strip()
        #     cat_name = cat_names[3].xpath('a/@title').extract()[0]
        #     product_cat['name'] = cat_name
        #     product['product_category'] = product_cat
        # elif len(cat_names) == 3:
        #     pcat_name = cat_names[1].xpath('a/@title').extract()[0]
        #     product_cat['parent_cat'] = pcat_name.strip()
        #     cat_name = cat_names[2].xpath('a/@title').extract()[0]
        #     product_cat['name'] = cat_name
        #     product['product_category'] = product_cat

        # elif len(cat_names) == 2:
        #     # import pdb; pdb.set_trace()
        #     pcat_name = pclass
            
        #     product_cat['parent_cat'] = pcat_name.strip()
        #     cat_name = cat_names[1].xpath('a/@title').extract()[0]
        #     product_cat['name'] = cat_name
        #     product['product_category'] = product_cat
        # else:
        #     product_cat['name'] = pclass
        #     product_cat['parent_cat'] = None
        #     product['product_category'] = product_cat

        product_colors = []
        colors = response.xpath('//*[@id="swatches"]/img')
        color_order = 0
        for color in colors:
            pcolor = color.xpath('@class').extract()[0]
            color_classes = pcolor.split(" ")
            if not 'hide' == color_classes:
                product_color = ProductColor()
                product_color['color_name'] = color.xpath('@title').extract()[0]
                product_color['color_code'] = color.xpath('@id').extract()[0].split(".")[1]
                product_color['color_order'] = color_order
                product_color['color_thumnail_url'] = color.xpath('@src').extract()[0]
                product_colors.append(product_color)
                color_order = color_order + 1
        product['product_colors'] = product_colors


        pro_thumb_list = response.xpath('//*[@id="thumbnailList"]')
        pro_image_list = pro_thumb_list.xpath('li[@class="thumbnailListItem"]/img')
        product_images = []
        thumb_order = 0

        for pro_image in pro_image_list:
            
            root_img_url = pro_image.xpath('@src').extract()[0].strip()
            if root_img_url != '':
                for prcolor in product_colors:

                    product_image = ProductImage()
                    image_split = root_img_url.split("/")
                    skuncolorcode = product['product_sku'].lower()+prcolor['color_code']
                    if not image_split[11] == skuncolorcode:
                        image_split[12] = image_split[12].replace(image_split[11], skuncolorcode)
                        image_split[11] = skuncolorcode
                        img_url = "/".join(image_split)
                    else:
                        img_url = root_img_url
                    product_image['thumb_url'] = img_url
                    if '_37x65' in img_url:
                        small_image_url = img_url.replace("_37x65","_150x296")
                        product_image['small_image_url'] = small_image_url.replace("_q","_p")
                        product_image['image_url'] = img_url.replace("_37x65","_336x596")
                        product_image['big_image_url'] = img_url.replace("_37x65","")
                        product_image['original'] = 'images/products/t-shirt2.png'
                        product_image['display_order'] = thumb_order
                        product_image['color_code'] = prcolor['color_code']
                        thumb_order = thumb_order + 1
                        product_images.append(product_image)
                    elif '_29x58' in img_url:
                        small_image_url = img_url.replace("_29x58","_150x296")
                        product_image['small_image_url'] = small_image_url.replace("_q","_p")
                        product_image['image_url'] = img_url.replace("_29x58","_336x596")
                        product_image['big_image_url'] = img_url.replace("_29x58","")
                        product_image['original'] = 'images/products/t-shirt2.png'
                        product_image['display_order'] = thumb_order
                        product_image['color_code'] = prcolor['color_code']
                        thumb_order = thumb_order + 1
                        product_images.append(product_image)
                    # thumb_order = 0

        product['images'] = product_images

        related_products = []
        rp_id_links = response.xpath('//*[@id="similarities"]/li/div/a')
        for rp_id_li in rp_id_links:
            related_product = RelatedProduct()
            url = rp_id_li.xpath("@href").extract()[0]
            rp_id = url.split("=")[-1]
            related_product['releted_product_id'] = rp_id
            related_products.append(related_product)
        product['related_products'] = related_products

        product_sizes = []
        sizes = response.xpath('//*[@id="sizes"]/span')
        for size in sizes:
            product_size = ProductSize()
            product_size['size'] = size.xpath('@data-selectedsize').extract()[0]
            product_sizes.append(product_size)
        product['product_sizes'] = product_sizes
        sizenfit = SizeNFitItem()
        allfits = response.xpath('//*[@id="sizeFitContainer"]/node()').extract()
        fittext = ''
        for allfit in allfits:
            fittext = fittext + allfit
        sizenfit['fit'] = fittext
        product['size_n_fit'] = sizenfit
        # import pdb; pdb.set_trace()
        try:
            price = response.xpath('//*[@id="productPrices"]/div[@class="priceBlock"]/span[@class="salePrice"]/text()')[0].extract().strip().replace(",","")
        except IndexError:
            price = path_product_price.xpath('meta[1]/@content').extract()[0].strip().replace(",","")
            pass
        
        

        product['price'] = price.split("$")[1]
        product['price_new'] = float(price.split("$")[1])/2
        product['product_currency'] = path_product_price.xpath('meta[2]/@content').extract()[0].strip()
        # import pdb; pdb.set_trace()
        return product