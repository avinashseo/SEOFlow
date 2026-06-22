import pandas as pd 

class CSVReader:
    def __init__ (self, file_path):
        self.file_path = file_path

    def load(self):
        try:
            df = pd.read_csv(self.file_path)
            return df

        except Exception as e:
            print(f"Error: {e}")
            print("Error")
            return None

if __name__ == "__main__":
    reader = CSVReader("C:\Avinash\Programming\Coockie SEO\input\products.csv")
    data = reader.load()
    print(data.head())


        
