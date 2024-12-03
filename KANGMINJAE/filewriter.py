def write_string_to_file(content: str, filename: str, encoding: str = 'utf-8') -> bool:
    """
    문자열을 파일로 저장하는 함수
    
    Args:
        content (str): 파일에 저장할 문자열
        filename (str): 저장할 파일 이름
        encoding (str, optional): 파일 인코딩. 기본값은 'utf-8'
    
    Returns:
        bool: 파일 저장 성공 여부
    """
    try:
        with open(filename, 'w', encoding=encoding) as file:
            file.write(content)
        return True
    except Exception as e:
        print(f"파일 저장 중 오류 발생: {str(e)}")
        return False