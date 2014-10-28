from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector
from shopbop.items import *
import re
# from shopbop.spiders.helper import parse_product


class ClothProductSpider(CrawlSpider):
    name = "product_access"
    allowed_domains = ["www.shopbop.com"]
    start_urls = [
        # "http://www.shopbop.com/accessories/br/v=1/2534374302024641.htm",
        "http://www.shopbop.com/accessories-jewelry/br/v=1/2534374302024617.htm",
        "http://www.shopbop.com/accessories-jewelry-bracelets/br/v=1/2534374302060428.htm",
        "http://www.shopbop.com/accessories-jewelry-earrings/br/v=1/2534374302060430.htm",
        "http://www.shopbop.com/accessories-jewelry-fine/br/v=1/19361.htm",
        "http://www.shopbop.com/accessories-jewelry-necklaces/br/v=1/2534374302060432.htm",
        "http://www.shopbop.com/accessories-jewelry-body-hand-chains/br/v=1/2534374302055824.htm",
        "http://www.shopbop.com/accessories-jewelry-personalized/br/v=1/2534374302056145.htm",
        "http://www.shopbop.com/accessories-jewelry-rings/br/v=1/2534374302060434.htm",
        "http://www.shopbop.com/accessories-trend-rose-gold/br/v=1/22024.htm",
        "http://www.shopbop.com/accessories-belts/br/v=1/2534374302062844.htm",
        "http://www.shopbop.com/accessories-gloves/br/v=1/2534374302062843.htm",
        "http://www.shopbop.com/accessories-hair/br/v=1/2534374302062842.htm",
        "http://www.shopbop.com/accessories-hats/br/v=1/2534374302062819.htm",
        "http://www.shopbop.com/accessories-home-gifts/br/v=1/2534374302197440.htm",
        "http://www.shopbop.com/accessories-home-gifts-books/br/v=1/28981.htm",
        "http://www.shopbop.com/accessories-home-gifts-dog/br/v=1/29004.htm",
        "http://www.shopbop.com/accessories-home-gifts-entertaining/br/v=1/29002.htm",
        "http://www.shopbop.com/accessories-home-gifts-decor/br/v=1/29005.htm",
        "http://www.shopbop.com/accessories-home-gifts-stationery/br/v=1/29003.htm",
        "http://www.shopbop.com/accessories-home-gifts-stationery/br/v=1/29003.htm",
        "http://www.shopbop.com/accessories-home-gifts-stationery/br/v=1/29003.htm",
        "http://www.shopbop.com/accessories-home-gifts-towels/br/v=1/29006.htm",
        "http://www.shopbop.com/hosiery/br/v=1/2534374302072037.htm",
        "http://www.shopbop.com/hosiery-socks/br/v=1/2534374302072085.htm",
        "http://www.shopbop.com/hosiery-tights/br/v=1/2534374302072084.htm",
        "http://www.shopbop.com/accessories-keychains/br/v=1/2534374302062839.htm",
        "http://www.shopbop.com/accessories-scarves-wraps/br/v=1/2534374302062834.htm",
        "http://www.shopbop.com/accessories-sunglasses-eyewear/br/v=1/2534374302029451.htm",
        "http://www.shopbop.com/accessories-sunglasses-eyewear-aviator/br/v=1/20041.htm",
        "http://www.shopbop.com/accessories-sunglasses-eyewear-aviator/br/v=1/20041.htm",
        "http://www.shopbop.com/accessories-sunglasses-eyewear-cat-eye/br/v=1/20042.htm",
        "http://www.shopbop.com/accessories-sunglasses-eyewear-mirrored/br/v=1/20043.htm",
        "http://www.shopbop.com/accessories-sunglasses-eyewear-oversized/br/v=1/20044.htm",
        "http://www.shopbop.com/accessories-sunglasses-eyewear-rectangle/br/v=1/20045.htm",
        "http://www.shopbop.com/accessories-sunglasses-eyewear-round/br/v=1/20046.htm",
        "http://www.shopbop.com/accessories-sunglasses-eyewear-special-fit/br/v=1/28301.htm",
        "http://www.shopbop.com/accessories-sunglasses-eyewear-statement/br/v=1/20047.htm",
        "http://www.shopbop.com/accessories-sunglasses-eyewear-optical/br/v=1/2534374302195501.htm",
        "http://www.shopbop.com/accessories-sunglasses-eyewear-cases-chains/br/v=1/19649.htm",
        "http://www.shopbop.com/accessories-tech/br/v=1/2534374302062840.htm",
        "http://www.shopbop.com/accessories-tech-headphones/br/v=1/2534374302203187.htm",
        "http://www.shopbop.com/accessories-tech-laptop/br/v=1/2534374302203194.htm",
        "http://www.shopbop.com/accessories-tech-phone/br/v=1/2534374302203196.htm",
        "http://www.shopbop.com/accessories-tech-tablet-reader/br/v=1/2534374302203189.htm",
        "http://www.shopbop.com/accessories-travel/br/v=1/13586.htm",
        "http://www.shopbop.com/accessories-umbrellas/br/v=1/2534374302062835.htm",
        "http://www.shopbop.com/accessories-watches/br/v=1/2534374302055823.htm",
        "http://www.shopbop.com/accessories-winter/br/v=1/2534374302207430.htm",
        "http://www.shopbop.com/accessories-designer-boutique/br/v=1/2534374302123250.htm",
    ]

    rules = (        
        
        Rule (SgmlLinkExtractor(restrict_xpaths=('//*[@id="product-container"]')), 
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
            cnamesplit = re.split(r"[ /]",cname)
            cnlist = []
            for cn in cnamesplit:
                if cn != "":
                    cnlist.append(cn.strip().replace("'",""))

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
                    small_image_url = img_url.replace("_37x65","_150x296")
                    product_image['small_image_url'] = small_image_url.replace("_q","_p")
                    product_image['image_url'] = img_url.replace("_37x65","_336x596")
                    product_image['big_image_url'] = img_url.replace("_37x65","")
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