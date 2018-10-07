class Source:
      '''
      Source class to define Source Objects
      '''

      def __init__(self,id,name,description):
        self.id = id
        self.name = name
        self.description = description

class Articles:
    '''
    articles class to define the article Objects
    '''
    def __init__(self,source,author,title,description,url,urlToImage,publishedAt):
        # self.id=id
        self.source=source
        self.author=author
        self.title=title
        self.description=description
        self.url=url
        self.urlToImage=urlToImage
        self.publishedAt=publishedAt