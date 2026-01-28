from transformers import AutoTokenizer, AutoModelForCausalLM

# Load model and tokenizer
tokenizer = AutoTokenizer.from_pretrained("gpt2")
model = AutoModelForCausalLM.from_pretrained("gpt2")

# Input prompt
prompt = "what is python"

# Convert text to tokens
inputs = tokenizer(prompt, return_tensors="pt")

# Generate output tokens
outputs = model.generate(
    inputs["input_ids"],
    max_length=150,
    do_sample=True
)

# Decode tokens to text
result = tokenizer.decode(outputs[0], skip_special_tokens=True)

# PRINT OUTPUT 🔥
print("\nModel Output:\n")
print(result)