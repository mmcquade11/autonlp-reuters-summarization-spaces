
from newspaper import Article
from newspaper import Config
import gradio as gr
from gradio.mix import Parallel, Series

def extrac_text(url):
  USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:78.0) Gecko/20100101 Firefox/78.0'
  config = Config()
  config.browser_user_agent = USER_AGENT
  config.request_timeout = 10
  
  article = Article(url, config=config)
  article.download()
  article.parse()
  text = article.text
  return text

extractor = gr.Interface(extrac_text, 'text', 'text')
summarizer = gr.Interface.load("huggingface/mmcquade11/autonlp-reuters-summarization-34018133")
sample_url = [['https://finance.yahoo.com/news/intuit-shares-hit-record-highs-quarter-blows-past-estimates-160822839.html'],
]
desc =  '''
         The news summarizer app uses an AutoNLP model trained on the Reuters dataset.
        '''
iface = Series(extractor, summarizer, 
  inputs = gr.inputs.Textbox(
      lines = 2,
      label = 'Enter URL below'
  ),
  outputs = 'text',
  title = 'News Summarizer',
  theme = 'grass',
  layout = 'horizontal',
  description = desc,
  examples=sample_url)
iface.launch()
