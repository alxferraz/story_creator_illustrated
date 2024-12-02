import os
from typing import List, Dict, Any
from anthropic import Anthropic

class ClaudeApiAdapter:
    def __init__(self, api_key: str = None):
        """
        Initialize the Claude API service
        
        :param api_key: Optional API key. If not provided, tries to read from environment variable
        """
        # Use provided API key or try to get from environment
        self.api_key = api_key or os.environ.get("ANTHROPIC_API_KEY")
        
        if not self.api_key:
            raise ValueError("No API key provided. Set ANTHROPIC_API_KEY environment variable or pass key directly.")
        
        # Initialize Anthropic client
        self.client = Anthropic(api_key=self.api_key)

    def send_message(self, 
                     message: str, 
                     model: str = "claude-3-haiku-20240307", 
                     max_tokens: int = 400) -> str:
        """
        Send a message to Claude and return its response
        
        :param message: User's message to send
        :param model: Claude model to use
        :param max_tokens: Maximum number of tokens in response
        :return: Claude's text response
        """
        try:
            # Create message request
            response = self.client.messages.create(
                model=model,
                max_tokens=max_tokens,
                messages=[
                    {
                        "role": "user", 
                        "content": message
                    }
                ]
            )
            
            # Return the text of the first content block
            return response.content[0].text
        
        except Exception as e:
            print(f"API call error: {e}")
            return f"An error occurred: {e}"