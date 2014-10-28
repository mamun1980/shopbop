from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector
from shopbop.items import *
import re
class ClothProductSpider(CrawlSpider):
    name = "product_whatsnew"
    allowed_domains = ["www.shopbop.com"]
    start_urls = [
        #"http://www.shopbop.com/whats-new/br/v=1/2534374302029428.htm",
        #"http://www.shopbop.com/whats-new-clothing/br/v=1/2534374302155172.htm",
        "http://www.shopbop.com/whats-new-clothing-activewear/br/v=1/2534374302090400.htm",
        "http://www.shopbop.com/whats-new-dresses/br/v=1/2534374302090413.htm",
        "http://www.shopbop.com/whats-new-clothing-jackets-coats/br/v=1/2534374302090402.htm",
        "http://www.shopbop.com/whats-new-clothing-jeans/br/v=1/2534374302090401.htm",
        "http://www.shopbop.com/whats-new-jumpsuits-rompers/br/v=1/2534374302090392.htm",
        "http://www.shopbop.com/whats-new-clothing-lingerie-sleepwear/br/v=1/2534374302090403.htm",
        "http://www.shopbop.com/whats-new-clothing-maternity/br/v=1/2534374302179423.htm",
        "http://www.shopbop.com/whats-new-clothing-pants-leggings/br/v=1/2534374302090415.htm",
        "http://www.shopbop.com/whats-new-shorts/br/v=1/2534374302090396.htm",
        "http://www.shopbop.com/whats-new-skirts/br/v=1/2534374302090397.htm",
        "http://www.shopbop.com/whats-new-sweaters-knits/br/v=1/2534374302090391.htm",
        "http://www.shopbop.com/whats-new-swimwear/br/v=1/2534374302090414.htm",
        "http://www.shopbop.com/whats-new-tops/br/v=1/2534374302090416.htm",
        "http://www.shopbop.com/whats-new-clothing-vests/br/v=1/2534374302196581.htm",

        #"http://www.shopbop.com/whats-new-shoes/br/v=1/2534374302090411.htm",
        "http://www.shopbop.com/whats-new-shoes-booties/br/v=1/2534374302090509.htm",
        "http://www.shopbop.com/whats-new-shoes-boots-all/br/v=1/2534374302090510.htm",
        "http://www.shopbop.com/whats-new-shoes-flats/br/v=1/2534374302090507.htm",
        "http://www.shopbop.com/whats-new-shoes-pumps-heels/br/v=1/2534374302090503.htm",
        "http://www.shopbop.com/whats-new-shoes-sandals-all/br/v=1/2534374302090514.htm",
        "http://www.shopbop.com/whats-new-shoes-sneakers/br/v=1/2534374302090512.htm",
        "http://www.shopbop.com/whats-new-shoes-wedges/br/v=1/13208.htm",
        "http://www.shopbop.com/whats-new-shoes-rain-wear-cold-weather/br/v=1/28966.htm",

        #"http://www.shopbop.com/whats-new-bags/br/v=1/2534374302090393.htm",
        "http://www.shopbop.com/whats-new-handbags-backpacks/br/v=1/2534374302090464.htm",
        "http://www.shopbop.com/whats-new-handbags-clutches/br/v=1/2534374302090466.htm",
        "http://www.shopbop.com/whats-new-handbags-small-accessories/br/v=1/2534374302090468.htm",
        "http://www.shopbop.com/whats-new-handbags-hobo-bags/br/v=1/2534374302159459.htm",
        "http://www.shopbop.com/whats-new-bags-mini/br/v=1/29101.htm",
        "http://www.shopbop.com/whats-new-bags-luggage/br/v=1/2534374302090471.htm",
        "http://www.shopbop.com/whats-new-handbags-shoulder-bags/br/v=1/2534374302090462.htm",
        "http://www.shopbop.com/whats-new-handbags-totes/br/v=1/2534374302090469.htm",
        "http://www.shopbop.com/whats-new-handbags-wallets/br/v=1/2534374302090460.htm",

        #"http://www.shopbop.com/whats-new-accessories/br/v=1/2534374302090405.htm",
        "http://www.shopbop.com/whats-new-accessories-belts/br/v=1/2534374302090425.htm",
        "http://www.shopbop.com/whats-new-accessories-hats/br/v=1/2534374302090424.htm",
        "http://www.shopbop.com/whats-new-accessories-hair/br/v=1/2534374302090423.htm",
        "http://www.shopbop.com/whats-new-jewelry/br/v=1/2534374302090407.htm",
        "http://www.shopbop.com/whats-new-accessories-gloves/br/v=1/2534374302090422.htm",
        "http://www.shopbop.com/whats-new-accessories-home-gifts/br/v=1/2534374302197441.htm",
        "http://www.shopbop.com/whats-new-hosiery/br/v=1/2534374302090394.htm",
        "http://www.shopbop.com/whats-new-accessories-keychains/br/v=1/2534374302090418.htm",
        "http://www.shopbop.com/whats-new-accessories-scarves-wraps/br/v=1/2534374302090421.htm",
        "http://www.shopbop.com/whats-new-accessories-sunglasses-eyewear/br/v=1/2534374302090398.htm",
        "http://www.shopbop.com/whats-new-accessories-tech/br/v=1/2534374302090428.htm",
        "http://www.shopbop.com/whats-new-jewelry-watches/br/v=1/2534374302090492.htm",

        #"http://www.shopbop.com/whats-new-designer-boutique/br/v=1/2534374302180211.htm",
        "http://www.shopbop.com/whats-new-designer-boutique-clothing/br/v=1/2534374302180263.htm",
        "http://www.shopbop.com/whats-new-designer-boutique-shoes/br/v=1/2534374302180311.htm",
        "http://www.shopbop.com/whats-new-designer-boutique-bags/br/v=1/2534374302180312.htm",
        "http://www.shopbop.com/whats-new-designer-boutique-accessories/br/v=1/2534374302180219.htm",

        # "http://www.shopbop.com/special-top-sellers/br/v=1/2534374302073392.htm",
        # "http://www.shopbop.com/whats-new-top-sellers-clothes/br/v=1/2534374302173220.htm",
        # "http://www.shopbop.com/whats-new-top-sellers-shoes/br/v=1/2534374302173221.htm",
        # "http://www.shopbop.com/whats-new-top-sellers-bags/br/v=1/2534374302173218.htm",
        # "http://www.shopbop.com/whats-new-top-sellers-accessories/br/v=1/2534374302173219.htm",

    ]

    rules = (
        Rule (SgmlLinkExtractor(allow=(),restrict_xpaths=('//*[@id="product-container"]',)), 
            callback="parse_product"),

        Rule (SgmlLinkExtractor(tags=('span'), attrs=('data-next-link'), unique=True, 
            restrict_xpaths=('//*[@id="pagination-container-top"]/div[@class="pages"]')),),
    )
    

    def parse_product(self, response):
        # import pdb; pdb.set_trace()
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
                    cnlist.append(cn.strip().replace(":","").replace("'",""))

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