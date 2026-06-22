from modules import csvReader
from modules.csvReader import CSVReader

def main():
    print("="* 50 )
    print("CoockieSEO" )
    print("Programatic SEO Automation Toolkit" )
    print("="* 50 )

    reader = CSVReader("C:\Avinash\Programming\Coockie SEO\input/products.csv")
    df = reader.load()
    if df is not None:
        print(f"Loaded {df.len} Products Successfully!\n")
        print(df.head())

if __name__ == "__main__":
    main()


