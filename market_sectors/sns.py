

def sns_prompt(input, keywords):

    prompt = f"""

    Task: Story Writer

    You are tasked as a social media editor for the Zoetis Petcare Company. Your goal is to create an Instagram post condensing the input content while retaining its essence and engagement factor. 

    Output Format:
    The post must follow the following key points:
    1. Identify the main message or takeaway from the "{input}" and generate a single post containing only two sentences.
    2. Use emojis as needed to convey emotion or add empahsis:
        <example>
        ":)", ":-)", "xD", ":-/", ";-(", ";P"
        </example>
    3. Use keywords from the post as hashtags at the end of the post. 

    Input:
    1. Input: "{input}"
    2. Keywords: "{keywords}"    

    Story Contents:
    1. Use "{input}" as the base for the post.
    2. The first sentence of the generated caption will contain an introduction to the topic. 
    3. The second sentence should serve as a call to action to learn more about the topic, by directing the readers to a link in the Instagram bio. The redirection should not be in a separate sentence. 
    2. Avoid being too technical but entertaining that will be interesting for the young audience.
    3. Ask questions ro encourage the audience to share their thoughts or experiences related to the post.
    4. Write a post for a target audience of teenagers in middle school.
        
    Provide Output:
    """

    return prompt



