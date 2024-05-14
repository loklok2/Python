#8-1
def display_message():
    print("hello")

display_message()

#8-2
def favorite_book(booktitle):
    print(f"내가 가장좋아하는 책은, {booktitle.title()}")

favorite_book('이상한 나라의 엘리스')

#8-3
def make_shirt(size, msg):
    print(f"\n 사이즈:{size}, 인쇄메세지:{msg}")
make_shirt('xl','fuck')

#8-4
def make_shirt(msg, size = 'm, l'):
    print(f"\n 사이즈:{size}, 인쇄메세지:{msg}")
make_shirt(msg= 'random')

#8-5
def describe_city(city = '레이캬비크'):
    print(f"{city}는,아이슬란드에 있습니다")
describe_city()
describe_city(city='부산')
describe_city(city='서울')

#8-6
def city_country(city, country):
    print(f"{city.title()},{country.title()}")
city_country('santiago','chile')
city_country('busan', 'korea')
city_country('ulsan','korea')