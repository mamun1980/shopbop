
def parse_product(self, response):
    # import pdb; pdb.set_trace()
    product = Product()
    product_class = ProductClass()
    product_cat = ProductCategory()
    
    cat_names = response.xpath('//*[@id="right-column"]/div[@class="breadcrumbs"]/ul/li')
    pclass = cat_names[0].xpath('span/text()').extract()[0].strip()
    product_class['name'] = pclass
    product_class['slug'] = pclass.lower()
    product_class['requires_shipping'] = True
    product_class['track_stock'] = True
    product['product_class'] = product_class
    
    if len(cat_names) > 1:
        cat_name = cat_names[-1]
        cat = cat_name.xpath('a/@title').extract()[0]
        product_cat['name'] = cat
        product['product_category'] = product_cat
    else:
        product['product_category'] = pclass
            


    pro_thumb_list = response.xpath('//*[@id="thumbnailList"]')
    pro_image_list = pro_thumb_list.xpath('li[@class="thumbnailListItem"]/img')
    product_images = []
    order = 0
    for pro_image in pro_image_list:
        product_image = ProductImage()
        img_url = pro_image.xpath('@src').extract()[0]
        product_image['shopbop_thumb_url'] = img_url
        small_image_url = img_url.replace("_37x65","_150x296")
        product_image['shopbop_small_image_url'] = small_image_url.replace("_q","_p")
        product_image['shopbop_image_url'] = img_url.replace("_37x65","_336x596")
        product_image['shopbop_big_image_url'] = img_url.replace("_37x65","")
        product_image['original'] = 'images/products/t-shirt2.png'
        product_image['display_order'] = order
        order = order + 1
        product_images.append(product_image)
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

    product_colors = []
    colors = response.xpath('//*[@id="swatches"]/img')
    for color in colors:
        pcolor = color.xpath('@class').extract()[0]
        color_classes = pcolor.split(" ")
        if not 'hide' == color_classes:
            product_color = ProductColor()
            product_color['color'] = color.xpath('@title').extract()[0]
            product_color['shopbop_color_thumnail_url'] = color.xpath('@src').extract()[0]
            product_colors.append(product_color)
    product['product_colors'] = product_colors

    sizenfit = SizeNFitItem()
    allfits = response.xpath('//*[@id="sizeFitContainer"]/node()').extract()
    fittext = ''
    for allfit in allfits:
        fittext = fittext + allfit
    sizenfit['fit'] = fittext
    product['size_n_fit'] = sizenfit

    
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
    
    price = path_product_price.xpath('meta[1]/@content').extract()[0].strip()
    product['price'] = price
    product['price_new'] = float(price[1:].replace(",",""))/2
    product['product_currency'] = path_product_price.xpath('meta[2]/@content').extract()[0].strip()

    return product