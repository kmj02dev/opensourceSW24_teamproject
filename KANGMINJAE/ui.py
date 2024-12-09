import tkinter as tk
from tkinter import ttk, scrolledtext
import threading
import time
import main

class SentimentAnalysisGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("뉴스 기사 감정 분석")
        self.root.geometry("800x700")  # 창 크기를 더 크게 조정
        
        self.style = ttk.Style()
        self.style.configure('Step.TFrame', padding=10)
        self.style.configure('Status.TLabel', padding=5)
        
        self.setup_ui()
        
    def setup_ui(self):
        # 메인 컨테이너
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # URL 입력 섹션
        url_frame = ttk.Frame(main_frame)
        url_frame.pack(fill=tk.X, pady=(0, 20))
        
        ttk.Label(url_frame, text="뉴스 URL:").pack(side=tk.LEFT)
        self.url_entry = ttk.Entry(url_frame)
        self.url_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)
        self.url_entry.insert(0, "")
        
        self.analyze_btn = ttk.Button(url_frame, text="분석 시작", command=self.start_analysis)
        self.analyze_btn.pack(side=tk.LEFT)
        
        # 진행 상태 표시 섹션
        self.steps_frame = ttk.Frame(main_frame)
        self.steps_frame.pack(fill=tk.X, pady=10)
        
        self.status_labels = []
        steps = [
            "1. URL 검증",
            "2. HTML 파싱",
            "3. 본문 추출",
            "4. 감정 분석"
        ]
        
        for step in steps:
            step_frame = ttk.Frame(self.steps_frame, style='Step.TFrame')
            step_frame.pack(fill=tk.X, pady=2)
            
            status_label = ttk.Label(step_frame, text="○ " + step, style='Status.TLabel')
            status_label.pack(side=tk.LEFT)
            self.status_labels.append(status_label)
        
        # 결과 표시를 위한 노트북 (탭) 생성
        notebook = ttk.Notebook(main_frame)
        notebook.pack(fill=tk.BOTH, expand=True, pady=10)
        
        # 분석 결과 탭
        result_frame = ttk.Frame(notebook)
        notebook.add(result_frame, text="감정 분석 결과")
        
        self.result_text = scrolledtext.ScrolledText(result_frame, height=15, wrap=tk.WORD)
        self.result_text.pack(fill=tk.BOTH, expand=True)

        # 본문 표시 탭
        content_frame = ttk.Frame(notebook)
        notebook.add(content_frame, text="추출된 본문")
        
        self.content_text = scrolledtext.ScrolledText(content_frame, height=15, wrap=tk.WORD)
        self.content_text.pack(fill=tk.BOTH, expand=True)
    
    def update_status(self, step: int, status: str):
        symbols = {"waiting": "○", "processing": "◎", "complete": "●", "error": "×"}
        self.status_labels[step].configure(text=f"{symbols[status]} {self.status_labels[step].cget('text')[2:]}")
    
    def log_result(self, message: str):
        self.result_text.insert(tk.END, message + "\n")
        self.result_text.see(tk.END)
    
    def display_content(self, content: str):
        """추출된 본문을 표시하는 새로운 메서드"""
        self.content_text.delete(1.0, tk.END)
        self.content_text.insert(tk.END, content)
        self.content_text.see(tk.END)
    
    def simulate_analysis(self):
        try:
            # URL 검증
            self.update_status(0, "processing")
            url = self.url_entry.get()
            if not url.startswith("https://"):
                raise ValueError("유효하지 않은 URL입니다.")
            time.sleep(0.5)
            self.update_status(0, "complete")
            self.log_result("URL 검증 완료")
            
            # HTML 파싱
            self.update_status(1, "processing")
            html_content = main.get_html(url)
            if html_content is None:
                raise ValueError("HTML 파싱 실패")
            self.update_status(1, "complete")
            self.log_result("HTML 파싱 완료")
            
            # 본문 추출
            self.update_status(2, "processing")
            main_content = main.extract_content(html_content)
            if main_content is None:
                raise ValueError("본문 추출 실패")
            self.update_status(2, "complete")
            self.log_result("본문 추출 완료")
            
            # 추출된 본문 표시
            self.display_content(main_content)
            
            # 감정 분석
            self.update_status(3, "processing")
            sentiment_pipeline = main.analyze_sentiment(main_content)
            result = sentiment_pipeline
            self.update_status(3, "complete")
            
            # 최종 결과 표시
            sentiment = "긍정적" if result[0]['label'] == 'POSITIVE' else "부정적"
            confidence = result[0]['score'] * 100
            self.log_result(f"\n최종 분석 결과:")
            self.log_result(f"감정: {sentiment}")
            self.log_result(f"신뢰도: {confidence:.1f}%")
            
        except Exception as e:
            self.log_result(f"\n오류 발생: {str(e)}")
            for i in range(4):
                if self.status_labels[i].cget('text').startswith("◎"):
                    self.update_status(i, "error")
        
        finally:
            self.analyze_btn.configure(state='normal')
    
    def start_analysis(self):
        self.analyze_btn.configure(state='disabled')
        self.result_text.delete(1.0, tk.END)
        self.content_text.delete(1.0, tk.END)
        for i in range(4):
            self.update_status(i, "waiting")
        
        thread = threading.Thread(target=self.simulate_analysis)
        thread.daemon = True
        thread.start()
    
    def run(self):
        self.root.mainloop()

app = SentimentAnalysisGUI()
app.run()