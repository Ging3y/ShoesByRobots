class Shoe_DAO(object):

    def __init__(self, path):
        self.path = path

    def getInfo(self):

        import requests
        from bs4 import BeautifulSoup as bs

        page = requests.get(self.path)
        soup = bs(page.content, 'html.parser')

        # Get shoe name
        try:
            name_= str(soup.find('h1').contents[0])
        except:
            name_ = "No name found"

        # Get shoe type
        try:
            type_ = str(soup.find('h2').contents[0])
        except:
            type_ = "No type found"

        # Get shoe price
        try:
            price_ = float(soup.find_all(class_="text-color-black")[1].contents[0].replace('$', ''))
        except:
            price_ = "No price found"

        # Get shoe description
        try:
            description_ = str(soup.find_all(class_="description-preview")[0].contents[0])
            soup_descrip = bs(description_, "html.parser")
            description_ = str(soup_descrip.find('p').contents[0])
        except:
            description_ = "No description found"

        # Get star rating
        try:
            stars_ = str(soup.find_all(class_="d-sm-ib pl4-sm")[0].contents[0])
        except:
            stars_ = "No rating found"


        # Get Reviews
        try:
            reviews_ = []
            review_container = list(soup.find_all(class_="review mb10-sm"))

            for review in review_container:
                soup_review = bs(str(review), "html.parser")
                review_ = str(soup_review.find_all('p')[-1].contents[0])
                reviews_.append(review_)
        except:
            reviews_ = "No reviews found"

        # Get image source
        try:
            image_source = str(soup.find_all(class_ = "slider"))
            soup_image = bs(image_source, "html.parser")
            image_ = str(soup_image.find_all('picture')[1])
            pos = image_.find('srcset=') + 8
            image_ = image_[pos:]
            pos = image_.find('/>') - 1
            image_ = image_[:pos]


        except:
            image_ = "No source found"

        print(image_)

        self.name = name_
        self.type = type_
        self.image = image_
        self.price = price_
        self.description = description_
        self.stars = stars_
        self.reviews = reviews_

        self.data = {'name': self.name,
                     'image': self.image,
                     'type': self.type,
                     'price': self.price,
                     'description': self.description,
                     'rating': self.stars,
                     'reviews': self.reviews}

        return self.data

    def printInfo(self):
        print("Shoe name: " + self.name)
        print("Shoe type: " + self.type)
        print("Price: $" + str(self.price))
        print("Shoe Description: " + self.description)
        print("Star Rating: " + self.stars)
        print("Reviews: " + str(self.reviews))

""" TRIAL RUN """

"""
shoe_links = ["https://www.nike.com/t/air-vapormax-flyknit-2-mens-running-shoe-zcHs9Q/AR5406-600"]

for link in shoe_links:

    shoe = Shoe_DAO(link)
    shoe_info = shoe.getInfo()
    #shoe.printInfo()
    #print("\n")
"""