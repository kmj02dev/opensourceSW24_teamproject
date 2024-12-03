def write_string_to_file(content: str, filename: str, encoding: str = 'utf-8') -> bool:
    try:
        with open(filename, 'w', encoding=encoding) as file:
            file.write(content)
        return True
    except Exception as e:
        print(f"파일 저장 중 오류 발생: {str(e)}")
        return False
    
def read_file(file_path: str, encoding: str = 'utf-8'):
        try:
            with open(file_path, 'r', encoding=encoding) as file:
                return file.read()
        except FileNotFoundError:
            print(f"파일을 찾을 수 없습니다: {file_path}")
            return None
        except Exception as e:
            print(f"파일 읽기 오류 발생: {str(e)}")
            return None