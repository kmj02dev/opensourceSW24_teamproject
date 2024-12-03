import anthropic
import config

client = anthropic.Anthropic(
    # defaults to os.environ.get("ANTHROPIC_API_KEY")
    api_key=config.anthropic_api_key,
)

def get_answer(text:str, model="claude-3-5-sonnet-20241022"):
    message = client.messages.create(
        model=model, # "claude-3-5-haiku-20241022" or "claude-3-5-sonnet-20241022",
        max_tokens=20000,
        temperature=0,
        system="You are an expert at extracting and analyzing the main content from HTML documents. Please extract the main body text while removing any navigation, headers, footers, advertisements, and other non-content elements.",
        messages=[
            {"role": "user", 
            "content": text}
        ]
    )
    return message.content