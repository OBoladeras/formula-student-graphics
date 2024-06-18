import pandas as pd


def xlsx_to_csv(input_file, output_file):
    try:
        df = pd.read_excel(input_file)

        df.to_csv(output_file, index=False, encoding='utf-8')

        print("Conversion successful!")
    except Exception as e:
        print("Error occurred during conversion:", str(e))


# Example usage
input_file = "input.xlsx"
output_file = "output.csv"
xlsx_to_csv(input_file, output_file)
