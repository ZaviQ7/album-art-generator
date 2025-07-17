# Paid Services Setup

The default backend is **OpenAI DALL‑E**.

1. Create an account at <https://platform.openai.com/>.
2. Generate an **API key** and add it to your environment:
   ```bash
   export OPENAI_API_KEY="sk‑..."
   ```
3. Account must hold sufficient credit;
   each 1024×1024 render costs about **$0.04** (July 2025).

### Switching Providers
If you prefer Stable Diffusion or another engine:
* Implement `Provider` subclass inside `generator.py`.
* Set the env var `ART_BACKEND` to its identifier.

