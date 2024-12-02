import os
import urllib
import requests
import tempfile

class PolinationsApiAdapter:
    def download_image(prompt):
        """
        Download an image from Polinations using the given prompt
        :return: Full path to the downloaded image
        """

        temp_dir = tempfile.gettempdir()
        illustration_prompt="child book illustration title "
        image_url = "https://image.pollinations.ai/prompt/"
        try:
            url_prompt = urllib.parse.quote(illustration_prompt+prompt);
            # Send GET request to the URL
            response = requests.get(image_url+url_prompt)
            
            # Raise an exception for bad responses
            response.raise_for_status()
            
            # Determine file extension from content type
            content_type = response.headers.get('content-type', '').lower()
            if 'image/jpeg' in content_type:
                ext = '.jpg'
            elif 'image/png' in content_type:
                ext = '.png'
            elif 'image/gif' in content_type:
                ext = '.gif'
            else:
                ext = '.jpg'  # Default to jpg if unknown
            
            # Generate filename if not provided
        
            filename = f"img_{prompt.replace(" ", "")}{ext}"
            
            # Full path in temp directory
            file_path = os.path.join(temp_dir, filename)
            
            # Write the content to a file
            with open(file_path, 'wb') as file:
                for chunk in response.iter_content(chunk_size=8192):
                    file.write(chunk)
            
            return file_path
        
        except requests.RequestException as e:
            print(f"Error downloading image: {e}")
            return None