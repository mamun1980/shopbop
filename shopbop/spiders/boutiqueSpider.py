import scrapy
# from shopbop.SeleniumSpider import SeleniumSpider
from shopbop.items import *
from shopbop.spiders.helper import parse_product as parse
import re

class MySpider(scrapy.Spider):
    name = "prdoduct_boutique"
    allowed_domains = ["www.shopbop.com"]
    start_urls = [
        "http://www.shopbop.com/boutique-whats-new-db/br/v=1/2534374302052549.htm",

        "http://www.shopbop.com/boutique-designer-boutique-clothes/br/v=1/2534374302159436.htm",
        "http://www.shopbop.com/boutique-designer-clothes-jeans/br/v=1/2534374302159479.htm",
        "http://www.shopbop.com/boutique-designer-boutique-clothes-dresses/br/v=1/2534374302159512.htm",
        "http://www.shopbop.com/boutique-designer-boutique-clothes-jackets/br/v=1/2534374302159475.htm",
        "http://www.shopbop.com/boutique-designer-boutique-clothes-jumpsuits-rompers/br/v=1/2534374302159489.htm",
        "http://www.shopbop.com/boutique-designer-boutique-clothes-lingerie/br/v=1/2534374302159486.htm",
        "http://www.shopbop.com/boutique-designer-boutique-clothes-pants/br/v=1/2534374302159491.htm",
        "http://www.shopbop.com/boutique-designer-boutique-clothes-shorts/br/v=1/2534374302159504.htm",
        "http://www.shopbop.com/boutique-designer-boutique-clothes-skirts/br/v=1/2534374302159469.htm",
        "http://www.shopbop.com/boutique-designer-boutique-clothes-suiting/br/v=1/2534374302159485.htm",
        "http://www.shopbop.com/boutique-designer-boutique-clothes-sweaters-knits/br/v=1/2534374302159490.htm",
        "http://www.shopbop.com/boutique-designer-boutique-clothes-swimwear/br/v=1/2534374302159508.htm",
        "http://www.shopbop.com/boutique-designer-boutique-clothes-tops/br/v=1/2534374302159473.htm",
        "http://www.shopbop.com/boutique-designer-clothing-vests/br/v=1/2534374302196672.htm",


        "http://www.shopbop.com/boutique-designer-boutique-shoes/br/v=1/2534374302159435.htm",
        "http://www.shopbop.com/boutique-designer-boutique-shoes-booties/br/v=1/2534374302159442.htm",
        "http://www.shopbop.com/boutique-designer-boutique-shoes-boots/br/v=1/2534374302159471.htm",
        "http://www.shopbop.com/boutique-designer-boutique-shoes-flats/br/v=1/2534374302159461.htm",
        "http://www.shopbop.com/boutique-designer-boutique-shoes-pumps-heels/br/v=1/2534374302159502.htm",
        "http://www.shopbop.com/boutique-designer-boutique-shoes-sandals/br/v=1/2534374302159466.htm",
        "http://www.shopbop.com/boutique-designer-boutique-shoes-sport/br/v=1/2534374302159470.htm",
        "http://www.shopbop.com/boutique-designer-boutique-shoes-clogs/br/v=1/13798.htm",

        "http://www.shopbop.com/boutique-designer-boutique-bags/br/v=1/2534374302159433.htm",
        "http://www.shopbop.com/boutique-designer-boutique-bags-backpacks/br/v=1/2534374302159440.htm",
        "http://www.shopbop.com/boutique-designer-boutique-bags-black-handbags/br/v=1/2534374302159446.htm",
        "http://www.shopbop.com/boutique-designer-boutique-bags-clutches/br/v=1/2534374302159510.htm",
        "http://www.shopbop.com/boutique-designer-boutique-bags-hobos/br/v=1/2534374302159511.htm",
        "http://www.shopbop.com/boutique-designer-boutique-bags-oversized/br/v=1/13810.htm",
        "http://www.shopbop.com/boutique-designer-boutique-bags-shoulder-bags/br/v=1/2534374302159454.htm",
        "http://www.shopbop.com/boutique-designer-boutique-bags-small-accessories/br/v=1/2534374302159449.htm",
        "http://www.shopbop.com/boutique-designer-boutique-bags-totes/br/v=1/2534374302159444.htm",
        "http://www.shopbop.com/boutique-designer-boutique-bags-wallets/br/v=1/2534374302159464.htm",
        "http://www.shopbop.com/boutique-designer-boutique-bags-weekend-bags/br/v=1/2534374302159467.htm",
        "http://www.shopbop.com/boutique-designer-bags-satchels/br/v=1/2534374302201401.htm",

        "http://www.shopbop.com/boutique-designer-accessories/br/v=1/2534374302159432.htm",
        "http://www.shopbop.com/boutique-designer-boutique-accessories-jewelry/br/v=1/2534374302159487.htm",
        "http://www.shopbop.com/boutique-designer-boutique-accessories-belts/br/v=1/2534374302159505.htm",
        "http://www.shopbop.com/boutique-designer-boutique-accessories-sunglasses/br/v=1/2534374302159451.htm",
        "http://www.shopbop.com/boutique-designer-boutique-accessories-gloves/br/v=1/2534374302159480.htm",
        "http://www.shopbop.com/boutique-designer-boutique-accessories-hair-accessories/br/v=1/2534374302159457.htm",
        "http://www.shopbop.com/boutique-designer-boutique-accessories-hats/br/v=1/2534374302159514.htm",
        "http://www.shopbop.com/boutique-designer-boutique-accessories-hosiery/br/v=1/2534374302159483.htm",
        "http://www.shopbop.com/boutique-designer-boutique-accessories-keychains/br/v=1/2534374302159455.htm",
        "http://www.shopbop.com/boutique-designer-boutique-accessories-scarves-wraps/br/v=1/2534374302159520.htm",
        "http://www.shopbop.com/boutique-designer-boutique-accessories-tech-accessories/br/v=1/2534374302159517.htm",


        #"http://www.shopbop.com/actions/designerindex/viewAlphabeticalDBDesigners.action",

        #"http://www.shopbop.com/ci/4/wedding/bridal-and-wedding-2013.html",
        "http://www.shopbop.com/boutique-wedding-dresses/br/v=1/2534374302183381.htm",
        "http://www.shopbop.com/boutique-wedding-dresses-line/br/v=1/2534374302206018.htm",
        "http://www.shopbop.com/boutique-wedding-dresses-ball-gown/br/v=1/2534374302206020.htm",
        "http://www.shopbop.com/boutique-wedding-dresses-sheath/br/v=1/2534374302206021.htm",
        "http://www.shopbop.com/boutique-wedding-dresses-short/br/v=1/2534374302206022.htm",
        "http://www.shopbop.com/boutique-wedding-dresses-trumpet-mermaid/br/v=1/2534374302206016.htm",

        "http://www.shopbop.com/boutique-wedding-bridesmaid-dresses/br/v=1/2534374302183382.htm",
        "http://www.shopbop.com/boutique-wedding-guest/br/v=1/21502.htm",
        "http://www.shopbop.com/boutique-wedding-lingerie/br/v=1/2534374302183600.htm",
        "http://www.shopbop.com/boutique-wedding-lingerie-day/br/v=1/27411.htm",
        "http://www.shopbop.com/boutique-wedding-lingerie-night/br/v=1/27412.htm",
        "http://www.shopbop.com/boutique-wedding-shoes/br/v=1/2534374302183603.htm",
        "http://www.shopbop.com/boutique-wedding-accessories/br/v=1/13851.htm",
        "http://www.shopbop.com/boutique-wedding-bags/br/v=1/2534374302183604.htm",
        "http://www.shopbop.com/boutique-wedding-hair-accessories/br/v=1/19541.htm",
        "http://www.shopbop.com/boutique-wedding-jewelry/br/v=1/2534374302183602.htm",
        "http://www.shopbop.com/boutique-wedding-bridal-party-gifts/br/v=1/13864.htm",

        "http://www.shopbop.com/boutique-editors-picks/br/v=1/2534374302205719.htm",
        "http://www.shopbop.com/boutiques-fashion-finds/br/v=1/28182.htm",
        "http://www.shopbop.com/boutiques-gift-boutique/br/v=1/2534374302207750.htm",
        "http://www.shopbop.com/boutique-holiday-gift-gifts-her/br/v=1/2534374302207761.htm",
        "http://www.shopbop.com/boutique-holiday-gift-gifts-her-bags/br/v=1/2534374302207769.htm",
        "http://www.shopbop.com/boutique-holiday-gift-gifts-her-jewelry/br/v=1/2534374302207771.htm",
        "http://www.shopbop.com/boutique-holiday-gift-gifts-her-accessories/br/v=1/2534374302207768.htm",
        "http://www.shopbop.com/boutique-holiday-gift-gifts-her-lingerie-sleepwear/br/v=1/2534374302207770.htm",

        "http://www.shopbop.com/boutique-holiday-gift-gifts-kids/br/v=1/2534374302207756.htm",
        "http://www.shopbop.com/boutique-holiday-gift-gifts-home/br/v=1/2534374302207757.htm",
        "http://www.shopbop.com/boutique-holiday-gift-gifts-100-under/br/v=1/2534374302207753.htm",

        "http://www.shopbop.com/boutiques-activewear-boutique/br/v=1/13924.htm",

        "http://www.shopbop.com/boutiques-activewear-tops/br/v=1/13931.htm",
        "http://www.shopbop.com/boutiques-activewear-bottoms/br/v=1/19552.htm",
        "http://www.shopbop.com/boutiques-activewear-boutique-swim-surf/br/v=1/13930.htm",
        "http://www.shopbop.com/boutiques-summer-sale-shoes/br/v=1/13934.htm",
        "http://www.shopbop.com/boutiques-activewear-bags/br/v=1/13925.htm",
        "http://www.shopbop.com/boutiques-activewear-accessories/br/v=1/13932.htm",

        "http://www.shopbop.com/one/br/v=1/2534374302182521.htm",
        "http://www.shopbop.com/one-clothing/br/v=1/2534374302182642.htm",

        "http://www.shopbop.com/one-clothing-jeans/br/v=1/2534374302182646.htm",
        "http://www.shopbop.com/one-clothing-dresses/br/v=1/2534374302182963.htm",
        "http://www.shopbop.com/one-clothing-jackets/br/v=1/2534374302192801.htm",
        "http://www.shopbop.com/one-clothing-jumpsuits-rompers/br/v=1/2534374302191862.htm",
        "http://www.shopbop.com/one-clothing-skirts/br/v=1/2534374302184425.htm",
        "http://www.shopbop.com/one-clothing-sweaters-knits/br/v=1/2534374302182644.htm",
        "http://www.shopbop.com/one-clothing-swimwear/br/v=1/2534374302184427.htm",
        "http://www.shopbop.com/one-clothing-tops/br/v=1/2534374302182648.htm",
        "http://www.shopbop.com/one-clothing-vests/br/v=1/2534374302196729.htm",

        "http://www.shopbop.com/one-shoes/br/v=1/2534374302182643.htm",
        "http://www.shopbop.com/one-shoes-winter-boots/br/v=1/33344.htm",
        "http://www.shopbop.com/one-shoes-booties/br/v=1/2534374302184426.htm",
        "http://www.shopbop.com/one-shoes-flats/br/v=1/2534374302187401.htm",

        "http://www.shopbop.com/one-bags/br/v=1/2534374302184421.htm",
        "http://www.shopbop.com/one-bags-backpacks/br/v=1/2534374302207838.htm",
        "http://www.shopbop.com/one-bags-black-handbags/br/v=1/2534374302196100.htm",
        "http://www.shopbop.com/one-bags-clutches/br/v=1/2534374302199760.htm",
        "http://www.shopbop.com/one-bags-cross-body/br/v=1/2534374302208232.htm",
        "http://www.shopbop.com/one-bags-oversized/br/v=1/10697.htm",
        "http://www.shopbop.com/one-bags-shoulder/br/v=1/2534374302184423.htm",
        "http://www.shopbop.com/one-bags-totes/br/v=1/2534374302184430.htm",

        "http://www.shopbop.com/one-accessories/br/v=1/2534374302182960.htm",
        "http://www.shopbop.com/one-accessories-belts/br/v=1/27338.htm",
        "http://www.shopbop.com/one-accessories-hats/br/v=1/21260.htm",
        "http://www.shopbop.com/one-accessories-jewelry/br/v=1/2534374302182961.htm",

        "http://www.shopbop.com/sale-one/br/v=1/2534374302187868.htm",
    ]

    # def parse(self, request):
    #     urls = response.xpath('//*[@id="leftNavigation"]/ul/li/a')

    def parse(self, response):
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
        product_class['name'] = "Boutiques"
        product_class['slug'] = "Boutiques".lower()
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