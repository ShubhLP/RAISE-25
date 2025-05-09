The Master of Public Informatics Program at the Rutgers Bloustein School proudly announces RAISE-25, an innovative Informatics, Data Science, and Artificial Intelligence (AI) competition where students are tasked to envision the scope of AI’s transformative impact on human society. With the theme Our Future with AI: Utopian or Dystopian?, RAISE-25 challenges participants to tackle one of the most profound questions of our time: How will AI shape the future of education, careers, and society?

about

Our tool is a LLM with access to news reports from the last two years. It classifies each article into utopia or dystopia.

examples

python main.py 'how is AI going to affect in photo searching?'

In the realm of photo searching, the impact of AI is multifaceted, as evidenced by recent events:

Google Photos has introduced artificial intelligence photo search, enhancing the search capabilities for users. (Mezha.Media, 2024)
Google's initiative to flag AI-generated images in Search aims to address concerns about the authenticity of visual content. (TechCrunch, 2024)
However, there are concerns raised about AI's influence on photo editing, with reports indicating that AI is both fixing and ruining photos. (The Verge, 2024)
Issues with AI-generated results in Google image search have been highlighted, particularly in relation to celebrity images. (Sherwood News, 2024)
On a positive note, AI-powered visual search has been integrated into the iPhone, offering users enhanced search capabilities. (TechCrunch, 2024)
The industry is grappling with ethical considerations surrounding AI in photography, emphasizing the need to prioritize ethics in this domain. (The Conversation Indonesia, 2024)
Various advancements, such as Google's Project Astra and Ask Photos, showcase the utopian potential of AI in revolutionizing search engines and visual content discovery. (ABC7 Bay Area, 2024)
Getty Images and iStock have leveraged AI to transform visual content discovery, enhancing the search experience for users. (Getty Images, 2024)
Google Photos is set to introduce features that indicate if an image was edited with AI, providing transparency to users. (The Verge, 2024)
The integration of AI in search engines, such as Google's significant update, demonstrates the ongoing evolution of AI in enhancing search functionalities. (The Independent, 2024)
AI-powered editing tools, like Magic Editor, have been made accessible to all Google Photos users for free, democratizing photo editing capabilities. (TechCrunch, 2024)
Meta's shift in labeling from 'Made with AI' to 'AI info' reflects the increasing use of AI in photos and the need for transparency. (TechCrunch, 2024)
Getty Images has introduced an updated AI model, emphasizing speed, quality, and accuracy in visual content discovery. (Getty Images, 2024)
The proliferation of AI-powered photo organizers underscores the positive impact of AI in streamlining photo management processes. (Unite.AI, 2024)
Overall, AI's influence on photo searching is a complex interplay between advancements in technology, ethical considerations, and the need for transparency and user empowerment.

instructions

The tool requires OpenAI api key in the system environment variables.

in the root directory, add two new directories: files and search. In /files, place the competition dataset

run the following script and generate the embedding matrix.

python loading.py
