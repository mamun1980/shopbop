from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector
from shopbop.items import *
import re
class ClothProductSpider(CrawlSpider):
    name = "product_sale"
    allowed_domains = ["www.shopbop.com"]
    start_urls = [
        "http://www.shopbop.com/new-to-sale/br/v=1/2534374302175438.htm",

        "http://www.shopbop.com/sale-clothes-denim-all-jeans/br/v=1/2534374302076379.htm",
        "http://www.shopbop.com/sale-clothes-denim-boot-cut-jeans/br/v=1/2534374302076380.htm",
        "http://www.shopbop.com/sale-clothes-denim-boyfriend-jeans/br/v=1/2534374302127693.htm",
        "http://www.shopbop.com/sale-clothes-denim-cropped-jeans/br/v=1/2534374302076348.htm",
        "http://www.shopbop.com/sale-clothes-denim-designer-boutique/br/v=1/2534374302152227.htm",
        "http://www.shopbop.com/sale-clothes-denim-distressed-jeans/br/v=1/2534374302101970.htm",
        "http://www.shopbop.com/sale-clothing-denim-flare-jeans-wide-leg/br/v=1/2534374302076383.htm",
        "http://www.shopbop.com/sale-clothes-denim-high-waisted-jeans/br/v=1/2534374302076384.htm",
        "http://www.shopbop.com/sale-clothes-denim-maternity-jeans/br/v=1/2534374302118204.htm",
        "http://www.shopbop.com/sale-clothes-denim-skinny-jeans/br/v=1/2534374302076387.htm",
        "http://www.shopbop.com/sale-clothes-denim-straight-leg-jeans/br/v=1/2534374302076388.htm",
        "http://www.shopbop.com/sale-clothing-denim-black-jeans/br/v=1/2534374302134911.htm",
        "http://www.shopbop.com/sale-clothes-denim-dark-rinse-jeans/br/v=1/2534374302076382.htm",
        "http://www.shopbop.com/sale-clothing-denim-grey-jeans/br/v=1/2534374302206382.htm",
        "http://www.shopbop.com/sale-clothes-denim-light-wash-jeans/br/v=1/2534374302079474.htm",
        "http://www.shopbop.com/sale-clothing-denim-white-jeans/br/v=1/2534374302079475.htm",
        "http://www.shopbop.com/sale-clothes-denim-jackets/br/v=1/2534374302078365.htm",
        "http://www.shopbop.com/sale-clothes-denim-overalls/br/v=1/2534374302076409.htm",
        "http://www.shopbop.com/sale-clothing-jeans-ankle/br/v=1/32866.htm",
        "http://www.shopbop.com/sale-clothing-jeans-relaxed-skinny/br/v=1/33043.htm",
        "http://www.shopbop.com/sale-clothing-denim-coated/br/v=1/2534374302204265.htm",
        "http://www.shopbop.com/sale-clothing-denim-colored/br/v=1/2534374302204263.htm",
        "http://www.shopbop.com/sale-clothing-denim-printed/br/v=1/2534374302204264.htm",
        "http://www.shopbop.com/sale-clothes-denim-shorts/br/v=1/2534374302076420.htm",

        "http://www.shopbop.com/sale-clothing-denim/br/v=1/2534374302076347.htm",
        "http://www.shopbop.com/sale-dresses-casual/br/v=1/2534374302076333.htm",
        "http://www.shopbop.com/sale-dresses-day-night/br/v=1/2534374302076349.htm",
        "http://www.shopbop.com/sale-clothing-dresses-night-out/br/v=1/2534374302161925.htm",
        "http://www.shopbop.com/sale-clothing-dresses-cocktail/br/v=1/2534374302076361.htm",
        "http://www.shopbop.com/sale-clothing-dresses-formal/br/v=1/2534374302204927.htm",
        "http://www.shopbop.com/sale-dresses-designer-boutique/br/v=1/2534374302124464.htm",
        "http://www.shopbop.com/sale-clothing-dresses-bright/br/v=1/2534374302077005.htm",
        "http://www.shopbop.com/sale-clothing-dresses-black/br/v=1/2534374302076441.htm",
        "http://www.shopbop.com/sale-clothing-dresses-white/br/v=1/2534374302092845.htm",
        "http://www.shopbop.com/sale-dresses-mini/br/v=1/2534374302076404.htm",
        "http://www.shopbop.com/sale-clothes-dresses-knee-length/br/v=1/2534374302101955.htm",
        "http://www.shopbop.com/sale-clothing-dresses-midi/br/v=1/2534374302204930.htm",
        "http://www.shopbop.com/sale-dresses-maxi/br/v=1/2534374302076400.htm",
        "http://www.shopbop.com/sale-clothing-dresses-strapless/br/v=1/2534374302204928.htm",
        "http://www.shopbop.com/sale-clothing-dresses-one-shoulder/br/v=1/2534374302161930.htm",
        "http://www.shopbop.com/sale-clothing-dresses-longsleeve/br/v=1/2534374302180280.htm",
        "http://www.shopbop.com/sale-clothing-dresses-bridal/br/v=1/18912.htm",

        "http://www.shopbop.com/sale-clothing-dresses/br/v=1/2534374302076332.htm",
        "http://www.shopbop.com/sale-jackets-blazers/br/v=1/2534374302076314.htm",
        "http://www.shopbop.com/sale-clothing-jackets-coats/br/v=1/2534374302196760.htm",
        "http://www.shopbop.com/sale-jackets-denim/br/v=1/2534374302078366.htm",
        "http://www.shopbop.com/sale-jackets-designer-boutique/br/v=1/2534374302124460.htm",
        "http://www.shopbop.com/sale-jackets-fashion/br/v=1/2534374302076362.htm",
        "http://www.shopbop.com/sale-jackets-leather/br/v=1/2534374302101962.htm",
        "http://www.shopbop.com/sale-clothing-jackets-coats-pea/br/v=1/2534374302196764.htm",
        "http://www.shopbop.com/sale-clothing-jackets-coats-puffer/br/v=1/2534374302196763.htm",
        "http://www.shopbop.com/sale-clothing-jackets-coats-trench/br/v=1/2534374302196761.htm",

        "http://www.shopbop.com/sale-clothing-jackets-coats/br/v=1/2534374302076313.htm",
        "http://www.shopbop.com/sale-clothing-jumpsuits-rompers/br/v=1/32865.htm",
        "http://www.shopbop.com/sale-clothing-jumpsuits-rompers/br/v=1/32673.htm",
        "http://www.shopbop.com/sale-designer-boutique/br/v=1/17768.htm",

        "http://www.shopbop.com/sale-jumpsuits-rompers/br/v=1/2534374302076393.htm",
        "http://www.shopbop.com/sale-lingerie-bras/br/v=1/2534374302076323.htm",
        "http://www.shopbop.com/sale-lingerie-camisoles/br/v=1/2534374302076325.htm",
        "http://www.shopbop.com/sale-clothing-lingerie-chemise/br/v=1/2534374302076342.htm",
        "http://www.shopbop.com/sale-lingerie-designer-boutique/br/v=1/2534374302124485.htm",
        "http://www.shopbop.com/sale-lingerie-garters/br/v=1/2534374302186120.htm",
        "http://www.shopbop.com/sale-lingerie-panties/br/v=1/2534374302076410.htm",
        "http://www.shopbop.com/sale-clothes-lingerie-robes/br/v=1/2534374302178489.htm",
        "http://www.shopbop.com/sale-lingerie-shapewear/br/v=1/2534374302180060.htm",
        "http://www.shopbop.com/sale-clothing-lingerie-sleepwear/br/v=1/2534374302076425.htm",
        "http://www.shopbop.com/sale-clothes-lingerie-teddies/br/v=1/2534374302178841.htm",

        "http://www.shopbop.com/sale-clothing-loungewear/br/v=1/2534374302076463.htm",

        "http://www.shopbop.com/sale-clothing-maternity/br/v=1/2534374302172238.htm",

        "http://www.shopbop.com/sale-clothing-lingerie/br/v=1/2534374302076322.htm",
        "http://www.shopbop.com/sale-clothing-pants-boot-cut-flare/br/v=1/2534374302180230.htm",
        "http://www.shopbop.com/sale-cropped-pants/br/v=1/2534374302076326.htm",
        "http://www.shopbop.com/sale-pants-designer-boutique/br/v=1/2534374302124476.htm",
        "http://www.shopbop.com/sale-clothing-pants-leggings/br/v=1/23481.htm",
        "http://www.shopbop.com/sale-clothing-pants-high-waisted/br/v=1/2534374302197400.htm",
        "http://www.shopbop.com/sale-clothing-pants-leather/br/v=1/2534374302180181.htm",
        "http://www.shopbop.com/sale-clothing-pants-skinny/br/v=1/2534374302076335.htm",
        "http://www.shopbop.com/sale-clothing-pants-straight-leg/br/v=1/2534374302180180.htm",
        "http://www.shopbop.com/sale-clothing-pants-sweatpants-yoga/br/v=1/2534374302180229.htm",
        "http://www.shopbop.com/sale-clothing-pants-wide-leg/br/v=1/2534374302076353.htm",

        "http://www.shopbop.com/sale-clothing-pants/br/v=1/2534374302076334.htm",
        "http://www.shopbop.com/sale-clothes-shorts-denim/br/v=1/2534374302079311.htm",
        "http://www.shopbop.com/sale-clothes-shorts-designer-boutique/br/v=1/2534374302152219.htm",
        "http://www.shopbop.com/sale-clothing-shorts-knee-length/br/v=1/2534374302076354.htm",
        "http://www.shopbop.com/sale-clothing-shorts-short/br/v=1/2534374302076337.htm",

        "http://www.shopbop.com/sale-clothing-shorts/br/v=1/2534374302076336.htm",
        "http://www.shopbop.com/sale-skirts-mini/br/v=1/2534374302150313.htm",
        "http://www.shopbop.com/sale-clothing-skirts-knee-length/br/v=1/2534374302076339.htm",
        "http://www.shopbop.com/sale-clothing-skirts-midi/br/v=1/2534374302182251.htm",
        "http://www.shopbop.com/sale-skirts-maxi/br/v=1/2534374302150317.htm",
        "http://www.shopbop.com/sale-clothing-skirts-dress/br/v=1/2534374302076355.htm",
        "http://www.shopbop.com/sale-skirts-pencil/br/v=1/2534374302150311.htm",
        "http://www.shopbop.com/sale-skirts-denim/br/v=1/2534374302079310.htm",
        "http://www.shopbop.com/sale-skirts-designer-boutique/br/v=1/2534374302124482.htm",

        "http://www.shopbop.com/sale-clothing-suit-separates/br/v=1/2534374302076430.htm",

        "http://www.shopbop.com/sale-clothing-skirts/br/v=1/2534374302076338.htm",
        "http://www.shopbop.com/sale-sweaters-knits-cardigans/br/v=1/2534374302077052.htm",
        "http://www.shopbop.com/sale-sweaters-knits-cashmere/br/v=1/2534374302077043.htm",
        "http://www.shopbop.com/sale-clothing-sweaters-cowlneck/br/v=1/2534374302192460.htm",
        "http://www.shopbop.com/sale-sweaters-knits-crew-scoop-necks/br/v=1/2534374302077047.htm",
        "http://www.shopbop.com/sale-sweaters-knits-designer-boutique/br/v=1/2534374302124480.htm",
        "http://www.shopbop.com/sale-sweaters-knits-sweater-dresses/br/v=1/2534374302077042.htm",
        "http://www.shopbop.com/sale-sweaters-knits-turtlenecks/br/v=1/2534374302077050.htm",
        "http://www.shopbop.com/sale-sweaters-knits-v-necks/br/v=1/2534374302077044.htm",

        "http://www.shopbop.com/sale-clothing-sweaters-knits/br/v=1/2534374302077034.htm",
        "http://www.shopbop.com/sale-clothes-swimwear/br/v=1/2534374302076309.htm",
        "http://www.shopbop.com/sale-swimwear-bikinis/br/v=1/2534374302076310.htm",
        "http://www.shopbop.com/sale-swimwear-cover-ups/br/v=1/2534374302076345.htm",
        "http://www.shopbop.com/sale-swimwear-designer-boutique/br/v=1/2534374302171239.htm",
        "http://www.shopbop.com/sale-swimwear-one-pieces/br/v=1/2534374302076407.htm",

        "http://www.shopbop.com/sale-clothing-tops/br/v=1/2534374302076315.htm",
        "http://www.shopbop.com/sale-clothes-tops-blouses/br/v=1/2534374302076316.htm",
        "http://www.shopbop.com/sale-clothes-tops-designer-boutique/br/v=1/2534374302125920.htm",
        "http://www.shopbop.com/sale-clothing-tops-night-out/br/v=1/2534374302076417.htm",
        "http://www.shopbop.com/sale-clothes-tops-sweatshirts-hoodies/br/v=1/2534374302076447.htm",
        "http://www.shopbop.com/sale-clothes-tops-tank/br/v=1/2534374302076475.htm",
        "http://www.shopbop.com/sale-clothes-tops-tees-long-sleeve/br/v=1/2534374302076439.htm",
        "http://www.shopbop.com/sale-clothes-tops-tees-short-sleeve/br/v=1/2534374302076440.htm",
        "http://www.shopbop.com/sale-clothes-tops-tunics/br/v=1/2534374302076449.htm",
        "http://www.shopbop.com/sale-clothing-tops-crop/br/v=1/32118.htm",
        "http://www.shopbop.com/sale-clothing-tops-graphic-tees/br/v=1/32238.htm",

        "http://www.shopbop.com/sale-clothing-kids-baby/br/v=1/30833.htm",

        "http://www.shopbop.com/sale-clothing-vests/br/v=1/2534374302196762.htm"
        "http://www.shopbop.com/sale-clothing-vests-designer-boutique/br/v=1/2534374302196766.htm",

        "http://www.shopbop.com/sale-designer-boutique/br/v=1/17752.htm",

        #"http://www.shopbop.com/sale-bags/br/v=1/2534374302076306.htm",

        "http://www.shopbop.com/sale-bags-backpacks/br/v=1/2534374302076307.htm",
        "http://www.shopbop.com/sale-bags-beach/br/v=1/2534374302161924.htm",
        "http://www.shopbop.com/sale-bags-black-handbags/br/v=1/2534374302122243.htm",
        "http://www.shopbop.com/sale-bags-clutches/br/v=1/2534374302076343.htm",
        "http://www.shopbop.com/sale-bags-cosmetic-pouches/br/v=1/2534374302076428.htm",
        "http://www.shopbop.com/sale-bags-cross-body/br/v=1/2534374302076403.htm",
        "http://www.shopbop.com/sale-bags/br/v=1/2534374302076306.htm",
        "http://www.shopbop.com/sale-bags-hobos/br/v=1/2534374302150472.htm",
        "http://www.shopbop.com/sale-bags-oversized/br/v=1/2534374302161932.htm",
        "http://www.shopbop.com/sale-bags-satchels/br/v=1/2534374302178488.htm",
        "http://www.shopbop.com/sale-bags-shoulder/br/v=1/2534374302076421.htm",
        "http://www.shopbop.com/sale-bags-totes/br/v=1/2534374302076445.htm",
        "http://www.shopbop.com/sale-bags-wallets/br/v=1/2534374302076458.htm",
        "http://www.shopbop.com/sale-bags-weekend/br/v=1/2534374302076460.htm",

        #"http://www.shopbop.com/sale-shoes/br/v=1/2534374302076317.htm",

        "http://www.shopbop.com/sale-shoes-booties/br/v=1/2534374302076318.htm",
        "http://www.shopbop.com/sale-shoes-booties-flat/br/v=1/2534374302161944.htm",
        "http://www.shopbop.com/sale-shoes-booties-heeled/br/v=1/2534374302161942.htm",
        "http://www.shopbop.com/sale-shoes-booties-lace/br/v=1/2534374302192241.htm",
        "http://www.shopbop.com/sale-designer-boutique/br/v=1/17758.htm",

        "http://www.shopbop.com/sale-shoes-boots/br/v=1/2534374302076319.htm",
        "http://www.shopbop.com/sale-shoes-boots-flat/br/v=1/2534374302076363.htm",
        "http://www.shopbop.com/sale-shoes-boots-heeled/br/v=1/2534374302161940.htm",
        "http://www.shopbop.com/sale-shoes-boots-knee-high/br/v=1/2534374302161941.htm",
        "http://www.shopbop.com/sale-shoes-boots-over-knee/br/v=1/2534374302166535.htm",

        "http://www.shopbop.com/sale-shoes-clogs/br/v=1/2534374302126734.htm",
        "http://www.shopbop.com/sale-shoes-designer-boutique/br/v=1/2534374302125922.htm",

        "http://www.shopbop.com/sale-shoes-flats/br/v=1/2534374302076364.htm",
        "http://www.shopbop.com/sale-shoes-flats-espadrilles/br/v=1/28103.htm",
        "http://www.shopbop.com/sale-shoes-flats-ballet/br/v=1/2534374302201820.htm",
        "http://www.shopbop.com/sale-shoes-flats-loafers/br/v=1/2534374302201821.htm",
        "http://www.shopbop.com/sale-shoes-flats-oxfords/br/v=1/2534374302201822.htm",

        "http://www.shopbop.com/sale-shoes-pumps/br/v=1/2534374302076413.htm",
        "http://www.shopbop.com/sale-shoes-pumps-heels/br/v=1/2534374302163691.htm",
        "http://www.shopbop.com/sale-shoes-pumps-heels-open-toe/br/v=1/2534374302161929.htm",
        "http://www.shopbop.com/sale-shoes-pumps-heels-platforms/br/v=1/2534374302161922.htm",
        "http://www.shopbop.com/sale-designer-boutique/br/v=1/17754.htm",
        "http://www.shopbop.com/sale-shoes-sandals/br/v=1/2534374302076415.htm",
        "http://www.shopbop.com/sale-shoes-sandals-flat/br/v=1/2534374302079289.htm",
        "http://www.shopbop.com/sale-shoes-flip-flops/br/v=1/2534374302076365.htm",
        "http://www.shopbop.com/sale-shoes-sandals-high-heeled/br/v=1/2534374302079476.htm",
        "http://www.shopbop.com/sale-shoes-sandals-platforms/br/v=1/2534374302161920.htm",
        "http://www.shopbop.com/sale-designer-boutique/br/v=1/17755.htm",
        "http://www.shopbop.com/sale-shoes-cold-weather-rain-wear/br/v=1/28341.htm",
        "http://www.shopbop.com/sale-shoes-sport/br/v=1/2534374302076429.htm",
        "http://www.shopbop.com/sale-shoes-sneakers-high-top/br/v=1/31241.htm",
        "http://www.shopbop.com/sale-shoes-sneakers-low-top/br/v=1/31244.htm",
        "http://www.shopbop.com/sale-shoes-sneakers-slip/br/v=1/31247.htm",
        "http://www.shopbop.com/sale-designer-boutique/br/v=1/17772.htm",
        "http://www.shopbop.com/sale-shoes-trend-combat-moto/br/v=1/32592.htm",
        "http://www.shopbop.com/sale-shoes-trend-nude/br/v=1/32151.htm",
        "http://www.shopbop.com/sale-shoes-trend-shearling-fur/br/v=1/33332.htm",

        "http://www.shopbop.com/sale-accessories-jewelry/br/v=1/2534374302076320.htm",
        "http://www.shopbop.com/sale-accessories-jewelry-bracelets/br/v=1/2534374302076321.htm",
        "http://www.shopbop.com/sale-accessories-jewelry-charms/br/v=1/2534374302076341.htm",
        "http://www.shopbop.com/sale-accessories-jewelry-designer-boutique/br/v=1/2534374302124493.htm",
        "http://www.shopbop.com/sale-accessories-jewelry-earrings/br/v=1/2534374302076357.htm",
        "http://www.shopbop.com/sale-accessories-jewelry-fine/br/v=1/19441.htm",
        "http://www.shopbop.com/sale-accessories-jewelry-necklaces/br/v=1/2534374302076406.htm",
        "http://www.shopbop.com/sale-accessories-jewelry-other/br/v=1/2534374302150312.htm",
        "http://www.shopbop.com/sale-accessories-jewelry-rings/br/v=1/2534374302076414.htm",
        "http://www.shopbop.com/sale-accessories-belts/br/v=1/2534374302076308.htm",
        "http://www.shopbop.com/sale-designer-boutique/br/v=1/17762.htm",
        "http://www.shopbop.com/sale-accessories-designer-boutique/br/v=1/2534374302124468.htm",
        "http://www.shopbop.com/sale-accessories-eyewear/br/v=1/2534374302076432.htm",
        "http://www.shopbop.com/sale-accessories-sunglasses-eyewear-aviator/br/v=1/20062.htm",
        "http://www.shopbop.com/sale-accessories-sunglasses-eyewear-cat-eye/br/v=1/20063.htm",
        "http://www.shopbop.com/sale-accessories-sunglasses-eyewear-mirrored/br/v=1/20981.htm",
        "http://www.shopbop.com/sale-accessories-sunglasses-eyewear-oversized/br/v=1/20061.htm",
        "http://www.shopbop.com/sale-accessories-sunglasses-eyewear-rectangle/br/v=1/20064.htm",
        "http://www.shopbop.com/sale-accessories-sunglasses-eyewear-special-fit/br/v=1/31961.htm",
        "http://www.shopbop.com/sale-accessories-sunglasses-eyewear-round/br/v=1/20065.htm",
        "http://www.shopbop.com/sale-accessories-sunglasses-eyewear-statement/br/v=1/20066.htm",
        "http://www.shopbop.com/sale-accessories-eyewear/br/v=1/2534374302076432.htm",
        "http://www.shopbop.com/sale-accessories-eyewear-cases/br/v=1/20963.htm",
        "http://www.shopbop.com/sale-designer-boutique/br/v=1/17761.htm",
        "http://www.shopbop.com/sale-accessories-hair/br/v=1/2534374302076371.htm",
        "http://www.shopbop.com/sale-accessories-hats/br/v=1/2534374302076374.htm",
        "http://www.shopbop.com/sale-accessories-home-gifts/br/v=1/2534374302199565.htm",
        "http://www.shopbop.com/sale-accessories-home-gifts-dog/br/v=1/32587.htm",
        "http://www.shopbop.com/sale-accessories-home-gifts-entertaining/br/v=1/30499.htm",
        "http://www.shopbop.com/sale-accessories-home-gifts-decor/br/v=1/29062.htm",
        "http://www.shopbop.com/sale-accessories-home-gifts-stationary/br/v=1/29063.htm",
        "http://www.shopbop.com/sale-accessories-home-gifts-books/br/v=1/29021.htm",
        "http://www.shopbop.com/sale-accessories-home-gifts-towels/br/v=1/29447.htm",
        "http://www.shopbop.com/sale-hosiery/br/v=1/2534374302076376.htm",
        "http://www.shopbop.com/sale-hosiery-tights/br/v=1/2534374302079302.htm",
        "http://www.shopbop.com/sale-accessories-keychains/br/v=1/2534374302076394.htm",
        "http://www.shopbop.com/sale-designer-boutique/br/v=1/17782.htm",
        "http://www.shopbop.com/sale-accessories-scarves-wraps/br/v=1/2534374302076416.htm",
        "http://www.shopbop.com/sale-accessories-tech/br/v=1/2534374302117102.htm",
        "http://www.shopbop.com/sale-accessories-tech-laptop/br/v=1/2534374302203320.htm",
        "http://www.shopbop.com/sale-accessories-tech-phone/br/v=1/2534374302203322.htm",
        "http://www.shopbop.com/sale-accessories-tech-tablet-reader/br/v=1/2534374302203321.htm",
        "http://www.shopbop.com/sale-accessories-jewelry-edit-fall-2013/br/v=1/22061.htm",
        "http://www.shopbop.com/sale-jewelry-watches/br/v=1/2534374302108677.htm",
        "http://www.shopbop.com/sale-accessories-winter/br/v=1/2534374302198040.htm",

        "http://www.shopbop.com/sale-shopbop-designer-boutique/br/v=1/2534374302123476.htm",
        "http://www.shopbop.com/sale-boutique-designer-boutique-clothes/br/v=1/2534374302161958.htm",
        "http://www.shopbop.com/sale-boutique-designer-boutique-clothes-denim/br/v=1/2534374302161987.htm",
        "http://www.shopbop.com/sale-boutique-designer-boutique-clothes-dresses/br/v=1/2534374302161967.htm",
        "http://www.shopbop.com/sale-boutique-designer-boutique-clothes-jackets/br/v=1/2534374302161968.htm",
        "http://www.shopbop.com/sale-boutique-designer-boutique-clothes-jumpsuits-rompers/br/v=1/2534374302161984.htm",
        "http://www.shopbop.com/sale-boutique-designer-boutique-clothes-lingerie/br/v=1/2534374302161971.htm",
        "http://www.shopbop.com/sale-boutique-designer-boutique-clothes-pants/br/v=1/2534374302161972.htm",
        "http://www.shopbop.com/sale-boutique-designer-boutique-clothes-shorts/br/v=1/2534374302161979.htm",
        "http://www.shopbop.com/sale-boutique-designer-boutique-clothes-skirts/br/v=1/2534374302161959.htm",
        "http://www.shopbop.com/sale-boutique-designer-boutique-clothes-sweaters-knits/br/v=1/2534374302161970.htm",
        "http://www.shopbop.com/sale-boutique-designer-boutique-clothes-swimwear/br/v=1/2534374302171238.htm",
        "http://www.shopbop.com/sale-boutique-designer-boutique-clothes-tops/br/v=1/2534374302161969.htm",
        "http://www.shopbop.com/sale-boutique-designer-clothing-vests/br/v=1/2534374302196765.htm",
        "http://www.shopbop.com/sale-boutique-designer-boutique-shoes/br/v=1/2534374302161954.htm",
        "http://www.shopbop.com/sale-boutique-designer-boutique-shoes-booties/br/v=1/2534374302161974.htm",
        "http://www.shopbop.com/sale-boutique-designer-boutique-shoes-pumps-heels/br/v=1/2534374302161955.htm",
        "http://www.shopbop.com/sale-boutique-designer-boutique-shoes-sandals/br/v=1/2534374302161962.htm",
        "http://www.shopbop.com/sale-boutique-designer-boutique-shoes-sport/br/v=1/2534374302199420.htm",
        "http://www.shopbop.com/sale-boutique-designer-accessories/br/v=1/2534374302161956.htm",
        "http://www.shopbop.com/sale-boutique-designer-boutique-accessories-jewelry/br/v=1/2534374302161982.htm",
        "http://www.shopbop.com/sale-boutique-designer-boutique-accessories-belts/br/v=1/2534374302161990.htm",
        "http://www.shopbop.com/sale-boutique-designer-boutique-accessories-sunglasses/br/v=1/2534374302161978.htm",
        "http://www.shopbop.com/sale-boutique-designer-boutique-accessories-keychains/br/v=1/2534374302161989.htm",

        "http://www.shopbop.com/sale-20-percent-off/br/v=1/2534374302180310.htm",
        "http://www.shopbop.com/sale-30-percent-off/br/v=1/2534374302029885.htm",
        "http://www.shopbop.com/sale-40-percent-off/br/v=1/2534374302207490.htm",
        "http://www.shopbop.com/sale-50-percent-off/br/v=1/2534374302029886.htm",
        "http://www.shopbop.com/sale-60-percent-off/br/v=1/2534374302207491.htm",
        "http://www.shopbop.com/sale-70-percent-off/br/v=1/2534374302029887.htm",


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