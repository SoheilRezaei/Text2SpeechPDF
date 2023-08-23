import PyPDF2

def extract_text_from_pdf(pdf_path):
    try:
        with open(pdf_path, "rb") as pdf_file:
            pdf_reader = PyPDF2.PdfReader(pdf_file)
            
            text = ""
            
            for page_num in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_num]
                text += page.extract_text()
            
            # Write into txt
            with open('extracted.txt', "w", encoding="utf-8") as txt_file:
                txt_file.write(text)
            
            print("Text extracted and saved")
            
    except Exception as e:
        print(e)

def main():
    pdf_path = 'data/med_enc.pdf'
    extract_text_from_pdf(pdf_path)

if __name__ == "__main__":
    main()
