from bot_ai_interface.azureai_interface import UseOpenAIPkg
from bot_ai_interface.azureai_interface import UseAzureAIInferencePkg
from bot_ai_interface.azureai_interface import UseLangchainPkg

def main():
    ai_client = UseOpenAIPkg()
    messages = [
        {
            "role": "system",
            "content": "You are a helpful assistant.",
        },
        {
            "role": "user",
            "content": "What is the capital of France?",
        }
    ]
    """  response = ai_client.chat_completion(messages)
    print(response) """

    ai_client = UseAzureAIInferencePkg()
    response = ai_client.process_conversation("What's the weather like in London?")
    print(response)

    """     ai_client = UseLangchainPkg()
    response = ai_client.chat_completion(messages)
    print(response) """

if __name__ == "__main__":
    main()