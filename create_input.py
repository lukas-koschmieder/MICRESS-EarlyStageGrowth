import yaml
import jinja2 as j2


def generate_input_file(input_data, template_path, output_path):
    """Generates a MICRESS input file by rendering a Jinja2 template."""
    with open(template_path, mode="r", encoding="utf-8") as file:
        template = j2.Template(file.read())

    rendered_template = template.render(data=input_data)

    with open(output_path, mode="w", encoding="utf-8") as file:
        file.write(rendered_template)


def main():
    # Read input data from SimStack WaNo file
    with open("rendered_wano.yml", mode="r", encoding="utf-8") as file:
        input_data = yaml.full_load(file)

    # Generate MICRESS input file
    generate_input_file(input_data, "input.dri.j2", "input.dri")


if __name__ == "__main__":
    main()
