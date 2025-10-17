DeepContent - AI Content Generator

A simple content generation tool that uses Wikipedia for research and AI to create blogs, social media posts, and marketing content.

Problem Statement

Creating content takes time. You need to research the topic thoroughly, write engaging introductions, maintain consistent tone, and ensure accuracy.

DeepContent automates this by pulling facts from Wikipedia and using AI to generate polished content in seconds.

Tech Stack

Python 3.x - Core programming language
Groq API - Fast, free AI inference using Llama 3.3 70B model
Wikipedia API - Real-time context retrieval
python-dotenv - Environment variable management
requests - HTTP API calls

We chose Groq because it's fast, completely free, and doesn't require a credit card.

Features

Smart Research: The tool automatically searches Wikipedia for your topic and uses that information to generate accurate content.

Multiple Content Types: Create blog posts, social media captions, marketing ads, or general posts.

Tone Customization: Choose from informative, engaging, persuasive, or casual tones.

Context-Aware Generation: AI uses verified Wikipedia facts to reduce errors and hallucinations.

Installation and Setup

Prerequisites: Python 3.7 or higher and pip installed on your system.

Step 1: Clone the Repository

git clone <your-repo-url>
cd content-idea-generation

Step 2: Install Dependencies

pip install python-dotenv requests wikipedia-api

Step 3: Get Your Free Groq API Key

Visit Groq Console: https://console.groq.com/keys
Sign up with your Google account (completely free, no credit card needed)
Click "Create API Key" button
Copy your new API key (it will start with gsk_)

Step 4: Configure Environment Variables

Create a file named .env in your project folder and add:

GROQ_API_KEY=your_groq_api_key_here

Important: Never share this file or upload it to GitHub.

Step 5: Run the Application

python main.py

How to Use

Run the script using python main.py

Enter your topic when prompted, for example: Artificial Intelligence

Choose content type or press Enter for default (blog, caption, post, or ad)

Select tone or press Enter for default (informative, engaging, persuasive, or casual)

Wait a few seconds while the AI generates your content

Demo Example

Input:
Enter a topic: Climate Change
Enter content type: blog
Enter tone: informative

Output:
The tool will fetch information from Wikipedia about climate change, then generate a complete blog post with an introduction, body paragraphs, and conclusion based on that research.

Project Structure

content-idea-generation/
    main.py - Main application script
    .env - Environment variables (your API key)
    .gitignore - Files to ignore in git
    README.md - This documentation file

Configuration

You can adjust the creativity level by changing the temperature setting in main.py (line 43). Higher values make output more creative, lower values make it more focused. Default is 0.85.

Available Groq models you can use:
llama-3.3-70b-versatile (default and recommended)
llama-3.1-70b-versatile
mixtral-8x7b-32768

Troubleshooting

If you see "GROQ_API_KEY not found in .env":
Make sure the .env file exists in your project folder
Check that you spelled GROQ_API_KEY correctly

If you see "401 Unauthorized":
Your API key might be wrong
Try generating a new key from Groq Console: https://console.groq.com/keys

If you see "Wikipedia module not found":
Run: pip install wikipedia-api

If Wikipedia fetching is slow:
This is normal for the first request
Check your internet connection

Future Ideas

Add a web interface using Streamlit or Gradio
Support multiple languages
Export content to PDF or Word
Add SEO optimization suggestions
Include image generation
Allow batch processing for multiple topics
Let users upload custom research documents

License

This project is open source and available under the MIT License.

Contributing

Feel free to fork this project, make improvements, and submit pull requests. All contributions are welcome.

Disclaimer

This tool generates AI content, so always review and edit the output before using it. Wikipedia summaries are used only for context. Respect copyright guidelines and give proper attribution where needed. Groq's free tier has rate limits, so check their documentation for details.

Get your free Groq API key: https://console.groq.com/keys

Built using Groq AI and Python
