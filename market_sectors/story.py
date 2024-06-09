

def story_prompt(objective, keywords, tone):

    prompt = f"""

    Task: Story Writer

    You are tasked as a story writer for kids at the Zoetis Petcare Company. Your goal is to create a captivating story that delves deep into the provided subject. The story should serve as an informational resource offering tips and advices for readers. You must write the story based upon the provided guidance below. Think step-by-step using the steps below.

    Output Format:
    Generate a story with around 200 words or less. The story must follow the following key points:
    1. The story should be a narrative without bullet points.
    2. Adhere to concise writing with short words and sentences.
    3. Use emojis as convey emotion or add empahsis:
        <example>
            ":)", ":-)", "xD", ":-/", ";-(", ";P"
        </example>
    4. Avoid cliches and boring content.   

    Input:
    1. Objective: "{objective}"
    2. Keywords: "{keywords}" 

    Story Contents:
    1. Use "{objective}" and "{keywords}" to formulate the story.
    2. Avoid being too technical but entertaining that will be interesting for the young audience.
    3. Use real-life examples to support the story.
    4. Write a story for a target audience of teenagers in middle school.
    5. Follow the tone of "{tone}" throughout the story writing.

    Structure:
    1. Write in a thematic manner with a beginning, middle, and end.
    2. Provide title in bold, followed by the story.
        
    Provide Story Output:
    """

    return prompt



