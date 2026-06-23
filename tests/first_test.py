reader = CSVReader("data/input/products.csv")

df = reader.read()

profile = ProfileLoader.load("mpg")

mapper = ProductMapper(profile)

products = mapper.map(df)

print(products[0].name)

print(products[0].meta_title)