from flask import Flask, request, jsonify
import torch
from transformers import T5ForConditionalGeneration, T5Tokenizer

app = Flask(__name__)

MODEL_DIR = "models/fine_tuned_model"

tokenizer = T5Tokenizer.from_pretrained(MODEL_DIR, local_files_only=True)
model = T5ForConditionalGeneration.from_pretrained(MODEL_DIR, local_files_only=True)
model.eval()

def summarize(text, max_length=64):
    input_text = "summarize: " + text
    inputs = tokenizer(input_text, return_tensors="pt", max_length=128, truncation=True)
    with torch.no_grad():
        outputs = model.generate(
            **inputs,
            max_length=max_length,
            num_beams=4,
            early_stopping=True,
        )
    return tokenizer.decode(outputs[0], skip_special_tokens=True)

@app.route("/summarize", methods=["POST"])
def summarize_endpoint():
    data = request.get_json()
    if not data or "findings" not in data or not data["findings"].strip():
        return jsonify({"error": "Missing or empty findings field in request body."}), 400
    impression = summarize(data["findings"])
    return jsonify({"impression": impression}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
