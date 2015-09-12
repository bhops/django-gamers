import scrapy
from gamesscraper.items import GamesscraperItem
from games.models import Platform

class GameRankingsGameSpider(scrapy.Spider):
    name = 'gamerankingsgame'
    start_urls = [
        'http://www.gamerankings.com/browse.html',
    ]

    def get_or_create_platform(self, platform_name, platform_slug):
        try:
            platform = Platform.objects.get(name=platform_name)
        except Platform.DoesNotExist:
            platform = Platform.objects.create(name=platform_name)
        return platform

    def parse(self, response):
        for idx, platform in enumerate(response.xpath('//*/div[@class="box_body"]/*/select[@name="site"]/option')):
            if idx > 0: # avoid "All Platforms" option
                slug = platform.xpath('@value').extract()[0]
                name = platform.xpath('text()').extract()[0]
                request = scrapy.Request("http://www.gamerankings.com/browse.html?site={0}&numrev=3".format(str(slug)),
                                         callback=self.parse_platform)

                request.meta['platform'] = self.get_or_create_platform(name, slug)
                request.meta['gr-platform'] = slug
                request.meta['gr-page'] = 1
                yield request


    def parse_platform(self, response):
        for game in response.xpath("//*/tr"):
            title = game.xpath('td/a/text()').extract()[0]

            gameItem = GamesscraperItem()
            gameItem['title'] = title
            gameItem['platform'] = response.meta['platform']

            yield gameItem

        pages = response.xpath('//*/div[@class="pod"]/div/a/text()').extract()
        if "Next Page" in pages:
            request = scrapy.Request("http://www.gamerankings.com/browse.html?site={0}&numrev=3&page={1}"
                                    .format(str(response.meta['gr-platform']), response.meta['gr-page'] + 1),
                                    callback=self.parse_platform)
            request.meta['gr-platform'] = response.meta['gr-platform']
            request.meta['gr-page'] = response.meta['gr-page'] + 1
            request.meta['platform'] = response.meta['platform']
            yield request
