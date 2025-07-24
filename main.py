from ollama import Client
from datetime import datetime
import re 

client = Client(host='http://localhost:11434')

test_content = """Sarah kicked off the meeting by thanking everyone for coming and gave a quick recap of our Q2 goals and how we performed — she mentioned we hit most of our targets, but the mobile app prototype is slightly behind, though catching up fast. James jumped in after and said the backend integration is actually ahead of schedule, which could help us recover some time. He’s planning to push to the staging environment by next Friday. Priya then shared her screen and walked us through the latest UI mockups for the new onboarding flow. Feedback was generally positive — Sarah said she liked the visual clarity, and James noted that the button placement should make implementation easier.

Tom raised the question about whether we’re still aiming for early access in August. Sarah confirmed that yes, the current plan is to have a working internal version ready by August 10, with public early access signups starting August 5. Tom is drafting the email campaign now and should have the first version ready by August 1. He asked if there would be a landing page available for the signups, and James said the dev team can prioritize it right after the staging deployment.

Alex gave a quick update on the analytics from the beta version. He’s been tracking session length and retention rate and mentioned that both are below target. He said he’ll finalize the report and share it by July 29. Priya asked if we can get more detail on where drop-offs are happening during onboarding — Alex said he’ll include that in the report.

There was a brief discussion about adding dark mode. Priya said it’s feasible from a design perspective, and James added that it’s not too difficult to implement, but they both agreed to make it a stretch goal rather than a core requirement for Q3.

Sarah wrapped up the meeting by summarizing the action items: Priya to finish the prototype by August 10, James to handle staging deployment by July 31, Tom to send his email campaign draft by August 1, and Alex to deliver the beta report by July 29. The next meeting was scheduled for July 30 at 10 AM."""

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
    'content': 'You are a professional summarizer, you will be given texts and meetings notes to summarize using the following format: 1. Subject- what the notes/text is about, around 1 sentence, 2. Main topics- What the text is actually about, more in depth and including explanations, 3. Key points- include stuff that should be remembered, 4. Anything else to add- such as important dates or events, 5. A paragraph length conclusion which explains the text/meeting.',
},
{
    'role': 'user',
    'content': test_content,
}
])

write_log(summary.message.content)

cleaned_summary = clean_output(summary.message.content)
print(cleaned_summary)