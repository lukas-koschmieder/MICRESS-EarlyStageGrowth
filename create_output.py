import yaml
from micpy import tab


def main():
    # Read input data from SimStack WaNo file
    with open("rendered_wano.yml", mode="r", encoding="utf-8") as file:
        input_data = yaml.full_load(file)

    # Read output data from MICRESS phase fraction file
    output_data = tab.read("output.TabF").to_dict(orient="split")

    # Generate SimStack output file
    with open("output_dict.yml", mode="w", encoding="utf-8") as out:
        yaml.dump({"input": input_data, "output": output_data}, out)


if __name__ == "__main__":
    main()
