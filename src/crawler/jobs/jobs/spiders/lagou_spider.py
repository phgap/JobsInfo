import scrapy
from jobs.items import LagouItem

class LagouSpider(scrapy.Spider):
    name = "lagou"
    start_urls = [
        'https://www.lagou.com/zhaopin/Java/',
        'https://www.lagou.com/zhaopin/Python/',
        'https://www.lagou.com/zhaopin/PHP/',
        'https://www.lagou.com/zhaopin/.NET/',
        'https://www.lagou.com/zhaopin/C%23/',
        'https://www.lagou.com/zhaopin/C%2B%2B/',
        'https://www.lagou.com/zhaopin/C/',
        'https://www.lagou.com/zhaopin/VB/',
        'https://www.lagou.com/zhaopin/Delphi/',
        'https://www.lagou.com/zhaopin/Perl/',
        'https://www.lagou.com/zhaopin/Ruby/',
        'https://www.lagou.com/zhaopin/Hadoop/',
        'https://www.lagou.com/zhaopin/Node.js/',
        'https://www.lagou.com/zhaopin/shujuwajue/',
        'https://www.lagou.com/zhaopin/ziranyuyanchuli/',
        'https://www.lagou.com/zhaopin/sousuosuanfa/',
        'https://www.lagou.com/zhaopin/jingzhuntuijian/',
        'https://www.lagou.com/zhaopin/quanzhangongchengshi/',
        'https://www.lagou.com/zhaopin/go/',
        'https://www.lagou.com/zhaopin/asp/',
        'https://www.lagou.com/zhaopin/shell/',
        'https://www.lagou.com/zhaopin/houduankaifaqita/http'
    ]

    def parse(self, response):
        # extract job info
        jobs = self.get_jobs(response)
        for job in jobs:
            item = LagouItem()
            item["_id"] = self.get_id(job)
            item["title"] = self.get_title(job)
            item["city"] = self.get_city(job)
            item["salary"] = self.get_salary(job)
            item["tags"] = self.get_tags(job)
            item["site"] = "www.lagou.com"
            yield item


        # follow links
        next_page = response.css('div.pager_container a:last-child::attr(href)').extract_first()
        if next_page is not None and next_page != "javascript:;":
            next_page = response.urljoin(next_page)
            print '=====================next page is %s' % next_page
            yield scrapy.Request(next_page, callback=self.parse)


    def get_jobs(self, resp):
        return resp.css('.s_position_list .item_con_list li')

    def get_id(self, job):
        return job.css('.position_link::attr(href)').extract_first()

    def get_title(self, job):
        return job.css('.position_link h2::text').extract_first()


    def get_city(self, job):
        return job.css('.position_link span.add em::text').extract_first()

    def get_salary(self, job):
        return job.css('.p_bot span.money::text').extract_first()

    def get_company(self, job):
        return job.css('.company_name a::text').extract_first()

    def get_tags(self, job):
        return job.css('.list_item_bot .li_b_l span::text').extract()

    def get_education(self, job):
        pass

    def get_experience(self, job):
        pass
