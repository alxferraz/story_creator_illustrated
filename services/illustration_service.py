
from adapters.pollinations_api_adapter import PolinationsApiAdapter

class IllustrationService:
   
    def download_image(prompt):
        """
        Download an image generated with the given prompt
        
        :param prompt: Prompt to generate custom image
        :return: Full path to the downloaded image
        """
        try:
            return PolinationsApiAdapter.download_image(prompt)
        except Exception as e:
            print(f"Error downloading image: {e}")
            return None