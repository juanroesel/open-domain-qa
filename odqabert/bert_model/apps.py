from django.apps import AppConfig
from transformers import pipeline
from transformers import DistilBertTokenizer, DistilBertForQuestionAnswering
import torch
from pathlib import Path
import os
from django.utils import timezone

# Sets up logging instance
import logging
from transformers import logging as hf_logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
# Removes verbose messages from Transformers and TensorFlow
hf_logging.set_verbosity_error()

class BertModelConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'bert_model'
    root_path = Path(__file__).parent.parent.parent
    model_path = os.path.join(root_path, "ckpt")
    logger.info(f"{timezone.now()} - Loading QA BERT model from path {model_path}")
    tokenizer = DistilBertTokenizer.from_pretrained('distilbert-base-uncased')
    model = DistilBertForQuestionAnswering.from_pretrained("distilbert-base-uncased")
    checkpoint = torch.load(model_path + "/ckpt_2.pt", map_location=torch.device('cpu'))
    model.load_state_dict(checkpoint['model_state_dict'])
    QA_BERT_model = pipeline("question-answering", model=model, tokenizer=tokenizer)
    logger.info(f"{timezone.now()} - QA BERT model loaded into memory")


