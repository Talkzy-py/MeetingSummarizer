from ollama import Client
from datetime import datetime
import re 

client = Client(host='http://localhost:11434')

with open('systemprompt.txt', 'r') as prompt_file:
    system_prompt = prompt_file.read()

text_to_summarize = input("Enter the text/meeting notes to summarize: ")

def clean_output(text):
    return re.sub(r'<think>.*?</think>', '', text, flags=re.DOTALL).strip()

def write_log(message):
    with open('log.txt', 'a') as log_file:
        log_file.write(message + '\n')
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        log_file.write(f'Log entry at {timestamp}\n')
        
summary = client.chat(model='deepseek-r1', messages=[
{
    'role': 'system',
    'content': system_prompt,
    'content': 'You are a professional summarizer, you give detailed responses without stating the obvious you will be given texts and meetings notes to summarize using the following format: 1. Subject- what the notes/text is about, around 1 sentence, 2. Main topics- What the text is actually about, more in depth and including explanations, 3. Key points- include stuff that should be remembered, 4. Anything else to add- such as important dates or events, 5. A paragraph length conclusion which explains the text/meeting.',
},
{
    'role': 'user',
    'content': text_to_summarize,
}
])

write_log(summary.message.content)

cleaned_summary = clean_output(summary.message.content)
print(cleaned_summary)
