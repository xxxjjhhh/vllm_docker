from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from pydantic import BaseModel, Field

from vllm import AsyncEngineArgs, AsyncLLMEngine, SamplingParams

import os

#################################################################################################

# vLLM init
print("=====================")
print(os.getcwd())
print(os.getenv('MODEL_PATH'))
print("=====================")
model_path = os.getenv('MODEL_PATH')
# "/home/xxxjjhhh/my_model/Meta-Llama-3.1-8B-Instruct/"

engine_args = AsyncEngineArgs(
    model=model_path,
    gpu_memory_utilization=0.95,
    tensor_parallel_size=2
)
llm = AsyncLLMEngine.from_engine_args(engine_args)


# fastapi init

app = FastAPI()

class QueryRequest(BaseModel):

    request_id: str

    query: str
     
    n: int = Field(default=1)
    top_p: float = Field(default=0.7)
    temperature: float = Field(default=0.0)
    max_tokens: int = Field(default=1024)
    seed: int = Field(default=42)

@app.post("/generate")
async def generate_post(request: QueryRequest):

    sent_text = ""

    async def stream_response():

        nonlocal sent_text

        # generating
        sampling_params = SamplingParams(
            n = request.n,
            temperature = request.temperature, 
            top_p = request.top_p,
            repetition_penalty = 1.1,
            max_tokens = request.max_tokens,
            seed = request.seed
        )
        results_generator = llm.generate(request.query, sampling_params, request_id=request.request_id)

        async for output in results_generator:
            text = output.outputs[0].text

            new_text = text[len(sent_text):]
            sent_text = text

            for word in new_text.split(" "):
                if word:  
                    yield word + " "

            if output.finished:
                return

    return StreamingResponse(stream_response(), media_type="text/plain")