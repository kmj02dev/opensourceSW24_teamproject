import requests
from requests.exceptions import RequestException
import logging

# 로깅 설정
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# 일반적인 웹 브라우저처럼 보이는 User-Agent 설정
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

def fetch_html(url):
    """
    주어진 URL에서 HTML 콘텐츠를 가져옵니다.
    
    Args:
        url (str): 가져올 웹 페이지의 URL
        
    Returns:
        str: 성공시 HTML 콘텐츠, 실패시 None
    """
    try:
        # URL 유효성 검사
        if not url.startswith(('http://', 'https://')):
            raise ValueError('Invalid URL format. URL must start with http:// or https://')

        # GET 요청 보내기
        response = requests.get(url, headers=headers, timeout=10)
        
        # HTTP 상태 코드 확인
        response.raise_for_status()
        
        # 인코딩 확인
        response.encoding = response.apparent_encoding or 'utf-8'
        
        return response.text

    except RequestException as e:
        logger.error(f"네트워크 에러 발생: {str(e)}")
        return None
        
    except ValueError as e:
        logger.error(f"URL 형식 에러: {str(e)}")
        return None
        
    except Exception as e:
        logger.error(f"예상치 못한 에러 발생: {str(e)}")
        return None