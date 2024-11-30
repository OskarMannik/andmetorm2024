from code_generator import VisualizationGenerator
import pandas as pd


def main():
    viz_gen = VisualizationGenerator()

    csv_path = "../scrape-and-modify-data/output/t_awtabel002_02_curr.csv"
    data_description = "Vee andmestik"

    user_requirements = "vali üks rida mille 'aruandeaasta' on 2023 ja tekita iga kuu kohta tulp graafiku peale"

    df = pd.read_csv(csv_path)

    generated_code = viz_gen.generate_visualization_code(
        data_columns=df.columns.tolist(),
        sample_row=df.iloc[0].tolist(),
        csv_filename=csv_path,
        user_requirements=user_requirements,
        data_description=data_description
    )

    print(generated_code)


main()
