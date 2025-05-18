import hashlib

import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from langchain.globals import set_llm_cache
from langchain_community.cache import InMemoryCache
from langchain_community.llms import VLLM

app = FastAPI()

set_llm_cache(InMemoryCache())

# Initialize the vLLM model
llm = VLLM(
    model="Qwen/Qwen3-0.6B",
    trust_remote_code=True,
    max_new_tokens=50,
    temperature=0.6,
    max_model_len=1024,
)

@app.get("/")
def read_root():
    return {"message": "LLM API is running."}

@app.post("/api/v1/prompt")
async def generate_text(request: Request):
    request_data = await request.json()
    user_prompt = request_data.get("prompt", "")
    if not user_prompt:
        return JSONResponse({"error": "Prompt is required."}, status_code=400)

    # Use /no_think directive + clear system instruction to skip thinking output
    full_prompt = (
        "<|im_start|>system\n"
        "You are a helpful AI assistant. Only respond to the user's message without showing your thinking steps. "
        "Avoid using <think> or similar tags. Reply in English unless the user uses another language. Be brief.\n"
        "<|im_end|>\n"
        f"<|im_start|>user\n{user_prompt.strip()} /no_think\n<|im_end|>\n"
        "<|im_start|>assistant\n"
    )

    output = llm.invoke(full_prompt)
    return JSONResponse({"text": output})

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5001)