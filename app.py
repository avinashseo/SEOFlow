"""
SEOFlow Entry Point
"""
from src.utils.logger import setup_logger
from src.reports.report_generator import ReportGenerator
from multiprocessing.reduction import duplicate
from unittest import result
from src.config.profile_loader import ProfileLoader
from src.readers.csv_reader import CSVReader
from src.mappers.product_mapper import ProductMapper
from src.validators import duplicate_validator
from src.validators.required_validator import RequiredValidator
from src.validators.meta_validator import MetaValidator
from src.validators.duplicate_validator import DuplicateValidator
from src.validators.validation_engine  import ValidationEngine


def main():

    print("=" * 50)
    print("SEOFlow")
    print("Programmatic SEO Automation Toolkit")
    print("=" * 50)

    # Load profile
    profile = ProfileLoader.load("mpg")

    print("\n✅ Profile loaded successfully")

    # Read CSV
    reader = CSVReader("data/input/products.csv")

    dataframe = reader.read()   

    logger = setup_logger()

    logger.info("CSV Loaded Successfully")
    print(f"Rows found: {len(dataframe)}")

    # Map products
    mapper = ProductMapper(profile)

    products = mapper.map(dataframe)

    logger.info("Products mapped successfully")
    print(f"Products created: {len(products)}")

    # Run validation Engine
    engine = ValidationEngine(
        [
            RequiredValidator(),
            MetaValidator(), 
            DuplicateValidator(),         

        ]
    )

    results = engine.run(products)

    # -------------------------------------
    # Print Validation Report
    # -------------------------------------

    report = ReportGenerator()
    report.generate(results)
    
    print(
        "\n✅ Report exported successfully"
    )



    # print("\nVALIDATION REPORT")
    # print("=" * 50)

    # if not results:

    #     print("✅ No issues found.")

    # else:

    #     for result in results:

    #         print(
    #             f"[{result.severity}] "
    #             f"[{result.product}] "
    #             f"| {result.message}"
    #         )

    
if __name__ == "__main__":
    main()