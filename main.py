import os
import sys
from PIL import Image
from pdf2image import convert_from_path
import pytesseract

input_dir = os.path.join('.', "data", "in")
output_dir = os.path.join('.', "data", "out")
language = None


def convertPdfToImages(file_path: str, file_name: str, output_file_dir: str):
    print("\tGenerating temporary images...")
    images = convert_from_path(file_path)
    page_prefix = file_name

    for i in range(len(images)):
        image_file_name = page_prefix + "_" + str(i) + '.jpg'
        print(f"\t\tGenerating temporary images {image_file_name}...")
        images[i].save(os.path.join(output_file_dir, image_file_name), 'JPEG')


def get_text(output_file_dir: str, file_name: str):
    images = os.listdir(output_file_dir)
    if not images:
        print("\t\tNo images found")
        exit
    ocr_file = os.path.join(output_file_dir, f"{file_name}.txt")
    with open(ocr_file, 'w') as f:
        f.write('')

    for image in images:
        if (image.endswith("jpg")):
            print(f"\t\t OCR processing on {image}...")
            image_text = pytesseract.image_to_string(
                Image.open(os.path.join(output_file_dir, image)), lang=language)
            with open(ocr_file, 'a') as f:
                f.write(image_text)


if __name__ == "__main__":
    print("\n********************************")
    print("* Welcome to PDF to TEXT Utility*")
    print("*********************************\n")

    if not os.path.isdir(input_dir):
        print(f"Directory {input_dir} does not exist!")
        sys.exit(os.EX_CONFIG)

    if not os.path.isdir(output_dir):
        print(f"Directory {output_dir} does not exist!")
        sys.exit(os.EX_CONFIG)

    print("Seeking pdf in input folder...\n")
    files = os.listdir(input_dir)

    if not files:
        print("No files on input folder\n")

    for file in files:
        if (file.endswith("pdf")):
            print(f"\nElaborating {file}...")
            file_name = file.split(".pdf")[0]
            file_temp_dir = os.path.join(output_dir, file_name)

            if not os.path.isdir(file_temp_dir):
                print(f"\tMaking temporarty directory {file_temp_dir}...")
                os.mkdir(file_temp_dir)

            convertPdfToImages(os.path.join(input_dir, file),
                               file_name, file_temp_dir)

            print(f"\tStarting OCR on pdf pages...")
            get_text(file_temp_dir, file_name)

    sys.exit(os.EX_OK)
