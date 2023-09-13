# Telegram_AutoReply With Free Hosting
This repository on GitHub is a script to auto reply messages on Telegram account  with free hosting

## Overview
The "Telegram_AutoReply" project is a script hosted on GitHub that enables automatic replies to messages on Telegram account. This script is designed to be hosted for free, making it a cost-effective solution for users who want to automate their Telegram responses.

  ## Installation
  First, you need to get the `api_hash` and `api_id` (also known as `api_key`) from my.telegram.org:
  ### 1. Get your `api_hash`and `api_id`
    1. Open your web browser and navigate to [my.telegram.org](https://my.telegram.org/).
    2. Log in using your Telegram phone number. Telegram will send you a confirmation code via the Telegram app, not SMS.
    3. After logging in, click on 'API development tools'.
    4. Fill out the form with your application details. You can enter any name for your application and a short description.
    5. After you've filled out the form, click on 'Create application' at the end.
    6. You'll now be able to see your `api_id` and `api_hash`. These are important credentials, so make sure to keep them safe and do not share them with anyone.
  
  ### 2. Clone the repository
  
  
  ```bash
  git clone https://github.com/mohammedalakhras/Telegram_AutoReply
  ```
  
  ### 3. Move to project directory
  
  ```bash
  cd Telegram_AutoReply
  ```
  ### 4. Install the required packages
  
  ```bash
  pip install -r requirements.txt
  ```
  
  ### 5. edit `init_session.py` to replace with your `api_id` , `api_hash` adn `@Your_Username`
  
  ### 6. run `init_session.py` 
  ```bash
  python init_session.py
  ```
  then you need to enter your phone and you will recive code to authentication.
  
  after that this code will create session file :`anon.session` 
  
## Free Huggingface Hosting

  you can host this code as `Gradio App` on [Huggingface.co](http://huggingface.co/)
  Sure, here are the steps to create a Gradio app with Hugging Face:
  Sure, here are the steps to create a new Gradio space on Hugging Face:
  
  1. **Go to Hugging Face Spaces**: Navigate to [Hugging Face Spaces](https://huggingface.co/spaces) in your web browser.
  
  2. **Create a New Space**: Click on the 'New Space' button on the top right corner of the page.
  
  3. **Select Gradio as the SDK**: In the 'New Space' form, select 'Gradio' from the 'SDK' dropdown menu.
  
  4. **Fill in the Details**: Provide a name for your space, and optionally a description. You can also choose whether to make your space public or private.
  
  5. **Add Your Gradio App**: Now you can add your Gradio app to this space by uploading `requirements.txt`,`anon.session` and`app.py` in the root directory of your space, and edit your `api_id`,`api_hash` and `@Your_Username` inside it.
  
  6. **Dont Forget uupload `anon.session` file.
  Good Luck! 