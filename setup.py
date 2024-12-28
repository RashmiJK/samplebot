from setuptools import setup, find_packages

setup(
    name="my_bot",
    version="0.1",
    packages=find_packages(),
    # Add any package dependencies here
    install_requires=[
        # example: "requests>=2.25.1",
        "openai",
        "python-dotenv",
        "azure-ai-inference>=1.0.0b6",
        "langchain_azure_ai",
        "langchain_core",
        "pydantic",
    ],
    # Optional metadata
    author="Rashmi",
    description="A brief description of your bot",
)