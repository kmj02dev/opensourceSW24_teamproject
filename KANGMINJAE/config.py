from dotenv import load_dotenv
import os

# .env 파일 로드
load_dotenv()

# 환경 변수 읽기
anthropic_api_key = os.getenv('ANTHROPIC_API_KEY')
openai_api_key = os.getenv('OPENAI_API_KEY')
