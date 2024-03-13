import anthropic
my_api_key = "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"

import anthropic

client = anthropic.Anthropic(
    # defaults to os.environ.get("ANTHROPIC_API_KEY")
    api_key=my_api_key,
)
message = client.messages.create(
    model="claude-3-sonnet-20240229",
    max_tokens=2000,
    temperature=1,
    system="Your task is to create a comprehensive, engaging, and well-structured lesson plan on the given subject. The lesson plan should be designed for a 60-minute class session and should cater to a specific grade level or age group. Begin by stating the lesson objectives, which should be clear, measurable, and aligned with relevant educational standards. Next, provide a detailed outline of the lesson, breaking it down into an introduction, main activities, and a conclusion. For each section, describe the teaching methods, learning activities, and resources you will use to effectively convey the content and engage the students. Include differentiation strategies to accommodate diverse learning needs and styles. Finally, describe the assessment methods you will employ to evaluate students' understanding and mastery of the lesson objectives. The lesson plan should be well-organized, easy to follow, and promote active learning and critical thinking.",
    messages=[
        {"role": "user", "content": "Subject: Introduction to Photosynthesis\nGrade Level: 7th Grade (Ages 12-13)"}
    ]
)
print(message.content[0].text)

