import os
from bot_utils.load_envs import get_env
from typing import List, Dict, Any





# OpenAI package
from openai import OpenAI
class UseOpenAIPkg:
    def __init__(self):
        self.client = OpenAI(
            base_url=get_env("GITHUB_INFERENCE_ENDPOINT"),
            api_key=get_env("GITHUB_TOKEN"),
        )

    def chat_completion(
        self,
        messages: List[Dict[str, str]],
        model: str = "gpt-4o",
        temperature: float = 1,
        max_tokens: int = 4096,
        top_p: float = 1
    ) -> str:
        try:
            response = self.client.chat.completions.create(
                messages=messages,
                model=model,
                temperature=temperature,
                max_tokens=max_tokens,
                top_p=top_p
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"Error occurred: {str(e)}"

# Azure AI Inference package
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential       
class UseAzureAIInferencePkg:
    def __init__(self):
        # https://learn.microsoft.com/en-us/python/api/overview/azure/ai-inference-readme?view=azure-python-preview
        # https://learn.microsoft.com/en-us/azure/ai-studio/reference/reference-model-inference-api?tabs=python
        # https://learn.microsoft.com/en-us/azure/ai-studio/reference/reference-model-inference-chat-completions
        self.client = ChatCompletionsClient(
            endpoint=str(get_env("GITHUB_INFERENCE_ENDPOINT")),
            credential=AzureKeyCredential(str(get_env("GITHUB_TOKEN"))),
        )

    def chat_completion(
        self,
        messages: List[Dict[str, str]],
        model: str = "gpt-4o",
        temperature: float = 1,
        max_tokens: int = 4096,
        top_p: float = 1
    ) -> str:
        try:
            # Convert dictionary messages to Azure SDK message types
            azure_messages = []
            for msg in messages:
                """
                if msg["role"] == "system":
                    azure_messages.append(SystemMessage(content=msg["content"]))
                elif """
                if msg["role"] == "user":
                    azure_messages.append(UserMessage(content=msg["content"]))
            print(azure_messages)
            response = self.client.complete(
                messages=azure_messages,
                model=model,
                temperature=temperature,
                max_tokens=max_tokens,
                top_p=top_p
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"Error occurred: {str(e)}"

# Langchain package
from langchain_azure_ai.chat_models import AzureAIChatCompletionsModel
from langchain_core.messages import HumanMessage, SystemMessage      
class UseLangchainPkg:
    def __init__(self):
        self.client = AzureAIChatCompletionsModel(
            endpoint=get_env("GITHUB_INFERENCE_ENDPOINT"),
            credential=get_env("GITHUB_TOKEN"),
            model_name="gpt-4o",
        )

    def chat_completion(
        self,
        messages: List[Dict[str, str]],
        model: str = "gpt-4o",
        temperature: float = 1,
        max_tokens: int = 4096,
        top_p: float = 1
    ) -> str:
        try:
            # Convert dictionary messages to Langchain message types
            langchain_messages = []
            for msg in messages:
                if msg["role"] == "system":
                    langchain_messages.append(SystemMessage(content=msg["content"]))
                elif msg["role"] == "user":
                    langchain_messages.append(HumanMessage(content=msg["content"]))
            
            response = self.client.invoke(
                langchain_messages,
            )
            return response.content
        except Exception as e:
            return f"Error occurred: {str(e)}"