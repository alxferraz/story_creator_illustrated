# Python Illustrated Stories Creator
A Python app for creating small, illustrated, children`s book stories.

## Why?
Since children stories are often simple they make the perfect candidates for small stories created using GenAI tools like Anthropic's Claude.ai. As children are essentialy visual beings it seems really important to add illustrations whenever possible.
The app will ask questions about the main characters, their features, places where the story takes place and more and then prompt Claude for a story that contemplates all the aspects informed by the user. Once the story's complete text is returned from the API the app prompts Claude for a title for the final text a summary, and an illustration from (Pollinations.ai)[https://pollinations.ai/] to combine it all into a a single PDF file.

## How to run

Set your Claude API key using

`export ANTHROPIC_API_KEY='<API_KEY>'`

Make sure you have the following pip packages installed

`pip3 install anthropic`
`pip3 install requests`
`pip3 install reportlab`

Run using

`python3 main.py`

The output is a PDF file with the story and an illustration at the project`s root folder

## Use Limitations

- The app runs locally in a console.
- The app restricts the content type to child stories and has some measures to avoid sensitive and controversial themes.
- User informed contexts are not persisted between creation sessions.
- Story's complete texts are limited to 400 characters
- The user's answers are not persisted anywhere once the app terminates

