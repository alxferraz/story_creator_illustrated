from services.story_service import StoryService
from adapters.claude_api_adapter import ClaudeApiAdapter

def main():
    # Initialize the  API service
    try:
        api_service = ClaudeApiAdapter()
        story_service = StoryService(api_service)
    except ValueError as e:
        print(f"Initialization Error: {e}")
        return

    print("- I`ve heard you would like to create an awesome story!")
    print("- I think I can help you, can you tell me more about your story?")
    print("*******************************************************")
    
    current_question_index =0
    question_list_length = len(story_service.question_list)

    while True:
        # Get user input
        print(story_service.question_list[current_question_index])
        user_input = input("> ")

        # Check for exit condition
        if user_input.lower() == 'quit':
            print("Exiting the application...")
            break
        story_service.register_answer(current_question_index,user_input)
        current_question_index +=1
        
        if current_question_index == question_list_length:
            try:
                response = story_service.create_story()
                print("\nResponse:")
                print(f"TITLE:{response.title}\n")
                print(f"SUMMARY:{response.summary}\n")
                print(f"COMPLETE_TEXT:{response.complete_text}\n")
                print(f"IMAGE PROMPT:{response.image_prompt}\n")
                print(f"IMAGE PATH:{response.image_path}\n")
            except Exception as e:
                print(f"An error occurred: {e}")
            break

if __name__ == "__main__":
    main()