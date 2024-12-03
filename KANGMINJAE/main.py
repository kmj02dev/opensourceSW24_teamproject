from transformers import pipeline
import fetcher
import filewriter

# 테스트할 URL 입력받기
url = input("Enter URL: ")

# HTML 가져오기
html_content = fetcher.fetch_html(url)

if html_content:
    print("Get HTML Success.")
    filewriter.write_string_to_file(html_content, "/KANGMINJAE/sample.txt")
else:
    print("Get HTML Fail")