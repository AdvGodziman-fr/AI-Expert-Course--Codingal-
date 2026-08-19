import os
from markdown_pdf import MarkdownPdf, Section
from groq import Groq

client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "What are some good places to visit in the world?",
        }
    ],
    model="openai/gpt-oss-safeguard-20b",
)
output = chat_completion.choices[0].message.content


with open(r"MODULE_4\Lesson 21 Activity 1\answer.md", "w") as file:
    file.write(output)


pdf = MarkdownPdf(toc_level=2)

# Add content as separate sections (useful for managing page breaks)
pdf.add_section(Section(output, toc=True))
pdf.save("output.pdf")