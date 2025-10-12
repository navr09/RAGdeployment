from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

class Generator:
    def __init__(self, model_name="google/flan-t5-base"):
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

    def generate(self, context, question, max_length=128):
        input_text = f"Context: {context}\nQuestion: {question}"
        inputs = self.tokenizer(input_text, return_tensors="pt")
        outputs = self.model.generate(**inputs, max_length=max_length)
        return self.tokenizer.decode(outputs[0], skip_special_tokens=True)

'''
🤖 How It Differs From Mistral (and Other Decoder-only LLMs)
Aspect	        FLAN-T5 (Seq2Seq)	                        Mistral / LLaMA (Decoder-only LLM)

Architecture	Encoder–Decoder	                            Decoder-only Transformer

Input Type	    Source → Target (conditional 	            Continues text (causal generation)
                        generation)

Training 	    Text-to-text tasks 	                        Next-token prediction on massive corpus
Objective       (translation, summarization, Q&A)

Prompt Format	Structured instructions like 	            Chat-style or completion-style prompts
                "Context: ... Question: ..."

Context Handling Shorter context window (~512–1024 tokens)	Large context (4K–32K+ tokens)
                (good for focused tasks)

Output Control	Easier to constrain outputs 	            More open-ended, harder to constrain
                (good for factual Q&A)

Inference Cost	Light (few hundred MB)	                    Heavy (many GB, needs GPU)
Best For	    RAG-style Q&A, summarization,	            Chatbots, creative writing, multi-turn reasoning
                reasoning with short context

Compute Needs	Can run on CPU	                            Typically needs GPU
'''