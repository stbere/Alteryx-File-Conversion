import xml.etree.ElementTree as ET
import json
import os
import glob
import zipfile

def convert_yxmd_to_json(yxmd_file, output_file):
    try:
        tree = ET.parse(yxmd_file)
        root = tree.getroot()

        def parse_element(element):
            parsed_element = {}
            if element.attrib:
                parsed_element.update(element.attrib)
            if element.text and element.text.strip():
                parsed_element['text'] = element.text.strip()
            for child in element:
                child_parsed = parse_element(child)
                if child.tag not in parsed_element:
                    parsed_element[child.tag] = child_parsed
                else:
                    if not isinstance(parsed_element[child.tag], list):
                        parsed_element[child.tag] = [parsed_element[child.tag]]
                    parsed_element[child.tag].append(child_parsed)
            return parsed_element

        workflow_dict = parse_element(root)

        with open(output_file, 'w') as json_file:
            json.dump(workflow_dict, json_file, indent=4)
        
        print(f"Successfully converted {yxmd_file} to {output_file}")
    except Exception as e:
        print(f"Error converting file {yxmd_file}: {e}")

def convert_yxmc_to_json(yxmc_file, output_file):
    # Same logic as convert_yxmd_to_json since .yxmc is also an XML file
    convert_yxmd_to_json(yxmc_file, output_file)

def convert_yxzp_to_json(yxzp_file, output_directory):
    try:
        with zipfile.ZipFile(yxzp_file, 'r') as zip_ref:
            zip_ref.extractall(output_directory)

        for file in os.listdir(output_directory):
            if file.endswith('.yxmd') or file.endswith('.yxmc'):
                input_file = os.path.join(output_directory, file)
                output_file = os.path.join(output_directory, file.replace('.yxmd', '.json').replace('.yxmc', '.json'))
                convert_yxmd_to_json(input_file, output_file)
        
        print(f"Successfully converted {yxzp_file} to JSON files in {output_directory}")
    except Exception as e:
        print(f"Error converting file {yxzp_file}: {e}")

def batch_convert_alteryx_files_to_json(input_directory, output_directory):
    os.makedirs(output_directory, exist_ok=True)
    for file in glob.glob(os.path.join(input_directory, '*')):
        if file.endswith('.yxmd'):
            output_file = os.path.join(output_directory, os.path.basename(file).replace('.yxmd', '.json'))
            convert_yxmd_to_json(file, output_file)
        elif file.endswith('.yxmc'):
            output_file = os.path.join(output_directory, os.path.basename(file).replace('.yxmc', '.json'))
            convert_yxmc_to_json(file, output_file)
        elif file.endswith('.yxzp'):
            convert_yxzp_to_json(file, output_directory)

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description='Batch convert Alteryx files (.yxmd, .yxmc, .yxzp) to .json')
    parser.add_argument('input_directory', type=str, help='Path to the input directory containing Alteryx files')
    parser.add_argument('output_directory', type=str, help='Path to the output directory for .json files')

    args = parser.parse_args()

    batch_convert_alteryx_files_to_json(args.input_directory, args.output_directory)