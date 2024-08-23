import scrapy


class BooksSpider(scrapy.Spider):
    name = "book_spider"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ['https://books.toscrape.com/catalogue/category/books_1/']

    def parse(self, response):
        book_elements = response.css('article.product_pod')

        # for book_element in book_elements:

        #     title = book_element.css('h3 a::attr(title)').getall()
        #     price = book_element.css('div p.price_color::text').getall()

            # yield {
            #     'title': title,
            #     'price': price
            # }
