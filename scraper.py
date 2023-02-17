import scrapy
class thespider(scrapy.Spider):
	name="dog"
	allowed_domains=['en.wikipedia.org']
	start_urls=['https://en.wikipedia.org/wiki/dog']

	def parse(self,response):
		title=response.xpath("//h1/test()").get()
		content=response.xpath("//div[@class='mw-parser-output']//p//text()").getall()
		yield
		{
		'title':title,
		'content':" ".join(content)
		}