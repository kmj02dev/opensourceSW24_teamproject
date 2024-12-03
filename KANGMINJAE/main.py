from transformers import pipeline
import fetcher
import filemanager
import llm

def get_html(url:str):
    # HTML 가져오기
    html_content = fetcher.fetch_html(url)
    assert html_content != None, 'Get HTML Fail'
    return html_content

def extract_content(html_content:str):
    # LLM을 이용해 본문 추출하기
    # main_content = filemanager.read_file("./KANGMINJAE/sample3.txt") # 비용 절감을 위해 테스트 시 테스트 파일 이용
    main_content = llm.get_answer(html_content)
    assert main_content != None, 'bad answer'
    # filemanager.write_string_to_file(main_content, "./KANGMINJAE/sample3.txt") # 분석을 위한 임시적 파일 작성
    print(main_content)
    return main_content

def analyze_sentiment(main_content:str):
    # 추출한 내용을 이용해 긍정, 부정 분석하기
    sentiment_pipeline = pipeline(model="distilbert-base-uncased-finetuned-sst-2-english")
    sentiment = sentiment_pipeline(main_content)
    print(sentiment)
    return sentiment

# analyze_sentiment("https://n.news.naver.com/mnews/article/057/0001857665")