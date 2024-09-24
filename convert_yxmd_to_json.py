import xml.etree.ElementTree as ET
import json
import os

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

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description='Convert Alteryx .yxmd file to .json')
    parser.add_argument('input_file', type=str, help='Path to the input .yxmd file')
    parser.add_argument('output_file', type=str, help='Path to the output .json file')

    args = parser.parse_args()

    convert_yxmd_to_json(args.input_file, args.output_file)