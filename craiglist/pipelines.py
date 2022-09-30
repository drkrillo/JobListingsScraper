
from itemadapter import ItemAdapter


class CraiglistPipeline:
    def text_cleaner(self, item, spider):

        item['description'] = [
                            substring for substring in item['description']
                            if substring != '\n'
                              ]
        item['description'] = item['description'].replace('\n\n','')

        return item
