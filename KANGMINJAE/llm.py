import anthropic
import config

client = anthropic.Anthropic(
    # defaults to os.environ.get("ANTHROPIC_API_KEY")
    api_key=config.anthropic_api_key,
)

models = {
    "Sonnet" : "claude-3-5-sonnet-20241022",
    "Haiku" : "Claude 3.5 Haiku"
}

def get_answer(text:str, model=models["Sonnet"]):
    try:
        message = client.messages.create(
            model=model,
            max_tokens=250,
            temperature=0,
            system="You are an expert at extracting and analyzing the main content from HTML documents. Please extract the main body text while removing any navigation, headers, footers, advertisements, and other non-content elements.",
            messages=[
                {"role": "user", 
                "content": text}
            ]
        )
        return message.content[0].text
    except anthropic.APIError as e:
        print("에러 코드:", e.status_code)
        print("에러 메시지:", e.message)
        return None
    