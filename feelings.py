from transformers import GPT2LMHeadModel, GPT2Tokenizer

def chat_with_ai(prompt):
    model_name = "gpt2"
    tokenizer = GPT2Tokenizer.from_pretrained(model_name)
    model = GPT2LMHeadModel.from_pretrained(model_name)

    inputs = tokenizer.encode(prompt, return_tensors="pt")
    outputs = model.generate(inputs, max_length=150, num_return_sequences=1)
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    
    return response.strip()

if __name__ == "__main__":
    user_input = input("You: ")
    print("AI:", chat_with_ai(user_input))


