# Policy LLM

A research project on fine-tuning specialized AI for advanced policy work, building on the study **"Automating public policy: a comparative study of conversational artificial intelligence models and human expertise in crafting briefing notes"** ([link](https://rdcu.be/dYDBq)).

## Research question

Is generative AI reliable enough to tackle the "policy challenge," and does model fine-tuning bring us closer to the acumen of policy briefing note crafting?

A follow-up paper has been accepted for presentation at the **7th Annual Conference of the International Association for Public Policy (ICPP7)**, co-hosted by Chiang Mai University School of Public Policy (July 2–4, 2025; Pre-Conference July 1, 2025). Results will be presented in the panel **T13P04 – Advanced Computational Methods for Public Policy: NLP, ML, and LLMs**, chaired by Antoine Lemor, Louis-Robert Beaulieu-Guay & Igor Tkalec. More information: [ICPP7 Chiang Mai 2025](https://www.ippapublicpolicy.org/conference/icpp7-chiang-mai-2025/21).

## Live model

The fine-tuned model is available at: **http://34.118.169.86/** (hosted on Open WebUI).

As of May 2025, the primary interface is Open WebUI; the legacy Heroku/Flask demo in this repository is discontinued. This repo retains the original web app code for reference and the research artifacts (generated briefing notes and human-written benchmarks).

## Project structure

```
policy-LLM-1/
├── app.py                 # Flask app (legacy chat interface)
├── templates/             # HTML templates for the legacy UI
├── requirements.txt       # Python dependencies
├── requirements-dev.txt   # Dev tools (e.g. linting)
├── .env.example           # Example env vars (copy to .env)
├── Procfile               # Process definition (e.g. Heroku)
├── runtime.txt            # Python version
├── .github/workflows/     # CI (lint, import check)
├── CONTRIBUTING.md
├── SECURITY.md
├── LICENSE
└── README.md
```

## Getting started (legacy Flask app)

For local development or reference:

```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
pip install -r requirements.txt
export OPENAI_API_KEY=your_key_here   # or copy .env.example to .env and set the key
python app.py
```

The app will run at `http://localhost:5000`. The `/chat` endpoint uses the OpenAI API (e.g. `gpt-4o-mini`); ensure `OPENAI_API_KEY` is set.

## Research artifacts

Generated briefing notes from the fine-tuned model and a human-written benchmark are available in this repository.

## Funding

This doctoral research is funded by Canada’s Social Sciences and Humanities Research Council (SSHRC) through the [Vanier Canada Graduate Scholarships](https://vanier.gc.ca/en/home-accueil.html).

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on how to contribute.

## License

This project is licensed under the MIT License — see [LICENSE](LICENSE) for details.

## Contact

**Stany Nzobonimpa**  
PhD Candidate, algorithms, equity and public services delivery  
ÉNAP — École nationale d'administration publique (Gatineau, Québec)  

- Email: [Stany.Nzobonimpa@enap.ca](mailto:Stany.Nzobonimpa@enap.ca)  
- Google Scholar: [profile](https://scholar.google.com/citations?user=aAI6Wf8AAAAJ&hl=en&oi=ao)
