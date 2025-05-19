import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.credentials import AzureKeyCredential
from azure.ai.inference.models import SystemMessage, UserMessage

def generate_text(prompt):
    try:
        # Initialize the client with GitHub Models endpoint
        client = ChatCompletionsClient(
            endpoint="https://models.inference.ai.azure.com",
            credential=AzureKeyCredential(os.environ["GH_TOKEN"])
        )

        # Define the conversation
        messages = [
            SystemMessage(content="You are a helpful AI assistant."),
            UserMessage(content=prompt)
        ]

        # Call the model
        response = client.complete(
            model="Phi-3-mini-4k-instruct",
            messages=messages,
            max_tokens=500,
            temperature=0.7
        )

        # Return the generated text
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    user_prompt = "Write a short poem about the night sky."
    result = generate_text(user_prompt)
    print("Generated Text:")
    print(result)