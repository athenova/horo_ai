from simple_blogger import SimplestBlogger
from string import Template
from datetime import datetime

class Project(SimplestBlogger):
    def __init__(self, **kwargs):
        super().__init__(            
            review_chat_id=-1002374309134,
            **kwargs)

    def _example_task_creator(self):
        prompt = Template(f"Составь гороскоп на $$date для знака '$sign', используй смайликии, используй не более {self.topic_word_limit} слов")
        return [{ 
            "pisces_prompt": prompt.substitute(sign='Рыбы'),
            "aries_prompt": prompt.substitute(sign='Овен'),
            "taurus_prompt": prompt.substitute(sign='Телец'),
            "gemini_prompt": prompt.substitute(sign='Близнецы'),
            "cancer_prompt": prompt.substitute(sign='Рак'),
            "leo_prompt": prompt.substitute(sign='Лев'),
            "virgo_prompt": prompt.substitute(sign='Дева'),
            "libra_prompt": prompt.substitute(sign='Весы'),
            "scorpio_prompt": prompt.substitute(sign='Скорпион'),
            "sagittarius_prompt": prompt.substitute(sign='Стрелец'),
            "capricorn_prompt": prompt.substitute(sign='Козерог'),
            "aquarius_prompt": prompt.substitute(sign='Водолей'),
        }]
    
    def _preprocess_text_prompt(self, prompt):
        return Template(prompt).substitute(date = datetime.today().strftime('%Y-%m-%d'))
    
    def _system_prompt(self, _):
        return f"Ты - профессиональный астролог"
    
