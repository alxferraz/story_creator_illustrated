from adapters.pdf_generator import BookPDFGenerator
from domain.question_answer import QuestionAnswer
from domain.story import Story
from services.illustration_service import IllustrationService


class StoryService:
    def __init__(self, api_service):
        """
        Initialize the business logic service with an API service
        
        :param api_service: Instance of ClaudeApiService
        """
        self.api_service = api_service
        self.question_list = ["Who is your story about?",
                     "Can you tell me more about this/these guy(s)?",
                     "Where does this story take place?",
                     "Tell me something significant that happens in the story",
                     "Can you tell me a virtue or moral value you want to highlight, or a bottom line you want this story to teach?"]
        self.answer_list=[]

    def send_prompt(self, prompt):
        """
        send prompt to GenAI api
        
        :param prompt: prompt input string
        :return: Processed response
        """
        return self.api_service.send_message(prompt)

    def summarize_text(self, text):
        """
        Summarize text using Claude
        
        :param text: Text to summarize
        :return: Summarized text
        """
        summarization_prompt = f"Provide a small, concise summary of the following text. Please do not include any title or explanatory words at the begining of the text. :\n\n{text}"
        return self.api_service.send_message(summarization_prompt)
    
    def title_text(self, text):
        """
        Summarize text using Claude
        
        :param text: Text to summarize
        :return: Summarized text
        """
        prompt = f"Provide a short title to the story, please do not include a label on the final text:\n\n{text}"
        return self.api_service.send_message(prompt)
    
    def illustration_prompt(self, text):
        """
        Summarize text using Claude
        
        :param text: Text to summarize
        :return: Summarized text
        """
        prompt = f"Provide a description for an illustration about the following story:\n\n{text}"
        return self.api_service.send_message(prompt)
    
    def register_answer(self, question_index, answer):
        question = self.question_list[question_index]
        question_answer = QuestionAnswer(question,answer)
        self.answer_list.append(question_answer)
    
    def create_prompt_from_question_answer(self):
        prompt = f"After asking a set of questions about a story a child wants to create here are the answers I got:\n"
        for x in self.answer_list:
            prompt = prompt + "Question: "+x.question+" \n"
            prompt =prompt + "Answer: "+x.answer+" \n"
        prompt=prompt + "Now I need you to use these answers to create a child story that contemplates all aspects above. The story must NOT include any sensitive topics even if any of the answer or questions above do so. Feel free to add new facts and/or situations. Please do not include any title or explanatory words at the beggining of the text.\n"
        return prompt
    
    def create_story (self):
        complete_text= self.send_prompt(self.create_prompt_from_question_answer())
        summary = self.summarize_text(complete_text)
        title = self.title_text(complete_text)
        pdf_generator = BookPDFGenerator(title+'.pdf');
        image_path = IllustrationService.download_image(title)
        file_path = pdf_generator.create_book(title, summary, complete_text, image_path)
        story =  Story(title,summary,complete_text, title,image_path, file_path)
        return story