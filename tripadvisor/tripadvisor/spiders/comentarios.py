# -*- coding: utf-8 -*-
import scrapy
from ..items import TripadvisorItem

class ComentariosSpider(scrapy.Spider):
    name = 'comentarios'
    allowed_domains = ['tripadvisor.com']
    start_urls = ['https://www.tripadvisor.com/Attraction_Review-g7377590-d315753-Reviews-Intinan_Museum-San_Antonio_de_Pichincha_Quito_Pichincha_Province.html']

    def parse(self, response):
        item = TripadvisorItem()
        quadros_de_comentarios = response.xpath("//div[@class='Dq9MAugU T870kzTX LnVzGwUB']") 
        for quadro in quadros_de_comentarios:
            item["autor_comentario"] = quadro.xpath(".//div[@class='_2fxQ4TOx']/span/a/text()").get()
            item["autor_endereco"] = quadro.xpath(".//span[@class='_1TuWwpYf']/span/text()").get()
            item["comentario_titulo"] = quadro.xpath(".//div[@class='glasR4aX']/a/span/span/text()").get()
            item["comentario_corpo"] = quadro.xpath(".//div[@class='cPQsENeY']/q/span/text()").get()
            item["comentario_data"] = quadro.xpath(".//span[@class='_34Xs-BQm']/text()").get()
            yield item
            
        page_next = response.xpath("//a[@class='ui_button nav next primary ' and text()='Next']/@href").get()
        if page_next:
            yield response.follow(url=page_next, callback=self.parse)



