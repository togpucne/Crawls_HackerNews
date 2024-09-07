import scrapy

class HackernewsSpider(scrapy.Spider):
    name = 'hackernews'
    allowed_domains = ['news.ycombinator.com']
    
    def start_requests(self):
        # Vòng lặp tạo URL cho các trang từ 1 đến 155
        for i in range(1, 180):  # Số trang từ 1 đến 155
            url = f'https://news.ycombinator.com/item?id=41342017&p={i}'
            yield scrapy.Request(url=url, callback=self.parse)
    
    def parse(self, response):
        # Lấy dữ liệu bình luận
        comments = response.xpath('//tr[@class="athing comtr"]')
        
        for comment in comments:
            yield {
                'user': comment.xpath('.//a[@class="hnuser"]/text()').get(),
                'comment': comment.xpath('.//div[@class="commtext c00"]/text()').get(),
                'comment_link': comment.xpath('.//a[contains(@href, "reply?id")]/@href').get(),
                'comment_id': comment.xpath('.//@id').get(),
                'time': comment.xpath('.//span[@class="age"]/a/text()').get(),
                'parent_id': comment.xpath('.//a[@class="clicky"]/@href').re_first(r'#(\d+)')
            }
        
        # Nếu cần xử lý tiếp các trang khác có thể thêm logic ở đây
