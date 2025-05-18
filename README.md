# FastAPI-vLLM

A FastAPI web service that integrates with vLLM to serve language model inferences.

## Overview

This project provides a simple REST API to generate text from an LLM (Language Learning Model) using vLLM. The application uses Qwen/Qwen3-0.6B as the default model and runs on CPU.

## Features

- REST API for inference with the LLM
- Built with FastAPI for high performance
- Uses vLLM for efficient language model inference
- Docker containers for easy deployment
- Log monitoring with Dozzle

## Prerequisites

- Docker and Docker Compose
- Git

## Installation

### Using Docker (Recommended)

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd fastapi-vllm
   ```

2. Build and start the container using Docker Compose:
   ```bash
   docker compose up -d
   ```

   This will:
   - Build the Docker image
   - Install vLLM from source optimized for CPU
   - Start the FastAPI server on port 5001
   - Start Dozzle for log monitoring on port 8080

### Manual Setup

1. Clone the repository:
```bash
git clone https://github.com/Kentakoong/fastapi-vllm
cd fastapi-vllm
```

Beyond this step, I recommend to create a python env first, before installing

2. Install vLLM

- For GPUs - [https://docs.vllm.ai/en/latest/getting_started/installation/gpu.html](https://docs.vllm.ai/en/latest/getting_started/installation/gpu.html)
- For CPUs - [https://docs.vllm.ai/en/latest/getting_started/installation/cpu.html](https://docs.vllm.ai/en/latest/getting_started/installation/cpu.html)

3. Install project dependencies:
```bash
pip install -r requirements.txt
```

4. Run the server:

- via `python`

Keep in mind your RAM, if using CPU, make sure to set `VLLM_CPU_KVCACHE_SPACE`

```bash
python app.py
```

- via `docker compose`

```bash
docker compose up -d --build
```

## Environment Variables

- `VLLM_CPU_KVCACHE_SPACE`: Set to 8 by default in the Docker setup to control memory usage 