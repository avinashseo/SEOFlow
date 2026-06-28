
class ReportGenerator: 
    def generate(self, results):

        with open(
            "reports/validation_report.txt", 
            "w", 
            encoding ="utf-8") as file:

            file.write("SEOFlow Workflow\n")
            file.write("="*50)
            file.write("\n")

            for result in results:

                file.write(
                    f"[{result.severity}]"
                    f"[{result.product}]" 
                    f"[{result.message}]\n"
                )



        print("COmplete SEOFLOW Report")
        print("-"*50)

        if not results: 
            print("No Record found. ")
            print("-"*50)

        errors = sum(
            1 for r in results
            if r.severity == "ERROR"
        )
            
        warnings = sum(
            1 for r in results
            if r.severity == "WARNING"
        )

        recommendations = sum(
            1 
            for r in results
            if r.severity == "RECOMMENDATION"
        )

        print(f"Errors Found: {errors}")
        print(f"Warnings Found: {warnings}")
        print(f"Recommendations : {recommendations}")

        print("Detailed Report")
        print("+"*50)

        for result in results: 
            print(
                f"[{result.severity}]", 
                f"[{result.product}]"
                f"[{result.message}]"
            )