from transformers import pipeline
import fetcher
import filemanager
import llm

# 테스트할 URL 입력받기
url = "https://n.news.naver.com/mnews/article/057/0001857665"# input("Enter URL: ")

# HTML 가져오기
html_content = fetcher.fetch_html(url)
assert html_content != None, 'Get HTML Fail'

# LLM을 이용해 본문 추출하기
main_content = llm.get_answer(html_content)
# main_content = filemanager.read_file("./KANGMINJAE/sample.txt") # 비용 절감을 위해 테스트 시 테스트 파일 이용
assert main_content != None, 'bad answer'
# filemanager.write_string_to_file(main_content, "./KANGMINJAE/sample.txt") # 분석을 위한 임시적 파일 작성

# 추출한 내용을 이용해 긍정, 부정 분석하기
sentiment_pipeline = pipeline("sentiment-analysis")
print(sentiment_pipeline(main_content))