from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector
from shopbop.items import *
import re
# from shopbop.spiders.helper import parse_product


class ClothProductSpider(CrawlSpider):
    name = "product_cloth"
    allowed_domains = ["www.shopbop.com"]
    start_urls = [
        "http://www.shopbop.com/clothing-activewear/br/v=1/2534374302053051.htm",

        # "http://www.shopbop.com/clothing-dresses/br/v=1/2534374302063518.htm",

        # "http://www.shopbop.com/clothing-dresses-casual/br/v=1/2534374302072409.htm",
        # "http://www.shopbop.com/clothing-dresses-day-night/br/v=1/2534374302063657.htm",
        # "http://www.shopbop.com/clothing-dresses-night-out/br/v=1/2534374302152371.htm",
        # "http://www.shopbop.com/clothing-dresses-cocktail/br/v=1/2534374302063655.htm",
        # "http://www.shopbop.com/clothing-dresses-formal/br/v=1/2534374302204905.htm",
        # "http://www.shopbop.com/clothing-dresses-bridal/br/v=1/18902.htm",
        # "http://www.shopbop.com/clothing-dresses-black/br/v=1/2534374302063651.htm",
        # "http://www.shopbop.com/dresses-mini/br/v=1/2534374302063659.htm",
        # "http://www.shopbop.com/clothes-dresses-knee-length/br/v=1/2534374302100951.htm",
        # "http://www.shopbop.com/clothing-dresses-midi/br/v=1/2534374302204904.htm",
        # "http://www.shopbop.com/dresses-maxi/br/v=1/2534374302063654.htm",
        # "http://www.shopbop.com/clothing-dresses-strapless/br/v=1/2534374302204903.htm",
        # "http://www.shopbop.com/clothing-dresses-longsleeve/br/v=1/2534374302180265.htm",
        # "http://www.shopbop.com/dresses-designer-boutique/br/v=1/2534374302123309.htm",

        # "http://www.shopbop.com/clothing-jackets-coats/br/v=1/2534374302066271.htm",

        # "http://www.shopbop.com/clothing-jackets-coats-blazers/br/v=1/2534374302066388.htm",
        # "http://www.shopbop.com/clothing-jackets-coats/br/v=1/2534374302196584.htm",
        # "http://www.shopbop.com/clothing-jackets-coats-denim/br/v=1/2534374302066387.htm",
        # "http://www.shopbop.com/clothing-jackets-coats-down/br/v=1/2534374302196587.htm",
        # "http://www.shopbop.com/clothing-jackets-coats-fashion/br/v=1/2534374302066386.htm",
        # "http://www.shopbop.com/jackets-leather/br/v=1/2534374302101674.htm",
        # "http://www.shopbop.com/clothing-jackets-coats-pea/br/v=1/2534374302196586.htm",
        # "http://www.shopbop.com/clothing-jackets-coats-trench/br/v=1/2534374302196583.htm",
        # "http://www.shopbop.com/jackets-designer-boutique/br/v=1/2534374302124042.htm",


        # "http://www.shopbop.com/clothing-jeans/br/v=1/2534374302064814.htm",
        # "http://www.shopbop.com/clothing-jeans-ankle/br/v=1/32663.htm",
        # "http://www.shopbop.com/clothing-denim-boot-cut-jeans/br/v=1/2534374302064887.htm",
        # "http://www.shopbop.com/clothes-denim-boyfriend-jeans/br/v=1/2534374302121211.htm",
        # "http://www.shopbop.com/clothing-denim-cropped-jeans/br/v=1/2534374302064889.htm",
        # "http://www.shopbop.com/clothes-denim-distressed-jeans/br/v=1/2534374302101673.htm",
        # "http://www.shopbop.com/clothing-denim-flare-jeans-wide-leg/br/v=1/2534374302064886.htm",
        # "http://www.shopbop.com/clothes-denim-high-waisted-jeans/br/v=1/2534374302064882.htm",
        # "http://www.shopbop.com/clothes-denim-maternity-jeans/br/v=1/2534374302080360.htm",
        # "http://www.shopbop.com/clothes-denim-overalls/br/v=1/13390.htm",
        # "http://www.shopbop.com/clothing-jeans-relaxed-skinny/br/v=1/32664.htm",
        # "http://www.shopbop.com/clothes-denim-skinny-jeans/br/v=1/2534374302064885.htm",
        # "http://www.shopbop.com/clothes-denim-straight-leg-jeans/br/v=1/2534374302064884.htm",
        # "http://www.shopbop.com/clothing-denim-black-jeans/br/v=1/2534374302134251.htm",
        # "http://www.shopbop.com/clothes-denim-dark-rinse-jeans/br/v=1/2534374302079492.htm",
        # "http://www.shopbop.com/clothing-denim-grey-jeans/br/v=1/2534374302205678.htm",
        # "http://www.shopbop.com/clothes-denim-light-wash-jeans/br/v=1/2534374302079318.htm",
        # "http://www.shopbop.com/clothing-denim-white-jeans/br/v=1/2534374302079317.htm",
        # "http://www.shopbop.com/clothing-denim-coated-jeans/br/v=1/2534374302204237.htm",
        # "http://www.shopbop.com/clothing-denim-colored-jeans/br/v=1/2534374302204241.htm",
        # "http://www.shopbop.com/clothing-denim-printed-jeans/br/v=1/2534374302204239.htm",
        # "http://www.shopbop.com/clothing-denim-shorts/br/v=1/2534374302073699.htm",
        # "http://www.shopbop.com/clothes-denim-designer-boutique/br/v=1/2534374302126533.htm",

        # "http://www.shopbop.com/clothing-jumpsuits-rompers/br/v=1/2534374302034081.htm",
        # "http://www.shopbop.com/clothing-jumpsuits-rompers/br/v=1/32661.htm",
        # "http://www.shopbop.com/clothing-jumpsuits-rompers/br/v=1/32662.htm",

        # "http://www.shopbop.com/clothing-lingerie-sleepwear/br/v=1/2534374302049464.htm",
        # "http://www.shopbop.com/clothing-lingerie-sleepwear-bras/br/v=1/2534374302066122.htm",
        # "http://www.shopbop.com/clothing-lingerie-bras-bralette/br/v=1/33186.htm",
        # "http://www.shopbop.com/clothing-lingerie-bras-convertible/br/v=1/33187.htm",
        # "http://www.shopbop.com/clothing-lingerie-bras-push/br/v=1/33188.htm",
        # "http://www.shopbop.com/clothing-lingerie-bras-racerback/br/v=1/33189.htm",
        # "http://www.shopbop.com/clothing-lingerie-bras-sports/br/v=1/33190.htm",
        # "http://www.shopbop.com/clothing-lingerie-bras-strapless/br/v=1/33191.htm",
        # "http://www.shopbop.com/clothing-lingerie-bras-shirt/br/v=1/33192.htm",
        # "http://www.shopbop.com/clothing-lingerie-bras-underwire/br/v=1/33193.htm",
        # "http://www.shopbop.com/clothing-lingerie-camisoles/br/v=1/2534374302066121.htm",
        # "http://www.shopbop.com/clothing-lingerie-chemises-slips/br/v=1/2534374302066120.htm",
        # "http://www.shopbop.com/clothing-lingerie-garters/br/v=1/2534374302186020.htm",

        # "http://www.shopbop.com/clothing-lingerie-sleepwear-panties/br/v=1/2534374302066119.htm",
        # "http://www.shopbop.com/clothing-lingerie-panties-bikini-brief/br/v=1/33194.htm",
        # "http://www.shopbop.com/clothing-lingerie-panties-sets/br/v=1/33195.htm",
        # "http://www.shopbop.com/clothing-lingerie-panties-thong/br/v=1/33196.htm",
        # "http://www.shopbop.com/clothing-lingerie-robes/br/v=1/2534374302178458.htm",
        # "http://www.shopbop.com/lingerie-shapewear/br/v=1/2534374302177903.htm",
        # "http://www.shopbop.com/clothing-lingerie-sleepwear/br/v=1/2534374302066118.htm",
        # "http://www.shopbop.com/clothing-lingerie-teddies/br/v=1/2534374302178459.htm",
        # "http://www.shopbop.com/clothing-lingerie-accessories/br/v=1/2534374302153631.htm",
        # "http://www.shopbop.com/lingerie-designer-boutique/br/v=1/2534374302123294.htm",
        # "http://www.shopbop.com/clothing-maternity/br/v=1/2534374302172178.htm",

        # "http://www.shopbop.com/clothing-pants-leggings/br/v=1/2534374302024611.htm",
        # "http://www.shopbop.com/clothing-pants-boot-cut-flare/br/v=1/2534374302180154.htm",
        # "http://www.shopbop.com/clothing-pants-cropped/br/v=1/2534374302070476.htm",
        # "http://www.shopbop.com/clothing-pants-high-waisted/br/v=1/2534374302196585.htm",
        # "http://www.shopbop.com/clothing-pants-leather/br/v=1/2534374302180153.htm",
        # "http://www.shopbop.com/clothing-pants-leggings/br/v=1/13287.htm",
        # "http://www.shopbop.com/clothing-pants-leggings-maternity/br/v=1/2534374302179422.htm",
        # "http://www.shopbop.com/clothing-pants-skinny/br/v=1/2534374302067314.htm",
        # "http://www.shopbop.com/clothing-pants-leggings-slouchy/br/v=1/2534374302159448.htm",
        # "http://www.shopbop.com/clothing-pants-straight-leg/br/v=1/2534374302180155.htm",
        # "http://www.shopbop.com/clothing-pants-leggings-sweatpants/br/v=1/2534374302180202.htm",
        # "http://www.shopbop.com/clothing-pants-wide-leg/br/v=1/2534374302067313.htm",
        # "http://www.shopbop.com/pants-designer-boutique/br/v=1/2534374302123357.htm",

        # "http://www.shopbop.com/clothing-shorts/br/v=1/2534374302024684.htm",
        # "http://www.shopbop.com/clothing-shorts-denim/br/v=1/2534374302079172.htm",
        # "http://www.shopbop.com/clothing-shorts-knee-length/br/v=1/2534374302067140.htm",
        # "http://www.shopbop.com/clothing-shorts-short/br/v=1/2534374302067141.htm",

        # "http://www.shopbop.com/clothing-skirts/br/v=1/2534374302024619.htm",
        # "http://www.shopbop.com/skirts-mini/br/v=1/2534374302149758.htm",
        # "http://www.shopbop.com/clothing-skirts-knee-length/br/v=1/2534374302070727.htm",
        # "http://www.shopbop.com/clothing-skirts-midi/br/v=1/2534374302182060.htm",
        # "http://www.shopbop.com/skirts-maxi/br/v=1/2534374302150097.htm",
        # "http://www.shopbop.com/clothing-skirts-dress/br/v=1/2534374302084993.htm",
        # "http://www.shopbop.com/skirts-pencil/br/v=1/2534374302150100.htm",
        # "http://www.shopbop.com/clothing-skirts-denim/br/v=1/2534374302079171.htm",
        # "http://www.shopbop.com/skirts-designer-boutique/br/v=1/2534374302123359.htm",

        # "http://www.shopbop.com/clothing-suit-separates/br/v=1/2534374302063184.htm",

        # "http://www.shopbop.com/clothing-sweaters-knits/br/v=1/2534374302024636.htm",
        # "http://www.shopbop.com/clothing-sweaters-knits-cardigans/br/v=1/2534374302069137.htm",
        # "http://www.shopbop.com/sweaters-knits-cashmere/br/v=1/2534374302069136.htm",
        # "http://www.shopbop.com/clothing-sweaters-cowlneck/br/v=1/2534374302192440.htm",
        # "http://www.shopbop.com/clothing-sweaters-knits-crew-scoop-necks/br/v=1/2534374302069135.htm",
        # "http://www.shopbop.com/clothing-sweaters-knits-sweater-dresses/br/v=1/2534374302182061.htm",
        # "http://www.shopbop.com/clothing-sweaters-knits-turtlenecks/br/v=1/2534374302069131.htm",
        # "http://www.shopbop.com/clothing-sweaters-knits-necks/br/v=1/2534374302069130.htm",
        # "http://www.shopbop.com/sweaters-knits-designer-boutique/br/v=1/2534374302123878.htm",

        # "http://www.shopbop.com/clothing-swimwear/br/v=1/2534374302024726.htm",
        # "http://www.shopbop.com/clothing-swimwear-bikinis/br/v=1/2534374302067620.htm",
        # "http://www.shopbop.com/clothes-swimwear-bikinis-tops/br/v=1/31001.htm",
        # "http://www.shopbop.com/clothes-swimwear-bikinis-bottoms/br/v=1/31002.htm",
        # "http://www.shopbop.com/clothes-swimwear-bikinis-sets/br/v=1/31003.htm",
        # "http://www.shopbop.com/clothes-swimwear-cover-ups/br/v=1/2534374302067619.htm",
        # "http://www.shopbop.com/clothes-swimwear-one-pieces/br/v=1/2534374302067618.htm",

        # "http://www.shopbop.com/clothing-tops/br/v=1/2534374302060562.htm",
        # "http://www.shopbop.com/clothing-tops-blouses/br/v=1/2534374302060711.htm",
        # "http://www.shopbop.com/clothes-tops-button-down-shirts/br/v=1/2534374302150953.htm",
        # "http://www.shopbop.com/clothing-tops-crop/br/v=1/32075.htm",
        # "http://www.shopbop.com/clothing-tops-graphic-tees/br/v=1/32076.htm",
        # "http://www.shopbop.com/clothing-tops-night-out/br/v=1/2534374302072624.htm",
        # "http://www.shopbop.com/clothing-tops-sweatshirts-hoodies/br/v=1/2534374302060709.htm",
        # "http://www.shopbop.com/clothing-tops-tank/br/v=1/2534374302060705.htm",
        # "http://www.shopbop.com/clothing-tops-short-sleeve-tees/br/v=1/2534374302060706.htm",
        # "http://www.shopbop.com/clothing-tops-tees-short-sleeve-crew-neck/br/v=1/32061.htm",
        # "http://www.shopbop.com/clothing-tops-tees-short-sleeve-scoop-neck/br/v=1/32062.htm",
        # "http://www.shopbop.com/clothing-tops-tees-short-sleeve-neck/br/v=1/32063.htm",

        # "http://www.shopbop.com/clothing-tops-long-sleeve-tees/br/v=1/2534374302060707.htm",
        # "http://www.shopbop.com/clothing-tops-tees-long-sleeve-crew-neck/br/v=1/32072.htm",
        # "http://www.shopbop.com/clothing-tops-tees-long-sleeve-scoop-neck/br/v=1/32073.htm",
        # "http://www.shopbop.com/clothing-tops-tees-long-sleeve-neck/br/v=1/32074.htm",

        # "http://www.shopbop.com/clothing-tops-tunics/br/v=1/2534374302060703.htm",
        # "http://www.shopbop.com/clothes-tops-designer-boutique/br/v=1/2534374302123326.htm",

        # "http://www.shopbop.com/clothing-vests/br/v=1/2534374302196580.htm",
        # "http://www.shopbop.com/clothing-kids-baby/br/v=1/28501.htm",
        
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